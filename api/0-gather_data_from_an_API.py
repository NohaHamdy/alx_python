'''
import requests

import sys



def  get_data(id):
    user_data_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    user_todos_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    output = 0


    user_data = requests.get(user_data_url)
    user_todo = requests.get(user_todos_url)

    json_output = user_data.json()
    emp_name = json_output["name"]
    json_user_todo = user_todo.json()
    total_tasks = len(json_user_todo)

    m = []
    for task in user_todo.json():
        if task["completed"]:
            output += 1
            m.append(task["title"])


    print(f'Employee {emp_name} is done with tasks ({output}/{total_tasks}):')
    for task_title in m:
        print(f'\t{task_title}')


if __name__ =='__main__':
    id = sys.argv[1]
    get_data(id)
    '''
    
    
import requests
import json

# Define the REST API endpoints
EMPLOYEE_DETAILS_ENDPOINT = "https://jsonplaceholder.typicode.com/users/{}"
EMPLOYEE_TODO_ITEMS_ENDPOINT = "https://jsonplaceholder.typicode.com/users/{}/todos"

# Define a function to get the employee details
def get_employee_details(employee_id):
    response = requests.get(EMPLOYEE_DETAILS_ENDPOINT.format(employee_id))
    employee_details = json.loads(response.content.decode())
    return employee_details

# Define a function to get the employee TODO items
def get_employee_todo_items(employee_id):
    response = requests.get(EMPLOYEE_TODO_ITEMS_ENDPOINT.format(employee_id))
    employee_todo_items = json.loads(response.content.decode())
    return employee_todo_items

# Define a function to calculate the employee TODO list progress
def calculate_employee_todo_list_progress(employee_todo_items):
    number_of_done_tasks = 0
    total_number_of_tasks = len(employee_todo_items)
    for employee_todo_item in employee_todo_items:
        if employee_todo_item["completed"]:
            number_of_done_tasks += 1
    return number_of_done_tasks / total_number_of_tasks

# Define a function to display the employee TODO list progress on the standard output
def display_employee_todo_list_progress(employee_name, employee_todo_list_progress):
    print("Employee {} is done with tasks {}/{}".format(employee_name, employee_todo_list_progress["number_of_done_tasks"], employee_todo_list_progress["total_number_of_tasks"]))
    for completed_task in employee_todo_list_progress["completed_tasks"]:
        print("\t {}".format(completed_task))

# Get the employee ID from the user
employee_id = int(input("Enter the employee ID: "))

# Get the employee details
employee_details = get_employee_details(employee_id)

# Get the employee TODO items
employee_todo_items = get_employee_todo_items(employee_id)

# Calculate the employee TODO list progress
employee_todo_list_progress = calculate_employee_todo_list_progress(employee_todo_items)

# Display the employee TODO list progress on the standard output
display_employee_todo_list_progress(employee_details["name"], employee_todo_list_progress)
  