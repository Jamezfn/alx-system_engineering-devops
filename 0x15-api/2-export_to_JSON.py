#!/usr/bin/env python

import sys
import requests
import json

url = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    user_id = sys.argv[1]
    user = requests.get(url + f"users/{user_id}").json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    output = {
        user_id: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user.get("name", "")
            }
            for todo in todos
        ]
    }
    with open(f"{user_id}.json", "w", encoding="utf-8") as jsonfile:
        json.dump(output, jsonfile)
