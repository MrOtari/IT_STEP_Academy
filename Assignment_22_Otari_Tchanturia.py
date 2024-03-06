import json

with open("movies.json", "r") as json_file:
    python_data = json.load(json_file)

print(type(python_data))

for i in python_data:
    print(i["page"])
    for j in i["results"]:
        print(j["release_date"][0:4])
        print(j["title"])
