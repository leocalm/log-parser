[![Build Status](https://travis-ci.org/leocalm/log-parser.svg?branch=master)](https://travis-ci.org/leocalm/log-parser)

# Log Parser
Utility to parse log and get data from it. 

This application allows you to parse the log and get info about webhoooks sent to clients.

The utility will inform the thre most accessed urls via webhook, and the amount of requests aggreagated by status.

## Requirements
In order to run and test the application, the following packages are needed:
 - pytest
 - pytest-cov
 - coveralls
 
To install the requirements, it is need to have both `Python3` and `pip3` isntalled, and then run
```
pip3 install -r requirements.txt
```

## Running the tests and measuring coverage
To run the application unit tests, just call `pytest`:
```
pytest
```
If you also want to measure coverage, just add a `--cov=.`
```
pytest --cov=.
```
The result will be shown on the screen
```
----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name             Stmts   Miss  Cover
------------------------------------
log_parser.py       32      0   100%
parse.py            13      0   100%
test_parser.py      87      0   100%
------------------------------------
TOTAL              132      0   100%

```

## Parsing log files
To parse a log file, just call the parse.py utility
```
python3 parse.py <file_path>
```
The application receives the log file name as a argument, perform the parse and print the results
```
➜  log-parser git:(master) python3 parse.py log.txt 
http://localHost-13.com.br/test - 2
http://localhost - 1

200 - 2
400 - 1
```
