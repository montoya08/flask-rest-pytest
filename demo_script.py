import requests

URL='http://127.0.0.1:5000/'

# First GET
response = requests.get(URL + "elements")
print("First GET:", response.text)

#POST
response = requests.post(URL + "elements", json={'element': 'one'})
print("Post 1:", response.json())

response = requests.post(URL + "elements", json={'element': 'two'})
print("Post 2:", response.json())

# Second GET
response = requests.get(URL + "elements")
print("Second GET:", response.json()) 

# PUT first element
response = requests.put(URL + "elements/0", json={'element': 'three'})
print("PUT first element:", response.json())

# DELETE second element
response = requests.delete(URL + "elements/1")
print("DELETE second element:", response.json())

# Last GET
response = requests.get(URL + "elements")
print("Last GET:", response.json())

