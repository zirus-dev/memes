import requests
import subprocess
import urllib.request
import json
count=1
while 1 == 1:
	try:
		req=requests.get("http://meme-api.herokuapp.com/gimme")
		json_data = json.loads(req.text)
		imgs="meme-"+str(count)+".jpg"
		imgt="meme-"+str(count)+".txt"
		urllib.request.urlretrieve(json_data["url"],imgs)
		count=count+1
		print(imgs + " is saved")
		filess=open(imgt,"w")
		filess.write(req.text)
		filess.close()
		print(imgt +" is saved")
	except:
		pass