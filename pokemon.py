import requests

response = requests.get("https://api.thedogapi.com/v1/breeds")
response.headers.get("Content-Type")
print(response.json())
#print(response.json()['name']) por que esto devuelve una lista y no un dict
print(requests.get("https://randomuser.me/api/?gender=female").json())
print(requests.get("https://pokeapi.co/api/v2/ability/3/").json())

query_params = {"q": "German Shepherd"}
endpoint = "https://api.thedogapi.com/v1/breeds/search"
print(requests.get(endpoint, params=query_params).json())