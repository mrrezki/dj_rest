import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Hellow world"})

print(get_response.text)
get_response = requests.get(endpoint)
print(get_response.json())
print(get_response.status_code)
