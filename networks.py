import requests

data = {
   'name': 'John Doe',
    'age': 20
}

response = requests.post (
    "https://jsonplaceholder.typiccode.com/posts" data = data)


print (response.content)