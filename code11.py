import urllib.request
f =  urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for a in f:
  print(a.decode().strip())
