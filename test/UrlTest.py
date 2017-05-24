import urllib2
import urllib
import cookielib

values = {"name": "wowo", "age": "20"}
data = urllib.urlencode(values)

headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}

cookie = cookielib.MozillaCookieJar()
headler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(headler)
request = urllib2.Request("http://www.wangzhi.com", data, headers)
response = opener.open(request)
print response.read()
print cookie
for item in cookie:
    print "-"*10
    print item.name
    print item.value

cookie.save("d:\\app.txt",True,True)

response.close()
