import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#url = input('Enter -')
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fintan.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup ('a')
x = tags[17].attrs['href']

for i in range(6):
     html1 =urllib.request.urlopen(x, context=ctx).read()     
     soup1 =BeautifulSoup(html1, 'html.parser')
     tag1 = soup1('a')     
     x = tag1[17].attrs['href']
     
print(x)
