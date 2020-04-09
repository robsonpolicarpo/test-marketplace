testapi :
	python -m pytest tests/service/test_service.py \
	--tb=short

testcases :
	python -m pytest tests/web/test_check_product_in_cart.py \
	--tb=short

testbdd :
	python -m pytest -k "automated" --tb=short \
	--gherkin-terminal-reporter-expanded \
	--cucumberjson='./reports/json/report.json' --cucumberjson-expanded

alltests :
	python -m pytest \
	--tb=short
