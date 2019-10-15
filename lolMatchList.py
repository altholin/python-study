import requests
import json;
##调用接口
url = "https://apps.game.qq.com/lol/match/apis/searchBMatchInfo.php?p1=128&p5=19&pagesize=60&r1=BMatchList&v=53&_=1571108021660"
ret = requests.get(url)
str = ret.text;
matchJson = json.loads(str[16:])
#print(matchJson)
match = matchJson['msg']['result']
for matchDetial in match:
    print(matchDetial['GameTypeName'])
    print(matchDetial['bMatchName'])
    print(matchDetial['MatchDate'])