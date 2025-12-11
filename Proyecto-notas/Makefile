PYTHON=python3
VENV=.venv
PIP=$(VENV)/bin/pip
PYTEST=$(VENV)/bin/pytest

.PHONY: venv install-dev install-editable test docs clean

venv:
	$(PYTHON) -m venv $(VENV)

install-dev: venv
	$(PIP) install -r requeriments.txt
	$(PIP) install -e .

install-editable:
	pip install -e .

test:
	@if [ -x $(PYTEST) ]; then \
		$(PYTEST) -q; \
	else \
		./scripts/run-tests.sh; \
	fi

docs:
	mkdocs serve

clean:
	rm -rf $(VENV) .pytest_cache __pycache__ build dist *.egg-info
