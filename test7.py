import requests
import webbrowser
# param = {"wd": "莫烦Python"}  # 搜索的信息
# r = requests.get('http://www.baidu.com/s', params=param)
# print(r.url)
#webbrowser.open(r.url)
data = {'firstname': '莫烦', 'lastname': '周'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36','referer': 'http://jwurp.hhuc.edu.cn/' }
#r = requests.get('https://zhuanlan.zhihu.com/python-programming', headers = headers)
data={'zjh':'1562810212','mm':'urpscode','v_yzm':'99t8'}
r = requests.post('http://jwurp.hhuc.edu.cn/loginAction.do', data=data,headers=headers)
print(r.text)
