.PHONY: install test test-unit test-integration test-acceptance test-regression test-e2e test-slow clean help

help:
	@echo "Jekyll Site Test Suite"
	@echo ""
	@echo "Available targets:"
	@echo "  make install           Install Python dependencies and Playwright browsers"
	@echo "  make test              Run all tests"
	@echo "  make test-unit         Run unit tests only (fast)"
	@echo "  make test-integration  Run integration tests (parse HTML)"
	@echo "  make test-acceptance   Run acceptance tests (HTTP server)"
	@echo "  make test-regression   Run regression tests (snapshots, CSS)"
	@echo "  make test-e2e          Run E2E tests (Playwright browser)"
	@echo "  make test-slow         Run slow tests (all + integration + acceptance + E2E)"
	@echo "  make clean             Remove cached files and snapshots"
	@echo "  make help              Show this help message"

install:
	pip3 install -r requirements.txt
	playwright install chromium
	@echo "✓ Installation complete. Run 'make test' to verify."

test:
	pytest -v

test-unit:
	pytest unit/ -v -m unit

test-integration:
	pytest integration/ -v -m integration

test-acceptance:
	pytest acceptance/ -v -m acceptance

test-regression:
	pytest regression/ -v -m regression

test-e2e:
	pytest e2e/ -v -m e2e

test-slow:
	pytest -v -m "not skip"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf regression/snapshots/*.json
	@echo "✓ Cleaned cache and snapshots"

update-snapshots:
	pytest regression/ -v --update-snapshots

# Special target for CI (if added later)
test-ci:
	pytest -v --tb=short --junit-xml=test-results.xml
