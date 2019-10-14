import requests
# payload = {'username': 'Morvan', 'password': 'password'}
# r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
# print(r.cookies.get_dict())
#
# # {'username': 'Morvan', 'loggedin': '1'}
#
#
# r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
# #r = requests.get('http://jwurp.hhuc.edu.cn/loginAction.do', cookies='JSESSIONID=dbak1Kw4TuP8naCGtvj3w')
# print(r.text)

# Hey Morvan! Looks like you're still logged into the site!
session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# {'username': 'Morvan', 'loggedin': '1'}


r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)