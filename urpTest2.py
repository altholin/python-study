# coding:utf8

import re
import urllib
import http.cookiejar

loginUrl = 'http://jwurp.hhuc.edu.cn/loginAction.do'

#cookie
cookie = http.cookiejar.CookieJar() # 声明cookiejar的对象,存放cookie的容器
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

#postdata
values = {
    'zjh':'1562810212',
    'mm':'',
    'v_yzm':''
}
postdata = urllib.parse.urlencode(values)
#headers
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer':'http://jwurp.hhuc.edu.cn/loginAction.do'
}

#第一次请求网页得到cookie
request = urllib.request.Request(loginUrl,postdata,headers=header)
response = opener.open(request)
print ('第一次请求网页得到cookie:')
print (response.getcode())

#获取验证码----------------!!!问题一直出在这，要用带cookie的方法访问验证码的网页---这样的话进入的验证码的页面对应的验证码就是登陆页面的验证码了哈哈哈哈哈(之前用的是不带cookie的urlopen()方法...)
# yzm = opener.open('http://115.24.160.162/validateCodeAction.do')
# yzm_data =  yzm.read()
# yzm_pic = file('yzm.jpg','wb')
# yzm_pic.write(yzm_data)
# yzm_pic.close()
#
# #用户输入验证码
# print '请输入验证码：'
# values['v_yzm'] = raw_input()
# #带验证码模拟登陆
# postdata = urllib.urlencode(values)
# request = urllib2.Request(loginUrl,postdata,header)
# response = opener.open(request)
# print 'Response of loginAction.do'
# print response.read().decode('gbk')