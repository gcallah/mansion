include common.mk

# Our directories
REQ_DIR = .
DASH_DIR = dashboard

FORCE:

prod: all_tests github

github: FORCE
	- git commit -a
	git push origin main

all_tests: FORCE
	cd $(DASH_DIR); make tests

dev_env: FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt
	@echo "You should set PYTHONPATH to: "
	@echo $(shell pwd)

prod_env: FORCE
	pip install -r $(REQ_DIR)/requirements.txt
