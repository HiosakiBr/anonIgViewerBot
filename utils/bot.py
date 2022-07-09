import telebot
from utils.instagram import Instagram
from utils.config import *

class Bot:

	""" gerenciar as consultas para stories feitas pelo telegram."""

	def __init__(self):

		self.bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

		def start(self):

			try:

				print('\n[INFO] iniciado com sucesso, aguardando solicitações...')

				self.bot.polling()

			except Exception as erro_a_iniciar:

				print(f'[INFO] não foi possivel iniciar o bot, stack trace :\n [{erro_a_iniciar}]')

		@self.bot.message_handler(commands=['start'])

		def start_msg(message):

			self.bot.send_message(message.chat.id ,"Hello, choose from the menu what you want to do!")

		@self.bot.message_handler(commands=['help'])

		def support(message):

			self.bot.send_message(message.chat.id , 'If you are having problems with our service or want to block your profile for consultation, please contact the developer by email:\nanonigviewerSupport@proton.me')

		@self.bot.message_handler(content_types=['text'])

		def send_stories(message):

			if message.text == '/stories':

				self.bot.send_message(message.chat.id , "Please submit username to get stories, example: /stories @user_name_here or send the profile link.")

			else:


				if '/stories' in message.text and len(message.text.split()) > 1 :
					
					usuario = Instagram().ParserUser(message.text.split()[1])


				else:

					usuario = Instagram().ParserUser(message.text)

				print(f'\n[+] nova consulta para : {usuario}')
				self.bot.send_message(message.chat.id , f'collecting stories from {usuario}, wait...')
				result = Instagram().stories(usuario)

				if type(result) == list:

					for storie in result:

						try:

							if storie['tipo'] == 'photo':

								self.bot.send_photo(message.chat.id , photo=storie['link'], caption=f"photo posted to {storie['date']} ago")

							else:

								self.bot.send_video(message.chat.id, video=storie['link'], caption=f"video posted to {storie['date']} ago", supports_streaming=True)

						except:

							self.bot.send_message(message.chat.id, 'error sending a file, please try to request again 🤕')
							


				elif result == 'desconhecido':

					self.bot.send_message(message.chat.id, 'An unknown error occurred during execution. report sent to developer.')

				else:

					self.bot.send_message(message.chat.id, "⚠️ error, check if the profile:\n\n- it's private\n\n- posted in the last 24 hours\n\n- there is no Instagram.")


		start(self)