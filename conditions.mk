# Conditions for Makefile

.PHONY: req-venv
# checks if virtual environment is activated and exits if it isn't 
req-venv:
ifeq (${INVENV}, "")
	$(error Virtual environment not activated)
endif
