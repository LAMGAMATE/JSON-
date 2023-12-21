import json

# Q1
data = {
    "nom": "Jean",
    "age": 25,
    "ville": "Paris"
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Q2
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print("Contenu du fichier JSON avant la modification :")
    print(loaded_data)

# Q3
loaded_data["langage"] = "Python"

# Q4
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file)

# Q5
with open('data.json', 'r') as json_file:
    modified_data = json.load(json_file)
    print("\nContenu du fichier JSON après la modification :")
    print(modified_data)