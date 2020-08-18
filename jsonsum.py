import urllib.request, urllib.parse, urllib.error
import json
import ssl
S = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
uh = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_421755.json', context = ctx)
data = uh.read()
info = json.loads(data)
#print(info['comments'][0]['count'])
x = info['comments']
print (len(x))
for i in range(50):
    y = info['comments'][i]['count']
    S = S+y
print (S)    
