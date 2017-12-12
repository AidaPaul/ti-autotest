# Autotest for TI

## Installation
To install you will need [python 3.3+](https://www.python.org/downloads/release/python-363/) and [pip](https://pypi.python.org/pypi/pip). With thoe two installed all there is left is to run `pip install -r requirements.txt` and you are ready to go!

### Configuration
We also have to provide login credentials to the game. To do so copy the file `settings.py.template` as `settings.py` and fill the `name` and `password` fields for the user. Can also adjust the host and port if required.

## Usage
The very basic suage is to navigate to the root directory of the application and fire up `behave`. That will run all test suites and print results of them as it chugs along. There are more options which can be found on [behave website](https://pythonhosted.org/behave/behave.html#command-line-arguments).