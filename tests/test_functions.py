from unittest import TestCase
import unittest
from utils import functions
from time import sleep
import pandas
from typing import List

class TestFunctions(TestCase):
    
    def test_printSyntax(self):
        
        # Print Syntax
        functions.printSyntax("Syntax")
        
        # Print Syntax
        functions.printSyntax("Syntax", False)
        
    def test_checkType(self):
        
        # Check Type
        v = ["yes",9,None,8.0]
        vv = [str,int,None,[int,float]]
        
        exist = functions.checkType(v,vv,False)
        self.assertTrue(exist)
        
        
        
        
        v = ["yes",8]
        vv = [int,str]
        
        exist = functions.checkType(v,vv,False)
        self.assertFalse(exist)
        
        
        
        v = ["yes",8]
        vv = [int,[int,str]]
        
        exist = functions.checkType(v,vv,False)
        self.assertFalse(exist)
        
        
        v = ["yes",["t","v"]]
        vv = [int,[int,str]]
        
        exist = functions.checkType(v,vv,False)
        self.assertFalse(exist)
        
        oneDF = pandas.Series()
        twoDF = pandas.Series()
        
        var = [oneDF,twoDF]
        exist = functions.checkType([var],[List[pandas.Series]],False)
        self.assertTrue(exist)
        
        
    def test_duration(self):
        
        d = functions.Duration()
        sleep(5)
        d.end()
        
if __name__ == '__main__':
    unittest.main()