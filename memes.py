import urllib
import json
import requests
count=1
req=requests.get("http://meme-api.herokuapp.com/gimme")
json_data = json.loads(req.text)
imgs="memes-"+str(count)+".jpg"
print(imgs)
urllib.urlretrieve(json_data["url"],imgs)
print(imgs + "is saved")