all: clean-pyc test

test:
	python setup.py nosetests --stop --tests tests.py

travis:
	python setup.py nosetests --tests tests.py

shell:
	../venv/bin/ipython

audit:
	python setup.py autdit

release:
	python setup.py sdist upload

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

find-print:
	grep -r --include=*.py --exclude-dir=venv --exclude=fabfile* --exclude=tests.py --exclude-dir=tests --exclude-dir=commands 'print' ./