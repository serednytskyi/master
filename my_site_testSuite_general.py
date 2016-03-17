import unittest
from xmlrunner import xmlrunner
# Test runner capable of crating HTML reprots
import HTMLTestRunner
import os
from my_site_testCase_data import mysite_testCase_data
from my_site_testCase_deployed import mysite_testCase_deployed
from my_site_testCase_JQeury_scripts import mysite_testCase_JQuery_scripts

# Test suite with all the test cases merged. All tests could be launched from here (added or removed).
# Couple of test runners are also available from here.

dir = os.getcwd()

mysite_testCase_deployed = unittest.TestLoader().loadTestsFromTestCase(mysite_testCase_deployed)
mysite_testCase_data = unittest.TestLoader().loadTestsFromTestCase(mysite_testCase_data)
mysite_testCase_JQuery_scripts = unittest.TestLoader().loadTestsFromTestCase(mysite_testCase_JQuery_scripts)


smoke_tests = unittest.TestSuite([mysite_testCase_deployed, mysite_testCase_data, mysite_testCase_JQuery_scripts])

outfile = open(dir + "\SmokeTestReport.html", "w")

runner = HTMLTestRunner.HTMLTestRunner(
	stream=outfile,
	title="Personal_Site_autotest_report",
	description="Smoke Tests"
)


#xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_tests) # Uncomment to use generate JUnit format report to use with Jenkins
runner.run(smoke_tests) # Uncomment to use HTML runner to get HTML report
#unittest.TextTestRunner(verbosity=2).run(smoke_tests) # Simple runner
