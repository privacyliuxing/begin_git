import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.xiachufang.com/")
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')

img_list = []

for img in soup.select("img"):
    if img.has_attr("data-src"):
        img_list.append(img.attrs['data-src'])
    else:
        img_list.append(img.attrs['src'])
print(img_list)
image_dir = os.path.join(os.curdir, "images")
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)
print(image_dir)
print(os.curdir)
for img in img_list:
    o = urlparse(img)
    file_name = o.path[1:].split("@")[0]
    filepath = os.path.join(image_dir,o.path)
    url = '%s://%s/%s' % (o.scheme, o.netloc, file_name)
    print(url)
    print(file_name)
    print(img)
    try:
        resp = requests.get(url)
    except:
        continue
    if not filepath.endswith('.svg'):
        with open(filepath, 'wb') as f:
            for chunk in resp.iter_content(1024):
                f.write(chunk)
