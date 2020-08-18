import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
s = 0
uh = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_421754.xml', context = ctx)
data = uh.read()
tree = ET.fromstring(data)
lst = tree.findall('.//count')
for i in lst:
    x = i.text
    s = s+int (x)
print (s)    
