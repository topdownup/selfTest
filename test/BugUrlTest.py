# coding=utf-8
import urllib2

url = "http://bugz.iwangzhi.com/show_bug.cgi?id=%d"
for i in range(11096, 11097):
    response = urllib2.urlopen(url % (i))
    print i, response.code
    response.close()
