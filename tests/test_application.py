from unittest import TestCase
import unittest
from utils import package
import os
import pandas


class TestApplication(TestCase):
    
    def test_coverPage(self):
        package.coverPage()
             
if __name__ == '__main__':
    unittest.main()