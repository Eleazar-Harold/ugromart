verbosity=15
language='en-gb'
compose:=docker-compose -f

help:
	@echo "Usage:"
	@echo " make help			-- display this help"
	@echo " make stack			-- installs and sets up development application"
	@echo " make tearstack			-- destroys development setup, together with development volumes"

env:
	cp .env.example .env

buildstack:
	$(compose) stack.yml build

downstack:
	$(compose) stack.yml down

propagatestack:
	$(compose) stack.yml up

stack: env
stack: buildstack
stack: downstack
stack: propagatestack

tearstack:
	$(compose) stack.yml down -v --rmi local --remove-orphans


