import jwt 
import json 
import requests

url_create = "https://web.cryptohack.org/json-in-json/create_session/"
url_auth = "https://web.cryptohack.org/json-in-json/authorise/"

s = 'mmukul", "admin": "True'
print(s)
body = '{' \
              + '"admin": "' + "False" \
              + '", "username": "' + str(s) \
              + '"}'
# print(body)
# print(json.loads(body))
session = eval(requests.get(f"{url_create}{s}/").text)["session"]
print(eval(requests.get(f"{url_auth}{session}/").text)["response"])
