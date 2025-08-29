.PHONY: gen-services lint fmt

gen-services:
	python3 scripts/summarize_cf_template.py template.yaml

lint:
	# Lint CFN locally if you have cfn-lint installed
	cfn-lint template.yaml || echo "Install cfn-lint to lint locally"

fmt:
	# Add formatters as needed (e.g., black, prettier)
	@echo "No formatters configured yet"
