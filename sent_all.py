#coding=utf8
import itchat, time,requests,random

itchat.auto_login(hotReload=True)

SINCERE_WISH = u'新年快乐！'

def getRandomGreeting():
  response = requests.get("http://www.xjihe.com/api/life/greetings?festival=新年&page=10", headers = {'apiKey':'sQS2ylErlfm9Ao2oNPqw6TqMYbJjbs4g'})
  results = response.json()['result']
  greeting = results[random.randrange(len(results))]['words']
  return greeting


friendList = itchat.get_friends(update=True)[1:]

print(len(friendList))

count = 0
for friend in friendList:
	regreting = SINCERE_WISH + getRandomGreeting() + "--by ***your name***'s wechat robot. \nPS:心意在我的程序里，嘿嘿嘿"
	regreting = "亲爱的%s: " % (friend['RemarkName'] or friend['NickName']) + regreting
	itchat.send(regreting,friend["UserName"])
	time.sleep(5)


print("----end----")
