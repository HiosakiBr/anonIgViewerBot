from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
from utils.config import *

class Browser:
	""" gerenciar o chorme driver para uso local e para uso no deploy"""
	
	def local():

		# configuração do webdriver

		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		options.add_argument('--log-level=3')
		options.add_argument('--disable-gpu')
		options.add_argument('--disable-logging')
		options.add_argument('--dev-shm-usage')
		options.add_argument('disable-dev-shm-usage')
		options.add_argument("--no-sandbox")
		options.add_experimental_option('excludeSwitches', ['enable-logging'])

		# iniciar e retornar o webdriver

		driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
		return driver


	def deploy():

		options = webdriver.ChromeOptions()
		options.binary_location = GOOGLE_CHROME_BIN
		options.add_argument('--headless')
		options.add_argument('--log-level=3')
		options.add_argument('--disable-gpu')
		options.add_argument('--disable-logging')
		options.add_argument('--dev-shm-usage')
		options.add_argument('disable-dev-shm-usage')
		options.add_argument("--no-sandbox")
		options.add_experimental_option('excludeSwitches', ['enable-logging'])
		driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
		return driver