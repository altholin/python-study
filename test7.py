import requests
import webbrowser
# param = {"wd": "莫烦Python"}  # 搜索的信息
# r = requests.get('http://www.baidu.com/s', params=param)
# print(r.url)
#webbrowser.open(r.url)
data = {'firstname': '莫烦', 'lastname': '周'}
r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
print(r.text)
# data={'zjh':'1562810212','mm':'urpscode','v_yzm':'mx9x'}
# r = requests.post('http://jwurp.hhuc.edu.cn/loginAction.do', data=data)
# print(r.text)
