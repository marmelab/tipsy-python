
DOCKER := docker run -it --rm tipsy-python

install: ## Build the docker container
	docker build -t tipsy-python .

run: ## Run the game.
	$(DOCKER) python3 ./main.py

test: ## Run the tests
	## TODO