#!/usr/bin/python3

"""
Using what you did in the task #0, extend your Python script to
export data in the JSON format.
Records all tasks from all employees.
"""


if __name__ == '__main__':
    import json
    import requests

    api_url = 'https://jsonplaceholder.typicode.com/todos'

    response = requests.get(api_url)
    todos = response.json()
    todos_by_user = {}

    for todo in todos:
        user_id = todo['userId']
        if user_id not in todos_by_user:
            todos_by_user[user_id] = []

        todos_by_user[user_id].append({
            'username': '',
            'task': todo['title'],
            'completed': todo['completed']
        })

    usernames_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(usernames_url)
    usernames = response.json()

    for user_id, user_todos in todos_by_user.items():
        username = next(user['username']
                        for user in usernames if user['id'] == int(user_id))
        for todo in user_todos:
            todo['username'] = username

    output = json.dumps(todos_by_user)

    with open('todo_all_employees.json', 'w') as file:
        file.write(output)
