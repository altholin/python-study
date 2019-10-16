#实战小项目：爬取教务网成绩并存入excel
import requests
import xlwt
from bs4 import BeautifulSoup

#模拟登录
formData={'zjh':'1562810212','mm':'','v_yzm':'nvax'}
s=requests.Session()
Post=s.post(url='http://jwurp.hhuc.edu.cn/loginAction.do',data=formData)
print (Post.status_code)
#获取基本信息
