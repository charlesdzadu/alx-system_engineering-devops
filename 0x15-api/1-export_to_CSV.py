#!/usr/bin/python3

"""Gather data from an API and export data to CSV"""

import csv
import requests
from sys import argv


if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users/{}".format(argv[1])).json()
    todos = requests.get(base_url + "todos?userId".format(argv[1])).json()

    with open("{}.csv".format(argv[1]), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([argv[1], users.get("username"),
                             task.get("completed"), task.get("title")])


