#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    employee = "Employee {} is done with tasks({}/{}):"

    r_users = requests.get(url_users, timeout=5).json()
    r_todos = requests.get(url_todos, timeout=5).json()

    for user in r_users:
        if user.get('id') == int(user_id):
            name = user.get('name')
            break

    done_tasks = []
    for task in r_todos:
        if task.get('completed') is True:
            done_tasks.append(task.get('title'))

    print(employee.format(name, len(done_tasks), len(r_todos)))
    for task in done_tasks:
        print("\t {}".format(task))
