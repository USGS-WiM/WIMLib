import unittest
import sys
import os
from WIMLib import Shared
import datetime

class Test_Shared(unittest.TestCase):
    def test_readCSV(self):
        file = Shared.readCSVFile(os.path.join(os.path.dirname(__file__), 'sharedtest.csv'))
        headers = file[0]
        x = headers.index("dec_long")
        self.assertEqual(x, 1)

    def test_appendLineToFile(self):
        Shared.appendLineToFile(os.path.join(os.path.dirname(__file__), 'sharedtest_append.txt'),"appending this data"+str(datetime.datetime.now()).replace('-','').replace(' ','').replace(':','').replace('.',''))
        self.assertEqual(1, 1)

    def test_writeToFile(self):
        try:
            datatowrite=[]
            datatowrite.append("writing this row1"+str(datetime.datetime.now()).replace('-','').replace(' ','').replace(':','').replace('.',''))
            datatowrite.append("writing this row2"+str(datetime.datetime.now()).replace('-','').replace(' ','').replace(':','').replace('.',''))
            Shared.writeToFile(os.path.join(os.path.dirname(__file__), 'sharedtest_write.txt'),datatowrite)        
            self.assertEqual(1, 1)
        except:
            self.fail("failed")

    def test_try_parse(self):
        try:
            val = Shared.try_parse("1.2345")
            self.assertEqual(val, 1.2345)
        except:
            self.fail()
        
    def test_parse(self):
        val = Shared.parse("2.3546")
        self.assertEqual(val, 2.3546)

    def test_GetWorkspaceDirectory(self):
        try:
            workingDir = Shared.GetWorkspaceDirectory("D:/ClientData")
            self.assertIsNone(None)
        except:
            self.fail()
      