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
        t = {"yes":str,8:int,None:None,8.0:[int,float]}
        f = {"yes":int,8:str}
        
        existT = functions.checkType(t)
        
        try:
            existF = functions.checkType(f,True)
        except:
            existF = False
            self.assertFalse(existF)
            
            
        self.assertTrue(existT)
    
    def test_duration(self):
        
        d = functions.Duration()
        sleep(5)
        d.end()
        
if __name__ == '__main__':
    unittest.main()