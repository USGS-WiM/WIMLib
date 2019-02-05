import unittest
import sys
import os
from WIMLib.WiMLogging import WiMLogging as log
from WIMLib.Config import Config
import json
from collections import namedtuple

class Test_WiMLog(unittest.TestCase):
    def test_LoggingWithPath(self):
        log().sm("sample")    
        log().sm(os.path.dirname(sys.executable))
        self.assertEqual(1, 1)

    def test_LoggingWithOutPath(self):
        log("D:/ClientData")    
        log().sm('samplelog')  
        log().sm(os.path.dirname(sys.executable))
        self.assertEqual(1, 1)
