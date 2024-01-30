#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in CSV format.

"""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user_str = f'{url}users/{user_id}'
    todos_str = f'{url}todos?userId={user_id}'
    file = f'{user_id}.csv'

    res = requests.get(user_str, timeout=5)
    username = res.json().get('username')

    res = requests.get(todos_str, timeout=5)
    tasks = []
    for task in res.json():
        tasks.append([user_id, username,
                      task.get('completed'), task.get('title')])
    with open(file, 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks)
