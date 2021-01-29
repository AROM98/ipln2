#a 2º linha do install, é para o programa 'poetry'
# em principio funciona em maquinas linux

install:
	sudo cpan Lingua::PT::PLN
	npm install -g poetry-parser
	pip3 install pathlib
	pip3 install requests
	pip3 install beautifulsoup4
	pip3 install ply 
	sudo apt-get install bison flex
