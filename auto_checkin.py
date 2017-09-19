import json
import urllib.request
opener = urllib.request.build_opener()
opener.addheaders.append(('Cookie', 
	'user_pwd=428cfb744dc4148e04c9e881ceba7206d99bdf950b587; uid=27; user_email=acoder1983%40163.com'))
f = opener.open("http://45.78.21.158/user/_checkin.php")
print(json.loads(f.read().decode('utf-8'))['msg'])
