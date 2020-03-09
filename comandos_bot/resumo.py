import requests
import re
import Algorithmia
import os


#definição da api e algoritmo do Algorithmia
keyAlgorit = os.environ.get('ALGORITHMIAKEY', None)
client = Algorithmia.client(keyAlgorit)
algo = client.algo('nlp/Summarizer/0.1.3')


#função que resume a mensagem enviada
def resumo(update, context):
	 try:

        # pega o texto que o usuário mandou
         text = update.message.text

        # sumariza usando o Algorithmia
         summary = algo.pipe(text)

        # faz o bot enviar o resultado
         bot.sendMessage(chat_id=update.message.chat_id,text=summary.result)

    except UnicodeEncodeError:

        bot.sendMessage(chat_id=update.message.chat_id,text="I'm sorry Dave, I'm afraid I can't do that")