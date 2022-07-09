//este arquivo não e usado pelo bot, este codigo pretende descobrir se o perfil e privado,
// existe no instagram ou se ele não postou stories na ultimas 24 horas.

erro = null

if (document.title == 'Página não encontrada • Instagram'){

	erro = 'não existe'
}

if (erro == null) { 

for (h of document.querySelectorAll('h2') ){

	if (h.textContent == 'Esta conta é privada'){erro = 'privado'}
}}

if (erro == null){

	erro = 'sem stories'
}


return erro