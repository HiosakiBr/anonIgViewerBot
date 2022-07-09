import re
import time
from utils.driver import Browser
from utils.config import *

class Instagram:

	def login(self,driver):

		driver.get('https://instagram.com/')

		for cookie in SESSION_COOKIE:

			driver.add_cookie(cookie)

	def ParserUser(self,user):

		""" pegar o nome de usuario pelo link do instagram e remover  @ se o usuario enviar """

		try:

			regex = "instagram.com/(.*)[/?].*"
			resp = re.search (regex, user)
			return resp.group(1).replace('@', '')

		except:

			return user.replace('@', '')


	def stories(self,user):

		""" coletar stories do instagram"""

		try:

			storie = []
			total_coletado = 0
			driver = Browser.deploy()
			self.login(driver)
			driver.get(instagram_path_url_stories + user + '/?hl=pt-br')
			time.sleep(6)
			driver.set_network_conditions(offline=True, latency=5 , download_throughput=500 * 1024, upload_throughput=500 * 1024) # desativar internet do navegador
			driver.execute_script('document.querySelector("button").click()')


			# verificar se tem stories para coletar, se passar nesse if coletar os stories.

			if driver.current_url != "https://www.instagram.com/?hl=pt-br" and driver.current_url != f'https://www.instagram.com/{user}/?hl=pt-br' and driver.current_url != 'https://www.instagram.com/?hl=pt-br' and driver.current_url != f'https://www.instagram.com/{user}/posts/' and driver.title != 'Página não encontrada • Instagram':

				while True:

					try:

						if driver.current_url == "https://www.instagram.com/?hl=pt-br": driver.execute_script("forçar um erro proposital no codigo.") # forçã um erro pra não pegar no feed
							
						
						photo = driver.execute_script(SCRIPTS['photo'][0])

						if photo == 'None':

							video = driver.execute_script(SCRIPTS['video'][0])
							storie.append({"link":video ,"date":driver.execute_script("return document.querySelector('time').textContent") ,"tipo":"video" })

						else:

							storie.append({"link":photo ,"date":driver.execute_script("return document.querySelector('time').textContent") ,"tipo":"photo" })

						driver.execute_script("""try {document.querySelector('[aria-label="Avançar"]').click()}catch { document.querySelectorAll('button')[4].click()} """)
						total_coletado += 1
						time.sleep(2)


					except: # fim do stories

						return storie


			else: # não tem stories, pedir para o usuario verificar as condições: se o perfil é privado,perfil não existe ou só não postou nas ultimas 24 horas.

				return 'erro'

		except Exception as erro_desconhecido:

			print(erro_desconhecido)
			return 'desconhecido'