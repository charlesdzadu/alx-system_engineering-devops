#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv


if __name__ == "__main__":
    
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users/{}".format(argv[1])).json()
    todos = requests.get(base_url + "todos?userId".format(argv[1])).json()

    completed_tasks = []
    for task in todos:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        users.get("name"), len(completed_tasks), len(todos)))

    for task in completed_tasks:
        print("\t {}".format(task))

