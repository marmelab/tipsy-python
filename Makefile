
DOCKER := docker run -it --rm tipsy-python

install: ## Build the docker container
	docker build -t tipsy-python .

run: ## Run the game.
	$(DOCKER) python3 ./tipsy.py

test: ## Run the tests
	$(DOCKER) python3 -m unittest -v

local-test: ## Run the tests on local machine
	python3 -m unittest discover -s ./src -v

local-run:
	python3 ./src/tipsy.py
