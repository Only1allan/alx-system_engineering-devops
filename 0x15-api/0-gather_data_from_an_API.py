#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user_str = f'{url}users/{user_id}'
    todos_str = f'{url}todos?userId={user_id}'
    employee_str = "Employee {} is done with tasks"

    res = requests.get(user_str, timeout=5)
    print(employee_str.format(res.json().get('name')), end="")

    res = requests.get(todos_str, timeout=5)
    tasks = []
    for task in res.json():
        if task.get('completed') is True:
            tasks.append(task)

    print(f"({len(tasks)}/{len(res.json())}):")
    for task in tasks:
        print(f"\t {task.get('title')}")
