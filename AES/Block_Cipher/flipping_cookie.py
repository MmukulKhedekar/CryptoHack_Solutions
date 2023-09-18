import requests

url_cookie = "https://aes.cryptohack.org/flipping_cookie/get_cookie/"
url_check  = "https://aes.cryptohack.org/flipping_cookie/check_admin/"

def get_cookie():
    data = requests.get(url_cookie).text
    return eval(data)["cookie"]
