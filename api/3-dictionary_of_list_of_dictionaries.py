#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_output = get(user_url).json()

    main_data = {}
    for user in user_output:
        tasks = []

        fix = "https://jsonplaceholder.typicode.com"
        tasks_url = fix + "/user/{}/todos".format(user.get("id"))
        names_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            user.get("id")
        )

        tasks_output = get(tasks_url).json()
        names_output = get(names_url).json()
        for todo in tasks_output:
            tasks_dict = {}
            tasks_dict.update(
                {
                    "username": names_output.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                }
            )
            tasks.append(tasks_dict)

        main_data.update({user.get("id"): tasks})

    with open("todo_all_employees.json", "w") as f:
        dump(main_data, f)