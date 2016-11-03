import time
import random
import datetime
import telepot
import urllib2
from bs4 import BeautifulSoup

"""
@iamakidilam
REPLACE THE TOKEN
"""

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/score':
        page = urllib2.urlopen("http://www.espncricinfo.com/australia-v-south-africa-2016-17/engine/match/1000851.html")
 
        soup = BeautifulSoup(page)
        links =soup.findAll("title")
        
        
        bot.sendMessage(chat_id,str(links))
        

bot = telepot.Bot('288498765:AAGrrFWjOf3GOMGqbFXLU4I3fzFoFYElDO0')
bot.message_loop(handle)
print 'I am listening ...'



while 1:
    time.sleep(10)
    
