from configparser import ConfigParser
import os
import sys


class ConfigData:
    conf = ''
    parser = ''

    def __init__(self, conf='conf.ini'):
        if os.path.exists(conf):
            self.conf = conf
        else:
            print("Config not exist for path: " + conf)
            sys.exit(1)

        self.parser = ConfigParser()
        self.parser.read(self.conf)

    def __del__(self):
        pass

    def get(self, section, field):
        if not self.parser.has_section(section):
            return False

        return self.parser.get(section, field)

    def get_section(self, section):
        section_data = {}
        options = self.parser.options(section)
        for option in options:
                if self.parser.get(section, option):
                    section_data[option] = self.parser.get(section, option)
                else:
                    section_data[option] = None

        return section_data
