make:
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt
	python3 setup.py install

test:
	python -m coverage run -m unittest
	python -m coverage report
