import configparser
import os.path

class ConfigWrapper(object):
    # singleton
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def configure(self, config = "selenium.ini"):
        self.config = configparser.RawConfigParser()
        self.config.readfp(open(os.path.join("..", "support", "conf", config)))

# initialize the singleton
cf = ConfigWrapper().configure()