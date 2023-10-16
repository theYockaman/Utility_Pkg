from unittest import TestCase
import unittest
from utils import functions
from time import sleep

class TestFunctions(TestCase):
    
    def test_printSyntax(self):
        
        # Print Syntax
        functions.printSyntax("Syntax")
        
        # Print Syntax
        functions.printSyntax("Syntax", False)
        
    def test_checkType(self):
        
        # Check Type
        vt = ["yes",9,None,8.0]
        vvt = [str,int,None,[int,float]]
        
        vf = ["yes",8]
        vvf = [int,str]
        
        existT = functions.checkType(vt,vvt,False)
        self.assertTrue(existT)
        
        existF = functions.checkType(vf,vvf,False)
        self.assertFalse(existF)
           
    def test_duration(self):
        
        d = functions.Duration()
        sleep(5)
        d.end()
        
if __name__ == '__main__':
    unittest.main()