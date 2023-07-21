import requests
import bs4
import csv
import pandas as pd
import urllib.request
from PIL import Image



base_url="https://xkcd.com/"

result = requests.get(base_url)
soup = bs4.BeautifulSoup(result.text,"lxml")
numb = soup.select('a')
numbe = numb[27].getText()
present_num = numbe[17:21]
print(f'The total number of comic strips present in the website currently is: {present_num}')

i = int(present_num)

while(i):
        print(f'processing {i}')
        result = requests.get(base_url.format(i))
        soup = bs4.BeautifulSoup(result.text,"lxml")
        tit = soup.select('title')
        if(((tit[0].getText())=='404 Not Found')):
            quit()
        else:
            title = soup.find_all('img')
            count = 0
            for each in title:
                count = count+1
                if(count==3):
                    img_link = each['src']
                    img_name = each['alt']

                    img_name = ''.join(filter(str.isalnum, img_name)) 

                    urllib.request.urlretrieve(f'https:{img_link}', f'{img_name}.jpg')
                    pic = Image.open(f'{img_name}.jpg')
                else:
                    continue
        i=i-1          
