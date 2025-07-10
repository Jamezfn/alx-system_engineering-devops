#!/usr/bin/env python
"""Gather data from an API"""
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    complete = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{})".format(user.get('name'), len(complete),
                                                         len(todo)))
    for c in complete:
        print("\t {}".format(c))
