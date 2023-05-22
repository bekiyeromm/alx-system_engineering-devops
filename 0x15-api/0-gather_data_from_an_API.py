#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    user_address = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                .format(argv[1]))
    name = user_address.json().get('name')
    tod = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       .format(argv[1]))
    request_data = tod.json()
    done = total = 0
    for task in request_data:
        total += 1
        if task.get('completed'):
            done += 1

    print('Employee {} is done with tasks({}/{}):'.format(name, done, total))
    for task in request_data:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
