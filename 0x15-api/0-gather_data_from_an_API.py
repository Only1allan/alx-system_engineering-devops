#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

"""

import sys
import requests

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    r = requests.get(url, timeout=5)
    json_o = r.json()
    name = json_o.get("name")
    url = f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}"
    r = requests.get(url, timeout=5)
    json_o = r.json()
    completed_tasks = []
    for task in json_o:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))
    print(f"Employee {name} is done with tasks \
        ({len(completed_tasks)}/{len(json_o)}):")
    for task in completed_tasks:
        print(f"\t {task}")
