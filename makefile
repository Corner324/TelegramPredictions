install:
	pip install -r requirements.txt


test: 
	echo 'Running testing module...'


start: test
	source ./BotEnv/bin/activate
	echo 'Virtual environment activated'
	echo 'Bot starting...
	python3 ./main_bot.py -d


.PHONY: test