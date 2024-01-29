#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in CSV format.

"""

import csv
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url, timeout=5)
    json_o = r.json()
    with open("todo_all_employees.csv", "w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for user in json_o:
            url = f"https://jsonplaceholder.typicode.com/todos?userId=\
            {user.get('id')}"
            r = requests.get(url, timeout=5)
            json_o = r.json()
            for task in json_o:
                writer.writerow([user.get("id"), user.get("username"),
                                 task.get("completed"), task.get("title")])
