from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from joblib import load
from sklearn.neighbors import NearestNeighbors


class RecommendationRequest(BaseModel):
    item_id: int
    top_k: int


class RecommendationResponse(BaseModel):
    item_id: int
    recommended_items: List[int]


app = FastAPI(
    title="Item-to-item recommender API",
    description="A simple API which takes input parameters and outputs list of recommendations")


@app.on_event("startup")
def load_model():
    model = load("final_model.joblib")
    app.model = model


@app.post("/recommend", response_model=RecommendationResponse)
def recommend(item_request: RecommendationRequest):
    """
    Recommend items similar to the item given in the request.
    :param item_request: Request containing item_id and number of items to be returned.
    :return: list of similar items
    """
    model = app.model
    item_id = item_request.item_id
    top_k = item_request.top_k

    if item_id not in model.media_mapper.keys():
        raise HTTPException(status_code=404, detail="Item not found")

    if top_k > model.get_params()['n_neighbors']:
        raise IndexError("Top_k too high")

    prediction = find_similar_items(item_id, model, top_k)
    return RecommendationResponse(item_id=1, recommended_items=prediction)


def find_similar_items(item_id: int, model: NearestNeighbors, k: int) -> List[int]:
    """
    Find similar items using KNN.
    :param item_id: The id of the item
    :param model: A dimension reduction model used to find similar items
    :param k: The number of similar items returned.
    :returns List with similar ids
    """
    neighbour_ids = []

    item_id = model.media_mapper[item_id]
    item_vec = model._fit_X[item_id]
    k += 1
    item_vec = item_vec.reshape(1, -1)
    neighbour = model.kneighbors(item_vec, return_distance=False)

    for i in range(k):
        n = neighbour.item(i)
        neighbour_ids.append(model.media_inv_mapper[n])
    # We don't want to recommend this item_id itself
    neighbour_ids.pop(0)
    return neighbour_ids[:k]
