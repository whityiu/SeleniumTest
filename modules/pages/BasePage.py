import time
from BaseException import ElementVisiblityTimeout, ElementTextTimeout
from pages import timeout_seconds

class BasePage(object):
    def wait_for_visible(self, locator):
        """
        Synchronization helper to wait until the Goal popup is displayed
        
        :raises: ElementVisiblityTimeout
        
        """
        for i in range(timeout_seconds):
            try:
                if self.se.is_visible(locator):
                    break
            except:
                pass
            time.sleep(1)
        else:
            raise ElementVisiblityTimeout("%s visibility timed out" % locator)
        return True

    def wait_for_hidden(self, locator):
        """
        Synchronization helper to wait until the Goal popup is no longer displayed

        :raises: ElementVisiblityTimeout

        """
        for i in range(timeout_seconds):
            if self.se.is_visible(locator):
                time.sleep(1)
            else:
                break
        else:
            raise ElementVisiblityTimeout("%s visibility timed out" % locator)
        return True
            
    def wait_for_text(self, locator, text):
        """
        Synchronization helper to wait until the Goal popup is displayed

        :raises: ElementVisiblityTimeout

        """
        for i in range(timeout_seconds):
            try:
                if self.se.get_text(locator) == text:
                    break
            except:
                pass
            time.sleep(1)
        else:
            raise ElementTextTimeout("%s value timed out" % locator)
        return True

    def wait_for_value(self, locator, text):
        """
        Synchronization helper to wait until the Goal popup is displayed

        :raises: ElementVisiblityTimeout

        """
        for i in range(timeout_seconds):
            try:
                if self.se.get_value(locator) == text:
                    break
            except:
                pass
            time.sleep(1)
        else:
            raise ElementTextTimeout("%s value timed out" % locator)
        return True
            
    def wait_for_element_not_present(self, locator):
        """
        Synchronization helper to wait until the Goal popup is displayed

        :raises: ElementVisiblityTimeout

        """
        for i in range(timeout_seconds):
            if self.se.is_element_present(locator):
                time.sleep(1)
            else:
                break
        else:
            raise ElementVisiblityTimeout("%s presence timed out" % locator)
        return True

