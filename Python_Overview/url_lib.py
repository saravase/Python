import urllib.request
import urllib.parse
url='http://pythonprogramming.net'
values={
    's':'basic',
    'submit':'search'
    }
data=urllib.parse.urlencode(values)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
resp=urllib.request.urlopen(req)
respData=resp.read()
file=open('url.txt','w');
file.write(str(respData));
'''x=urllib.request.urlopen('https://www.google.com')
print(x.read())'''
