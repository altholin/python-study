from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json;
##调用接口
url = "https://apps.game.qq.com/lol/match/apis/searchBMatchInfo.php?p1=128&p5=19&pagesize=60&r1=BMatchList&v=53&_=1571108021660"
# headers = {'content-type': 'application/json'}
# requestData = {"name": "lance", "age": "28"}
ret = requests.get(url)
# if ret.status_code == 200:
#     print(ret.text)
str = ret.text;
# str[6:]
matchJson = json.loads(str[16:])
#print(matchJson)
match = matchJson['msg']['result']
for matchDetial in match:
    print(matchDetial['GameTypeName'])
    print(matchDetial['bMatchName'])
    print(matchDetial['MatchDate'])
#print(match)
#['bMatchName']['MatchDate']
# if has Chinese, apply decode()
# html = urlopen("https://lpl.qq.com/").read().decode('utf-8',"ignore")
# print(html)
# soup = BeautifulSoup(html, features='lxml')
# jan = soup.find('ul', {"id": 'matchlist'})
# d_jan = jan.find_all('li')              # use jan as a parent
# for d in d_jan:
#     print(d.get_text())
# # use class to narrow search
# # match = soup.find_all('li', {"class": "gamelist-item"})
# # for m in match:
# #     print(m.get_text())
# match = soup.find('p', {"class": "gamelist-item-topbar wait"})
# team = match.find_all('span')
# for t in team:
#     print(t.get_text())
# # for m in match:
# #     print(m.get_text())
# # jan = soup.find('ul', {"class": 'jan'})
# # d_jan = jan.find_all('li')              # use jan as a parent
# # for d in d_jan:
# #     print(d.get_text())