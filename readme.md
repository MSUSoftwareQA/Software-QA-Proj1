# Software Testing and QA Porject 1

## Prereqs

* [python3](https://www.python.org/)
	* Preinstalled in most Linux distros. Possibly just under the package name of "python".
	* Installation instructions and guide: https://wiki.python.org/moin/BeginnersGuide
	* Version used for development and testing: 3.6.0
* [pip](https://pypi.python.org/pypi/pip)
	* Just needed to pytest. Under the package name of "python-pip" in most Linux repos.
	* Full installation instructions here: https://pip.pypa.io/en/stable/installing/
	* Version used for development and testing: 9.0.1 (python 3.6)
* [pytest](http://docs.pytest.org/en/latest/)
	* To install: pip install -U pytest
	* Installation instructions and guide: http://docs.pytest.org/en/latest/getting-started.html
	* Version used for development and testing: 3.0.6

## Running tests

1. Open shell and move to directory containing program files.
2. Run the test with: pytest test.py
	* If all tests have passed, a green success message will appear telling you how many of the tests have passed.
	* If any of the tests fail, a red failure message will be printed showing which of the tests have failed and where.

Each test within the [test.py](https://github.com/MSUSoftwareQA/Software-QA-Proj1/blob/master/test.py) file checks each of the functions within [functions.py](https://github.com/MSUSoftwareQA/Software-QA-Proj1/blob/master/functions.py). Each one of the tests runs multiple checks for all types of inputs that could be given to them.

## Running the program

1. Open shell and move to directory containing program files.
2. Run: python3 formulas.py

The program will then step you through how to run each part of the program.