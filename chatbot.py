from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer('chatbot')

trainer.train("chatterbot.corpus.english")+
+


print("Hi, i am ChatBot")
while True:
    query = input('You : ')
    print(chatbot.get_response(Statement(text=query, search_text=query)))
