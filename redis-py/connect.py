import json
import time

import numpy as np
import pandas as pd
import redis
import requests
from redis.commands.search.field import (
    NumericField,
    TagField,
    TextField,
    VectorField,
)
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query


response = requests.get("https://raw.githubusercontent.com/bsbodden/redis_vss_getting_started/main/data/bikes.json")
bikesData = response.json()
print(f"bikesData: {bikesData}")


json.dumps(bikesData[0], indent=2)
client = redis.Redis(host="localhost", port=6379, decode_responses=True)

assert(client.ping()==True)



## Insert
pipeline = client.pipeline()
for i, bike in enumerate(bikesData, start=1):
    redis_key = f"bikes:{i:03}"
    pipeline.json().set(redis_key, "$", bike)
res = pipeline.execute()
# >>> [True, True, True, True, True, True, True, True, True, True, True]


## Search
res = client.json().get("bikes:010", "$.model")
print(f"client.json().get(\"bikes:010\", \"$.model\"): {res}")



keys = sorted(client.keys("bikes:*"))
print(f"client.keys(\"bikes:*\")): {keys}")
# >>> ['bikes:001', 'bikes:002', ..., 'bikes:011']
