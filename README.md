# Black-box tests created with Selenium Python API

**To run all tests one has to:**
- install *Mozilla Firefox* browser (other browsers would require changes in code, especially those connected with the driver)
- prepare environment using one of below commands:
  - `python -m pip install -r requirements.txt`
  - `conda env create -n <env name> -f req.txt` (for *Anaconda* users)
- make sure to have downloaded *geckodriver* (driver for *Mozilla Firefox* browser) and added to environment variable `PATH` 
(read more [here](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/))
- use command `python <test_name>` (for example: `python test_login_right.py`)

## Further reading
- https://selenium-python.readthedocs.io/installation.html#
- https://selenium-python.readthedocs.io/getting-started.html
