#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_str = f'{url}users/'
    todos_str = f'{url}todos/'
    file = 'todo_all_employees.json'

    res = requests.get(user_str, timeout=5)
    users = res.json()

    res = requests.get(todos_str, timeout=5)
    tasks = res.json()

    all_tasks = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        all_tasks[user_id] = []
        for task in tasks:
            if user_id == task.get('userId'):
                all_tasks[user_id].append({"username": username,
                                           "task": task.get('title'),
                                           "completed": task.get('completed')})

    with open(file, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)
