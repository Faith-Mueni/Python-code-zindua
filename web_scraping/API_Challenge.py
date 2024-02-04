#Using what we've learnt about APIs and sending HTTP requests. Write a python program that makes POST, GET, and UPDATE requests to the jsonplaceholder api.



import requests

data = {'gender': "Female",
"age": 15
}
response = requests.post("https://jsonplaceholder.typicode.com/post", data=data)

print (response.content)






