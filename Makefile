#!/usr/bin/make

help:
	@echo "make"
	@echo "	hello"
	@echo "		print hello world"
	@echo "	init-locale"
	@echo "		Initialize locale messages: make init-locale ARGS='ru'"
	@echo "	update-locale"
	@echo "		Initialize locale messages: make update-locale ARGS='ru'"

hello:
	echo "Hello, World"
extract-locale:
  pybabel extract -k __ --input-dirs=./aiogram_bot -o aiogram_bot/locales/messages.pot
init-locale:
	pybabel init -i ./aiogram_bot/locales/messages.pot -d ./aiogram_bot/locales -D messages -l $(ARGS)
update-locale:
	pybabel update -i aiogram_bot/locales/messages.pot -d aiogram_bot/locales -D messages -l $(ARGS)
compile-locale:
	pybabel compile -d ./aiogram_bot/locales -D messages