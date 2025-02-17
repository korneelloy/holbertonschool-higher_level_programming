import requests
import json
import csv


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    code = response.status_code
    print(code)
    if code == 200:
        json_ob = response.json()

    for item in json_ob:
        print(item['title'])


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    code = response.status_code

    if code == 200:
        json_ob = response.json()

    list_dic = []

    for item in json_ob:
        dic = {
            'id': item['id'],
            'title': item['title'],
            'body': item['body']
        }
        list_dic.append(dic)

    with open('posts.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(list_dic)
