PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

.PHONY: setup check run

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

check:
	$(PY) -m compileall -q .
	$(PY) -c "import axeon_linear; print(axeon_linear.sync_issue('ABC-1','in_progress')['synced'])"

run:
	$(PY) axeon_web/adapter.py
