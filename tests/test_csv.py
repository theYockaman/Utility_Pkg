from unittest import TestCase
import unittest
from utils import file
import os
import pandas


class TestCSV(TestCase):
    
    def test_init(self):
        
        # Create Test File & Creates the File
        f = file.CSV()
        
        # Check to see if the file exists
        exist = os.path.isfile(f.directory)
        
        # If File Exists
        self.assertTrue(exist)
        
        # Deletes File
        os.remove(f.directory)
        
        
        # Try a Parameter File
        
        
        # Create Test File & Creates the File
        f = file.CSV("new.csv")
        
        # Check to see if the file exists
        exist = os.path.isfile(f.directory)
        
        # If File Exists
        self.assertTrue(exist)
        
        # Deletes File
        os.remove(f.directory)
        
    def test_read(self):
        
        # Create Test File & Creates the File
        f = file.CSV()
        
        # Read File
        data = f.read()
        
        # If File Exists
        self.assertTrue(data.empty)
        
        # Deletes File
        os.remove(f.directory)
        
    def test_write(self):
        
        # Create Test File & Creates the File
        f = file.CSV()
        
        # Write to File
        df = pandas.DataFrame([10,20,30,40,50,60],columns=['Numbers'])
        
        # Write to File
        f.write(df)
        
        # Read File
        data = f.read()
        
        #Check
        pandas.testing.assert_frame_equal(df,data)
        
        # Deletes File
        os.remove(f.directory)    
   
        
if __name__ == '__main__':
    unittest.main()