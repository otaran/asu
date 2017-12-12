import yaml
import os.path
from shutil import copyfile

class Config():
    def __init__(self, config_file="config.yml"):
        self.config = {}

        if not os.path.exists(config_file):
            copyfile(("config.yml.default"), config_file)

        with open(config_file, 'r') as ymlfile:
            self.config = yaml.load(ymlfile)

    def load(self):
        return self.config

