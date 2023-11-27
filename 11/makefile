make:
	python3 -m venv environ
	. venv/bin/activate
	pip install requirements.txt
	python3 setup.py install

test:
	python3 -m unittest --coverage test_json_dumps.py test_json_loads.py
