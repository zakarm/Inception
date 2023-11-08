fclean:
	docker rm -f $(shell docker ps -qa)
	docker rmi -f $(shell docker images -q)`