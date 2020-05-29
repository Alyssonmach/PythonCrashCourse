# Guia de Instalação do Python na Máquina

a) Baixamos e instalamos o Python 3.7;

b) Baixamos e instalamos o PyCharm;

c) Instalamos com o pip (gerenciador de pacotes Python) as bibliotecas:
	pip install virtualenv
	pip install virtualenvwrapper-win

d) Adicionamos uma variável de ambiente no PATH do sistema:
	WORKON_HOME %USERPROFILE%\Envs


e) Criamos um ambiente virtual para começarmos os estudos:
	mkvirtualenv ppe 

f) Para fazer acesso ao ambiente virtual:
	workon ppe

OBS: ppe é o nome do ambiente virtual criado.


g) Para sair do ambiente virtual:
	
	deactivate

