import requests
import sys


id = sys.argv[1]
request_user = requests.get('https://jsonplaceholder.typicode.com/users/'+id)
request_todos = requests.get('https://jsonplaceholder.typicode.com/users/'+id+'/todos')

data_user = request_user.json()
data_todos = request_todos.json()

completed = 0
for i in data_todos:
    if i.get('completed')==True:
        completed = completed + 1


print ('Employee {} is done with tasks({}/{}):'.format(data_user.get('name'), completed,len(data_todos)))


for item in data_todos:
    if item.get('completed') == True:
        print('\t ' + item.get('title'))   