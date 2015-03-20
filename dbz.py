import shutil
import requests

url = 'http://s1.mp4vids.tv/videos/afnauihj2anvfuu/video.mp4'
url2 = 'http://s1.mp4vids.tv/videos/fr2o6jro2b1oekb/video.mp4'

response = requests.get(url, stream=True)
response2 = requests.get(url2, stream=True)
with open('e15.mp4', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
with open('e16.mp4', 'wb') as out_file:
    shutil.copyfileobj(response2.raw, out_file)

del response
del response2
print("All Done! \n")
