import json
import sys
from os import path


class DataParser:
    data = []

    def __init__(self, data_conf):
        data_type = data_conf['type']
        if data_type == 'json':
            file_path = data_conf['path']
            self.data = self.jsonParsing(file_path)
        else:
            print("ERROR: Undefined format: " + data_type)
            sys.exit(1)

    def jsonParsing(self, file_path):
        return json.loads(open(path.normpath(file_path)).read())

    def getData(self):
        return self.data