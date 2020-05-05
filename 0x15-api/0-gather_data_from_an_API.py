#!/usr/bin/python3
"""
Module for retreiving info from API
"""
import requests
from sys import argv

if __name__ == "__main__":
    completed = 0
    total = 0
    completed_titles = []
    url = "https://jsonplaceholder.typicode.com/users/{}/".format(argv[1])
    user = requests.get(url).json()["name"]
    tasks = requests.get(url + "todos/").json()
    for task in tasks:
        if task["completed"] is True:
            completed += 1
            completed_titles.append(task["title"])
        total += 1

    print("Employee {} is done with tasks({}/{}):".format(user,
                                                          completed, total))
    for title in completed_titles:
        print("\t {}".format(title))
