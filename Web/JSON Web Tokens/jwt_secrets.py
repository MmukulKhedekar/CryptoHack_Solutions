import jwt 
import requests

x = jwt.encode({"username":"admin", "admin":True},"secret",algorithm="HS256")
url = "https://web.cryptohack.org/jwt-secrets/authorise/" + x +"/"
print(requests.get(url).text)

## crypto{jwt_secret_keys_must_be_protected}