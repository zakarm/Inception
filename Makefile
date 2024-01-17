DC = docker-compose
DC_FILE = ./srcs/docker-compose.yml

all: build up

build :
	$(DC) -f $(DC_FILE) build

up :
	$(DC) -f $(DC_FILE) up

down :
	$(DC) -f $(DC_FILE) down -v

clean: down
	@if [ -n "$$(docker ps -qa)" ]; then docker rm -f $$(docker ps -qa); fi
	@if [ -n "$$(docker images -q)" ]; then docker rmi -f $$(docker images -q); fi

fclean: clean
	@rm -rf /Users/$(shell whoami)/data/mariadb/*
	@rm -rf /Users/$(shell whoami)/data/wordpress/*
	@rm -rf /Users/$(shell whoami)/data/portainer/*
	@docker system prune -af
	@docker volume prune --all -af

re : fclean all

.PHONY: all build up down clean re