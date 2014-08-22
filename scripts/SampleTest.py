import BaseTestCase

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
        self.assertEqual("homepage", bodyTag.get_attribute("id"))
    
    @attr(tags=['deep', 'dashboard', 'python'])    
    def FailedTest(self):
        driver = self.driver
        driver.get("Http://www.python.org")
        bodyTag = driver.find_element_by_tag_name("body")
        self.assertEqual("notarealid", bodyTag.get_attribute("id"))