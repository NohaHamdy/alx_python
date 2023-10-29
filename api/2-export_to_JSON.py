"""
    This script gathers employee todo data and stores it in JSON format
"""
import json
import requests
import sys

def save_todo_progress_to_json(id):
    """
    fetching employee data
    """
    # user details
    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"

    # setch user details
    user_response = requests.get(user_url)

    # check whether user exists
    if user_response.status_code != 200:
        print(f"Employee with ID {id} not found.")
        return

    # parse response to obtain user data
    user_data = user_response.json()
    username = user_data["username"]

    # url for tasks
    tasks_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    # fetch user's tasks
    tasks_response = requests.get(tasks_url)

    # check whether the tasks were fetched
    if tasks_response.status_code != 200:
        print(f"Unable to fetch TODO list for employee with ID {id}.")
        return

    # parse to obtain data
    tasks_data = tasks_response.json()

    # creating json data
    json_data = {
        str(id): [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": username,
            }
            for todo in tasks_data
        ]
    }


    # creating a json file
    json_filename = f"{id}.json"
    with open(json_filename, "w") as json_file:
        json.dump(json_data, json_file, indent=4)



if __name__ == "__main__":
    # get the user id from command-line argument
    id = int(sys.argv[1])

    # calling the function to export all data to json file
    save_todo_progress_to_json(id)