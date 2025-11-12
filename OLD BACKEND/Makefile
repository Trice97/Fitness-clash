# Makefile - Fitness Clash Backend
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Formatage
format:
	@echo "Formatting with Black..."
	$(VENV)/bin/black .

# Installation
install:
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt
	$(PIP) install black ruff

# Linting
lint:
	@echo "Linting with Ruff..."
	$(VENV)/bin/ruff check .

# Nettoyage
clean:
	@echo "Cleaning caches..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .ruff_cache

# Vérifier que venv existe
check-venv:
	@if [ ! -d "$(VENV)" ]; then \
		echo "venv not found! Run: python3 -m venv $(VENV)"; \
		exit 1; \
	fi

.PHONY: format install lint clean check-venv
