import requests
import hashlib

url="http://docker.hackthebox.eu:42767/"

r=requests.session()
out=r.get(url).text
sMarker = "<h3 align='center'>"
sEnd = "</h3><center>"
hashStart = out.find(sMarker) + len(sMarker)
theHash = (out[hashStart:out.find(sEnd)])

theHash=hashlib.md5(theHash.encode('utf-8')).hexdigest()

data={'hash': theHash}
out = r.post(url = url, data = data)

print(out.text)