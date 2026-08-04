import json


def load_test_data():

    with open("data/users.json") as file:
        return json.load(file)


def get_user(username):

    data = load_test_data()

    return data[username]


def get_customer():

    data = load_test_data()

    return data["customer"]


def load_login_data():

    data = load_test_data()

    return [
        (
            user["username"],
            user["password"],
            user["expected_error"]
        )
        for user in data.values()
        if "expected_error" in user
    ]
