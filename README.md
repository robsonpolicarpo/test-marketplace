# Marketplace IntegrationTests


###### Integrations tests using BDD, Web, API tests with Python and Selenium frameworks


#### Requirements

Linux (Optional)  
Python 3.7 ou superior


#### Install dependencies

You can use virtualenv, if you want.
```
$ virtualenv -p python3 venv

$ source venv/bin/activate

$ pip install -r requirements.txt
```


#### Install ChromeDriver

Chromedriver must be in your PATH.  
If you are using virtualenv you have to put the file in venv/bin.  
The script below make the download of the version 80 of Chrome,  
if your Chrome is in other version, you can change the script or 
download manually in <https://chromedriver.chromium.org/downloads>
```
$ ./setup_chromedriver.sh
```


#### Run Local

Use Pytest to run the tests. 
You can use Makefile in project to run the tests
```bash
$ make testapi
$ make testcases
$ make testbdd
$ make alltests
```


Pytest options:

```
$ pytest            >> base
$ -k "my-tag"       >> tags
$ --tb=short        >> log
```

#### Run Remote

You can run in Jenkins or another CI, 
but need some few config and verifications, so in the next version 
it will be possible and how to run write here.


#### Report

In this moment you can see just the console log, but you can see some reports with 
pytest and pytest-bdd.

If you use CI you can add plugins like "Cucumber Json Reporter" and "Allure Report"
 
- pytest-bdd options:
```bash
--cucumberjson-expanded 
--cucumberjson='./reports/json/report.json'
```


#### References

* https://blog.testproject.io/2019/07/16/set-your-test-automation-goals/
* https://github.com/yashaka/selene
