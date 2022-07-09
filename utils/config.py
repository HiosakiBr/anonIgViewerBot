# neste arquivo está sendo definindo variaveis que serão usadas pelo programa

# para gerar um cookie de sessão rode o codigo "cookies.py"
# um arquivo com nome "cookies.txt" será criado, cole tudo no arquivo dentro dessa variavel.

SESSION_COOKIE = 

# chave de acesso do seu bot do telegram, lembre-se o token é uma string.

TELEGRAM_API_TOKEN = 

# link que da acesso a stories do instagram

instagram_path_url_stories = 'https://instagram.com/stories/'

# jacascripts que serão usados no codigo

SCRIPTS = {'photo':[open('utils/js/photo.js' , 'r').read()],'video':[open('utils/js/video.js' , 'r').read()]}

# confurando variaveis para o google chrome que serão usadas no deploy

CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'