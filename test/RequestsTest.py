# coding = UTF-8
import requests

url = "http://bugz.iwangzhi.com/show_bug.cgi?id=%d"
# jar = requests.cookies.RequestsCookieJar()
# jar.set()
data = {"name": "selfname", "age": 1}
re = requests.post(url % (10000), data)
cookies = re.cookies
for item in cookies:
    print "-"*10
    print item.name
    print item.value
print re.status_code
