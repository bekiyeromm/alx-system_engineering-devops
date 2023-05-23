#!/usr/bin/python3

"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format
"""

if __name__ == '__main__':
    import requests
    import csv
    from sys import argv

    user_addres = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                               format(argv[1]))
    name = user_addres.json().get('username')

    tod = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))
    request_data = tod.json()

    with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in request_data:
            csv_writer.writerow([argv[1], name, task.get('completed'),
                                 task.get('title')])
