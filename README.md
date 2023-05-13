Item-to-item collaborative filters compute the 
similarity between items to recommend new items to users. 

Files:
- `item_to_item_cf.ipynb` analyses and processes the data and 
develops an item-to-item collaborative filter.
- `main.py` is the API containing an endpoint that can be called with an `item_id` and number `top_k`, 
creates a list of k similar items.

Run the app with:

```bash
> uvicorn main:app --host 0.0.0.0 --port 80
```

Send request:
```commandline
curl -X POST -H "Content-Type: application/json" \
    -d '{
    "item_id": 1,
    "top_k": 3
}'  http://0.0.0.0:80/recommend
```

Run the test with:

```
> pytest
```