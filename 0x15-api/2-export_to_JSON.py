#!/usr/bin/python3

"""Gather data from an API and export data to JSON"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users/{}".format(argv[1])).json()
    todos = requests.get(base_url + "todos?userId".format(argv[1])).json()

    with open("{}.json".format(argv[1]), "w") as jsonfile:
        json.dump({argv[1]: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": users.get("username")} for task in todos]}, jsonfile)
