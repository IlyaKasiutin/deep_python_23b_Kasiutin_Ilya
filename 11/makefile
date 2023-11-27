make:
	python3 -m venv venv
	chmod +x venv/bin/activate
	. venv/bin/activate
	python3 setup.py install

test:
	python3 -m unittest --coverage test_json_dumps.py test_json_loads.py
