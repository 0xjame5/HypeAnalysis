# Makefile to ease trivial tasks for the project

include conditions.mk
VENV="$(shell find . -name ".*env")"
INVENV="$(shell which python | grep ${VENV})"
REQ="requirements.txt"


.PHONY: installenv
installenv:
	# install the virtual environment
	@test -d ${VENV} && virtualenv ${VENV} || virtualenv .venv


.PHONY: run
run: req-venv
	# run the Flask server
	@python hypeanalysis/run.py ${PORT}


.PHONY: init
init: req-venv
	# upgrade PIP on virtual environment
	@pip install -U pip && pip install -r ${REQ}


.PHONY: update
update: req-venv
	# update PIP requirements
	@pip freeze | grep -Eiv "pkg-resources" > ${REQ}


.PHONY: test
test: req-venv
	# run backend unit tests with nose
	@nosetests -v -w tests


.PHONY: clean
clean:
	# clean out cache and temporary files
	@find . \( -name "*.pyc" -type f -o -name "__pycache__" -type d \) -delete
