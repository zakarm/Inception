DC 		= docker-compose
DC_YML	= ./srcs/docker-compose.yml
PROJECT = inception

all: up

dir:
	@mkdir -p /Users/$(USER)/data
	@mkdir -p /Users/$(USER)/data/portainer
	@mkdir -p /Users/$(USER)/data/wordpress
	@mkdir -p /Users/$(USER)/data/mariadb

remove:
	@rm -rf /Users/$(USER)/data
	@rm -rf /Users/$(USER)/data/portainer
	@rm -rf /Users/$(USER)/data/wordpress
	@rm -rf /Users/$(USER)/data/mariadb


up: dir
	$(DC) -f $(DC_YML) --project-name $(PROJECT) up --build

start: 
	$(DC) -f $(DC_YML) --project-name $(PROJECT) start

stop: 
	$(DC) -f $(DC_YML) --project-name $(PROJECT) stop

down: stop remove
	$(DC) -f $(DC_YML) --project-name $(PROJECT) down --rmi all --volumes --remove-orphans

status:
	docker ps

prune: down
	docker system prune -af

network:
	docker network inspect inception

.PHONY: all build up stop down clean re
