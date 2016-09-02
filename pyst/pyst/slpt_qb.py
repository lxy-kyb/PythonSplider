import urllib
import urllib2
import re
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

file = open("print.txt",'w+');

page = 1

url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {"User-Agent" : user_agent}

try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    #print response.read()
    content = response.read()
    pattern = re.compile('<div class="author.*?>.*?<a.*? alt="(.*?)".*?</a>.*?<div.*?content">(.*?)</div>', re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item[0].decode()
        print item[1].decode()
        file.writelines(item[0] + '\n')
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
