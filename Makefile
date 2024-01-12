DC = docker-compose
DC_FILE = ./srcs/docker-compose.yml

all: build up

build :
	$(DC) -f $(DC_FILE) build

up :
	$(DC) -f $(DC_FILE) up

down :
	$(DC) -f $(DC_FILE) down

clean: down
	@if [ -n "$$(docker ps -qa)" ]; then docker rm -f $$(docker ps -qa); fi
	@if [ -n "$$(docker images -q)" ]; then docker rmi -f $$(docker images -q); fi

fclean: clean
	@docker system prune -af --volumes

re : fclean all

.PHONY: all build up down clean re