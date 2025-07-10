#!/usr/bin/env python
"""Export to CSV"""
import requests
import sys
import csv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("name")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    with open(f"{sys.argv[1]}.csv", "w" ) as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([
                sys.argv[1],
                username,
                t.get("completed"),
                t.get("title")
                ])
