install:
	pip3 install -r requirements.txt


env:
	. ./BotEnv/bin/activate


test: env


start: test
	python3 ./main_bot.py -d


.PHONY: test env