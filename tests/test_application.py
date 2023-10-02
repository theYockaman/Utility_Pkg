from unittest import TestCase
import unittest
from utils import package
import os
import pandas
import sys

class TestApplication(TestCase):
    
    def test_coverPage(self):
        
        def test():
            pass
        
        package.coverPage("___Hello_World____",{"Print":test})
             
if __name__ == '__main__':
    unittest.main()