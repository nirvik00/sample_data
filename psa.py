import json

with open("spatial_adjacency.json", "r") as f:
    input = json.loads(f.read())

arr =[]

for k, v in input.items():
    print(k)
    d = dict()
    d[k] = v
    arr.append(d)

with open("data.json", "w") as f:
    f.write(json.dumps(arr))