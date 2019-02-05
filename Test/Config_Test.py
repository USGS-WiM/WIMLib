import unittest
import sys
import os
from WIMLib.Config import Config
import json
from collections import namedtuple

class Test_Config(unittest.TestCase):
    def test_Config(self):
        #configFile = json.loads('{"workingdirectory": "D:/ClientData/Test"}', object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        configFile = json.load(open(os.path.join(os.path.dirname(__file__), 'config.json')))
        config = Config(configFile)

        workingdir = config["workingdirectory"]
        self.assertEqual(1, 1)
