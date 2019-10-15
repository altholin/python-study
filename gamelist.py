from urllib.request import urlopen
# if has Chinese, apply decode()

html = urlopen(
    "https://lpl.qq.com/"
).read().decode('utf-8',"ignore")

# print(html)
import re
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])
res = re.findall(r"<p>(.gamelist-item-topbar wait?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])
# res = re.findall(r'href="(.*?)"', html)
# print("\nAll links: ", res)