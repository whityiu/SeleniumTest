"""
===========
BaseTestCase
===========
"""
import unittest

from selenium import webdriver

import logging
import string
import random

class BaseTestCase(unittest.TestCase):
    """
    Intermediary class that all scripts will inherit from
    """
    def setUp(self):
        """
        This method runs before every 'test' method
        """
        self.verificationErrors = []
        self.driver = webdriver.Firefox()
        self.base_url = "https://www.mozilla.org/en-US/"
        self.driver.get(self.base_url)
        

    def tearDown(self):
        """
        This method runs after every 'test' method
        """
        self.driver.close()
        self.assertEqual([], self.verificationErrors)

    def verifyEqual(self, want, got):
        """
        Soft assert wrapper for assertEqual Does not not return anything, but on failure it will return append the assert exception to the list of failures for later script failing

        :param want: What you think you should have
        :param got: What you actually have
        """
        try:
            self.assertEqual(want, got)
        except AssertionError as e:
            self.verificationErrors.append("%s: %s" % (self._testMethodName, str(e)))

    def random_text(self, random_length = None):
        """
        Returns a random string of a-z plus whitespace

        :param random_length: (Optional) How big a string to generate. By default it is 1024 character.
        :returns: String
        """
        choices = string.letters + ' '
        text = []
        if not random_length:
            random_length = random.randint(1, 1024)
        for x in range(random_length):
            text.append(random.choice(choices))
        return "".join(text).strip()