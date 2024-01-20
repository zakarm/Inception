DC 		= docker-compose
DC_YML	= ./srcs/docker-compose.yml
PROJECT = inception

all: up

up :
	$(DC) -f $(DC_YML) --project-name $(PROJECT) up --build

start : 
	$(DC) -f $(DC_YML) --project-name $(PROJECT) start

stop :
	$(DC) -f $(DC_YML) --project-name $(PROJECT) stop

down : stop
	$(DC) -f $(DC_YML) --project-name $(PROJECT) down --rmi all --volumes --remove-orphans

status :
	docker ps

prune : down
	docker system prune -af

network :
	docker network inspect inception

.PHONY: all build up stop down clean re
