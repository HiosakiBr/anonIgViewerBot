from utils.driver import Browser
from selenium.webdriver.common.by import By
import time

class Gerar():

	def terminal(user,pasword):

		driver = Browser.local()
		print('\n[INFO] navegador iniciado, fazendo login...')
		driver.get('https://instagram.com/')
		time.sleep(5)
		driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(user)
		driver.find_element(By.CSS_SELECTOR , '[name="password"]').send_keys(pasword)
		driver.find_element(By.CSS_SELECTOR , '[type="submit"]').click()
		print('\n[INFO] login realizado, aguardando 5 segundos para coletar cookies.')
		time.sleep(5)
		cookies = driver.get_cookies()
		open('cookies.txt', 'a').write(str(cookies))
		print('\n[INFO] cookies de sessão salvo em cookies.txt')
		print('\n[INFO] não foi verificado se o login teve sucesso,lembre-se de sempre informar a senha correta!')
		input('\n[+] pressione enter para fechar navegador agora')

		



usuario = input('\n[+] digite o usuario do instagram: ')
senha = input('\n[+] agora digite a senha do instagram: ')
Gerar.terminal(usuario , senha)