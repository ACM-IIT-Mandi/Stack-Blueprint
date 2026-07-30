# Standard task interface for every Stack-Blueprint blueprint.
# The TARGET NAMES are standardised across all blueprints; what they run is yours.
# CI calls these exact names, and so do people comparing blueprints. Do not rename them.


.DEFAULT_GOAL := help
.PHONY: help setup dev test lint format check docker-up docker-down

# Read from .env if present, so `make dev` picks up your configuration.
-include .env

APP_PORT ?= {{PORT_BASE}}


help: ## List available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'


setup: ## Install dependencies (must be idempotent, and work from a clean clone)
	@echo "TODO: install dependencies"
	@echo "  python: uv sync   |   node: npm ci   |   go: go mod download"
	@exit 1


dev: ## Run the application locally, with reload if the framework supports it
	@echo "TODO: run the app on port $(APP_PORT)"
	@exit 1


test: ## Run the full test suite (must exit non-zero on failure)
	@echo "TODO: run tests"
	@exit 1


lint: ## Report problems. MUST NOT modify any file.
	@echo "TODO: run the linter"
	@exit 1


format: ## Rewrite files to the canonical style
	@echo "TODO: run the formatter"
	@exit 1


check: ## Format check + lint + tests. EXACTLY what CI runs. Must not modify files.
	@echo "TODO: run format --check, then lint, then tests"
	@exit 1


docker-up: ## Build and start everything, waiting until healthy
	docker compose up --build --wait


docker-down: ## Stop everything and remove volumes
	docker compose down --volumes --remove-orphans
