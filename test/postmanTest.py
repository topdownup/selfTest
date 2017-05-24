import requests

url = "http://www.wangzhi.com/"

headers = {
    'cache-control': "no-cache",
    'postman-token': "f0213c2e-5117-df65-6670-8705e622a398"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)