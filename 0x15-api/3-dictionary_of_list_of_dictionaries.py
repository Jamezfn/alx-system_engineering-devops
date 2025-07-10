#!/usr/bin/env python

import requests
import json

url = "https://jsonplaceholder.typicode.com/"

if __name__ == '__main__':
    user = requests.get(url + "users").json()

    output = {
            u.get("id"): [
                {
                    "username": u.get("name"),
                    "task": t.get("title"),
                    "completed": t.get("completed")
                    } for t in requests.get(url + "todos", params={"userId": u.get("id")}).json()]
                for u in user
            }

    with open("todo_all_employees.json", "w", encoding="utf-8") as jsonfile:
        json.dump(output, jsonfile)
