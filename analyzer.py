import json

with open("pools.json") as f:
    pools=json.load(f)

for pool in pools:
    print(pool["name"], pool["apy"])
