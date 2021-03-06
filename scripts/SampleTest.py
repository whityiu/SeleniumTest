import BaseTestCase

from BaseException import ElementNotPresentException
from selenium import webdriver

from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest

class SampleTest(BaseTestCase.BaseTestCase):
    """
    Load Google.com
    """
    @attr(tags=['deep', 'dashboard', 'google'])
    def GoogleLoad(self):
        driver = self.driver
        driver.get(self.base_url)

    @attr(tags=['deep', 'dashboard', 'python'])
    def PythonOrgBodyClass(self):
        driver = self.driver
        driver.get("Http://www.python.org")
        bodyTag = driver.find_element_by_tag_name("body")
        print("Test Setting = " + self.cf.get("Test", "test_setting"))
        self.verifyEqual("homepage", bodyTag.get_attribute("id"))
    
    @attr(tags=['deep', 'dashboard', 'python'])    
    def FailedTest(self):
        driver = self.driver
        driver.get("Http://www.python.org")
        bodyTag = driver.find_element_by_tag_name("body")
        self.verifyEqual("notarealid", bodyTag.get_attribute("id"))

    @attr(tags=['deep', 'dashboard', 'python'])    
    def SearchBoxTest(self):
        driver = self.driver
        driver.get("Http://www.python.org")
        searchBox = driver.find_element_by_id("id-search-field")
        self.verifyEqual("search", searchBox.get_attribute("type"))
        
    @attr(tags=['deep', 'dashboard', 'python'])    
    def FailedSearchBoxTest(self):
        driver = self.driver
        driver.get("Http://www.python.org")
        searchBox = driver.find_element_by_id("id-search-field")
        self.verifyEqual("input", searchBox.get_attribute("type"))
        
    @attr(tags=['deep', 'dashboard', 'python', 'ex'])    
    def CustomExceptionTest(self):
        driver = self.driver
        driver.get("Http://www.python.org")
        raise ElementNotPresentException("Exception - Element is not present")