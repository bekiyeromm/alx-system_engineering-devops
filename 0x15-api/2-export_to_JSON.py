#!/usr/bin/python3

"""
Using what you did in the task #0, extend your Python script
to export data in the JSON format
"""

if __name__ == '__main__':
    import requests
    import csv
    import json
    from sys import argv

    user_addres = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                               format(argv[1]))
    name = user_addres.json().get('username')

    tod = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))
    request_data = tod.json()
    j_file = {}
    j_file['{}'.format(argv[1])] = []
    for task in request_data:
        j_file['{}'.format(argv[1])].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': name
        })
    with open('{}.json'.format(argv[1]), 'w') as json_file:
        json.dump(j_file, json_file)
