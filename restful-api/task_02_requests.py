import requests
import csv


"""fetch posts"""


def fetch_and_print_posts():
    """fetch and print posts"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    code = response.status_code
    print(f"Status Code: {code}")
    if code == 200:
        json_ob = response.json()
        for item in json_ob:
            print(item['title'])


def fetch_and_save_posts():
    """fetch and register posts"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    code = response.status_code

    if code == 200:
        json_ob = response.json()
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'],
                                    extrasaction="ignore")
            writer.writeheader()
            writer.writerows(json_ob)
