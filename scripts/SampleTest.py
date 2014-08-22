"""
===============
Dashboard Goals
===============
"""
import BaseTestCase

from selenium import webdriver

from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest

class SampleTest(BaseTestCase.BaseTestCase):
    """
    Load Google.com
    """
    @attr(tags=['deep', 'dashboard', 'google'])
    def NatureAboutUs(self):
        driver = self.driver
        driver.get(self.base_url)
