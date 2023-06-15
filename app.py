from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
#ex:trainer.train("C:\Users\user\Desktop") edit the path as the given example once the coustomized ai.yml file is placed in a path.
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(chatbot.get_response(userText))


if __name__ == "--main__":
    app.run()
