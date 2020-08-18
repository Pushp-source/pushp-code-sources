import urllib.request, urllib.parse, urllib.error
import json

address = input ('enter address-')
url = urllib.parse.urlencode({'address':address})
print (url)
