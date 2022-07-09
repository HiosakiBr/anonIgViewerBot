resposta = 'None'

try{

resposta = document.querySelector('video').querySelector('source').src

}

catch(e){

	resposta =  document.querySelector('video').src
}

return resposta