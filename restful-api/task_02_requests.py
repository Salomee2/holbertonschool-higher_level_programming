import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        print("Status Code: 200")
        posts = response.json()

        for post in posts:
            print(post['title'])
    else:
        print(f"Erreur : {response.status_code}")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        with open("posts.csv", mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
        print("Les posts ont été sauvegardés dans 'posts.csv'.")
    else:
        print(f"Erreur : {response.status_code}")


fetch_and_print_posts()
fetch_and_save_posts()
