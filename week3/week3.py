import urllib.request
import json


# 定義目標網頁的 URL
url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'

name = []
local = []
lon = []
lat = []
jpg = []

try:
    # 發送 GET 請求並獲取響應
    response = urllib.request.urlopen(url)

    # 讀取響應的內容
    html = response.read()

    # 將內容轉換為字串格式並輸出
    data = html.decode()
    
    data_dict = json.loads(data)
    
    all_info = data_dict['result']['results']
    
    for i in all_info :
        name.append(i['stitle'])
        local.append(i['address'][5:8])
        lon.append(i['longitude'])
        lat.append(i['latitude'])
        jpg.append(i['file'].split('jpg')[0] + 'jpg')
    
    
except Exception as e:
    print(e)

with open('attraction.csv','w',encoding='utf-8') as f :
    for i in range(len(name)) :
        word = f"{name[i]},{local[i]},{lon[i]},{lat[i]},{jpg[i]}\n"
        f.write(word)


import urllib.request
import json


# 定義目標網頁的 URL
url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'

mrt = []
name = []

try:
    # 發送 GET 請求並獲取響應
    response = urllib.request.urlopen(url)

    # 讀取響應的內容
    html = response.read()

    # 將內容轉換為字串格式並輸出
    data = html.decode()
    
    data_dict = json.loads(data)
    
    all_info = data_dict['result']['results']
    
    for i in all_info :
        mrt.append(i['MRT'])
        name.append(i['stitle'])

    info = {}
    for i in range(len(mrt)) :
        if mrt[i] in info :
            info[mrt[i]].append(name[i])
        else :
            info[mrt[i]] = [name[i]]

except Exception as e:
    print(e)
    
with open('mrt.csv','w',encoding='utf-8') as f :
    for i,j in info.items() :
        word = f"{i},"
        for k in j :
            word += k
            word += ','
        word += '\n'
        f.write(word)


import requests
from bs4 import BeautifulSoup


def get_info(url,whole) :
    try :
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for i in soup.select('div.title a') :
            whole['title'].append(i.text)
            
        for i in soup.select('div.r-ent div.nrec') :
            whole['num'].append(i.text)
            
        for i in soup.select('div.r-ent div.title a') :
            html = i.get('href')
            whole_html = 'https://www.ptt.cc/'
            whole_html += str(html)
            response_html = requests.get(whole_html)    
            soup_html = BeautifulSoup(response_html.content, 'html.parser')
            whole['time'].append(soup_html.select('div.article-metaline span.article-meta-value')[2].text)

    except Exception as e :
        print(e)
    return whole

url = 'https://www.ptt.cc/bbs/movie/index.html'
whole = {'title':[],'num':[],'time':[]}

get_info(url,whole)
for i in range(2) :
    url = f"https://www.ptt.cc/bbs/movie/index{9606-i}.html"
    get_info(url,whole)
    
print(whole)

with open('movie.txt','w',encoding='utf-8') as f :
    for i in range(len(whole['title'])) :
        word = f"{whole['title'][i]},{whole['num'][i]},{whole['time'][i]}\n"
        print(word)
        f.write(word)