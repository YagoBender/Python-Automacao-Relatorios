import requests

def get_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()
