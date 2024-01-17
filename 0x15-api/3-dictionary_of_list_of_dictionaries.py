#!/usr/bin/python3
"""Gather data from an API and export data to JSON"""


import json
import requests
from sys import argv


if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users").json()

    json_dict = {}
    for user in users:
        todos = requests.get(base_url + "todos?userId={}".format(
            user.get("id"))).json()
        json_dict[user.get("id")] = [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")} for task in todos]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_dict, jsonfile)


