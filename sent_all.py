#coding=utf8
import itchat, time

itchat.auto_login()

SINCERE_WISH = u'祝%s新年快乐！'

def getRandomGreeting():
  response = requests.get("http://www.xjihe.com/api/life/greetings?festival=新年&page=10", headers = {'apiKey':'sQS2ylErlfm9Ao2oNPqw6TqMYbJjbs4g'})
  results = response.json()['result']
  greeting = results[random.randrange(len(results))]['words']
  return greeting


friendList = itchat.get_friends(update=True)[1:]

count = 0
for friend in friendList:
    itchat.send( SINCERE_WISH % (friend['DisplayName']
         or friend['NickName']), friend['UserName'])
    time.sleep(1)
print("----end----")
