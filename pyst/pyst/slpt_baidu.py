import urllib2
from bs4 import BeautifulSoup
import re
#response = urllib2.urlopen("http://www.baidu.com")
#print response.read()

#httpHandler = urllib2.HTTPHandler(debuglevel=1)
#httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
#opener = urllib2.build_opener(httpHandler, httpsHandler)
#urllib2.install_opener(opener)

#request = urllib2.Request("http://www.baidu.com")
#response = urllib2.urlopen(request)
#print response.read()

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, "lxml")

#for child in soup.descendants:
#    print child

print soup.find_all('a')

for tag in soup.find_all(re.compile("^b")):
    print(tag.name)