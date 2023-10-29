#!/usr/bin/python3

import csv
import requests
import sys


user_id = str(sys.argv[1])
request_user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
request_todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)

data_user = requests.get(request_user).json()
data_todos = requests.get(request_todos).json()
filename = f"{user_id}.csv"


with open(filename, "w", newline="") as file:
    csvwriter = csv.writer(file, quoting=csv.QUOTE_ALL)
    for task in data_todos:
        csvwriter.writerow(
            [user_id, str(data_user["username"]), task["completed"], task["title"]]
        )