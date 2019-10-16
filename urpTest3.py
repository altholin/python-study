# cookie:爬虫维持登陆状态的机制
import http.cookiejar,urllib.request
cookie = http.cookiejar.CookieJar() # 声明cookiejar的对象,存放cookie的容器
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.zhihu.com')
for item in cookie:
    print(item.name + '=' + item.value)
