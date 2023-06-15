from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer('chatbot')

#ex:trainer.train("C:\Users\user\Desktop") edit the path as the given example once the coustomized ai.yml file is placed in a path.
trainer.train("chatterbot.corpus.english") 
                                            


print("Hi, i am ChatBot")
while True:
    query = input('You : ')
    print(chatbot.get_response(Statement(text=query, search_text=query)))
