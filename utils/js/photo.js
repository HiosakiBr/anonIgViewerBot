resposta = 'None'

try{

   if(document.querySelectorAll('video').length == 0){

      resposta = document.querySelector('img').src
	
      if(resposta == ''){resposta = 'None'}

   }

   else {resposta = 'None'}
}

catch (e){

   for (img of document.querySelectorAll('img') ){

         if (img.alt.search('Foto do perfil de') == -1){
         //resposta = document.querySelectorAll('img')[0].src
         resposta = img.src
         break;   
               }
   }


}

return resposta