#!/usr/bin/python3
# Getting api information

import requests
import sys

try:

    user = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    todos = 'https://jsonplaceholder.typicode.com/todos'
    request_td = requests.get(todos)
    request_usr = requests.get(user)
    imported_users = request_usr.json().get('name')
    imported_tasks = request_td.json()

    tasks = []
    completed_count = 0
    todos_count = 0

    for task in imported_tasks:
        if task.get('userId') == int(sys.argv[1]):
            todos_count += 1
            if task.get('completed') is True:
                completed_count += 1
                tasks.append(task.get('title'))

    print ("Employee {} is done with tasks({}/{}):".format(imported_users,
                                                           completed_count,
                                                           todos_count))

    for task_lines in tasks:
        print("\t {}".format(task_lines))

except Exception as err:
    pass
