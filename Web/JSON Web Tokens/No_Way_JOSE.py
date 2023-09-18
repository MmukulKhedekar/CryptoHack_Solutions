import jwt 
import requests
import base64

url_auth = "https://web.cryptohack.org/no-way-jose/authorise/"
url_ses = "https://web.cryptohack.org/no-way-jose/create_session/"

def create_sessions(s):
    url_new = url_ses + str(s) +"/"
    x = eval(requests.get(url_new).text)["session"]
    print(x)
    print(jwt.decode(x,algorithms="HS256",options={"verify_signature":False}))
    return eval(requests.get(url_new).text)["session"]

x = jwt.encode({"username": "admin", "admin": True},'',algorithm='none')

data = requests.get(f"{url_auth}{x}/").text
print(data)

# tamper_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
# plain_token = eval(base64.b64decode(tamper_token).decode('ascii'))
# plain_token = "{\"typ\": \"JWT\", \"alg\": \"none\"}"
# enc_token = base64.b64encode(str(plain_token).encode('ascii')).decode().strip('=')
# print(enc_token)

## crypto{The_Cryptographic_Doom_Principle}
