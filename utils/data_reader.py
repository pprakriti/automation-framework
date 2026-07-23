import json

def load_test_data():

    with open("data/users.json") as file:

        return json.load(file)