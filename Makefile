export PYTHONPATH := $(shell pwd)
export SOURCE_DIR=/vagrant/source_dir/


develop:
	pip install -r requirements.txt

test:
	pytest

testxml:
	pytest --junitxml test_results.xml --cov ./DataStructuresandAlgorithmsInPython --cov-config tests/.coveragerc --cov-report xml

lint:
	pylint --ignore=vendor DataStructuresandAlgorithmsInPython | tee pylintout.text

bld:
	pip install -r requirements.txt
	python setup.py build

clean:
	-rm -rf dist/
	-rm -rf .pytest_cache/
	-rm -rf spacereclamation.egg-info/
	-rm -rf htmlcov
	-rm -rf build/
	-rm coverage.xml
	-rm test_results.xml
	-rm pylintout.text