# extract links to images in a web's html
import re
import requests

r = requests.get('https://www.history.com/topics/european-history/joseph-stalin')

image_regex = re.compile(r'(https://[\w\d./-]*\.)(jpg|png|jpeg)', re.I)

link_list = image_regex.findall(r.text)

for i in set(link_list):
    print(i[0]+i[1])
