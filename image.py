import urllib.request, urllib.error, urllib.parse
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open ('cover3.jpg' , 'wb')
print (fhand.write(img))
fhand.close()              
