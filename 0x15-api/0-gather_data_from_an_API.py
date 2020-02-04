#!/usr/bin/python3
""" GEtting api information """

import requests
import sys

user = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
todos = 'https://jsonplaceholder.typicode.com/todos'
request_td = requests.get(todos)
request_usr = requests.get(user)
imported_users = request_usr.json().get('name')
imported_tasks = request_td.json()

tasks = []
completed_count = 0

for task in imported_tasks:
    if task.get('userId') == int(sys.argv[1]):
        if task.get('completed') is True:
            completed += 1
            tasks.append(task.get('title'))

print ("Employee {} is done with tasks({}/{})".format(task, user, completed))
