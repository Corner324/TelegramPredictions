install:
	poetry install


env:



test: env


start: test
	poetry run python3 ./main_bot.py -d


.PHONY: test env