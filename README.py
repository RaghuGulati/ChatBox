# ChatBox
from chatterbot.trainers import ListTrainer
from chatterbot import *

bot = ChatBot('Test')

conv = open('chats.txt','r').readlines()

bot.set_trainer(ListTrainer)

bot.train(conv)
i=0
while True:
    request = input('You: ')
    response = bot.get_response(request)
    
    if(conv[i]=="Q"):
        print("Sorry Ans entered")
    else:
        print('Bot: ',response)
   
    i=i+1
