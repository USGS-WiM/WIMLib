import unittest
from WIMLib.WiMLogging import WiMLogging as log

class Test_WiMLog(unittest.TestCase):
    def test_LoggingWithPath(self):
        
        log().sm("test")       
        self.assertEqual(1, 1)

    def test_LoggingWithOutPath(self):
        log("D:/ClientData")    
        log().sm('testlog')  
        self.assertEqual(1, 1)
