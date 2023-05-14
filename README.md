# Description
Item-to-item collaborative filters compute the 
similarity between items to recommend new items to users. 
This repo contains code for training a kNearestNeighbor for providing similar items 
and scripts for deployment with FastApi and Docker.

## Files
- `item_to_item_cf.ipynb` analyses and processes the data and 
develops an item-to-item collaborative filter.
- `main.py` is the API containing an endpoint that can be called with an `item_id` and number `top_k`, 
creates a list of k similar items.
- `test_main.py` for testing the API with pytest.

## Usage

1. Run the app.
    ```commandline
    uvicorn main:app --reload
    ```
   Send request.
    ```commandline
    curl -X POST -H "Content-Type: application/json" \
        -d '{
        "item_id": 1,
        "top_k": 3
    }'  http://127.0.0.1:8000/recommend
    ```

    Optionally specify port and host:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 80
    ```

3. Docker

   Create and run Docker image.
   ```commandline
   docker build -t {name}/{api-name}:latest .
   ```
   Verify that the build ran successfully:
   ```commandline
   docker run -d -p 8000:80 {name}/{api-name}:latest
   curl -X POST 'http://localhost:8000/recommend' --header 'Content-Type: application/json' --data-raw '{"item_id":1, "top_k":3}'
   ```
4. Pytest Run

   Run pytest with:
   ```
   pytest
   ```