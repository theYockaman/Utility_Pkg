from unittest import TestCase
import unittest
from utils import file
import os


class TestJSON(TestCase):
    
    def test_init(self):
        
        # Create Test File & Creates the File
        f = file.JSON()
        
        # Check to see if the file exists
        exist = os.path.isfile(f.directory)
        
        # If File Exists
        self.assertTrue(exist)
        
        # Deletes File
        os.remove(f.directory)
        
        
        # Try a Parameter File
        
        
        # Create Test File & Creates the File
        f = file.JSON("new.json")
        
        # Check to see if the file exists
        exist = os.path.isfile(f.directory)
        
        # If File Exists
        self.assertTrue(exist)
        
        # Deletes File
        os.remove(f.directory)
        
    def test_read(self):
        
        # Create Test File & Creates the File
        f = file.JSON()
        
        # Read File
        data = f.read()
        
        # If File Exists
        self.assertEqual(data,{})
        
        # Deletes File
        os.remove(f.directory)
        
    def test_write(self):
        
        # Create Test File & Creates the File
        f = file.JSON()
        
        # Write to File
        f.write({"key":"value"})
        
        # Read File
        data = f.read()
        
        
        if list(data.keys())[0] == "key" and list(data.values())[0] == "value":
            exist = True
        else:
            exist = False
        
        # If File Exists
        self.assertTrue(exist)
        
        # Deletes File
        os.remove(f.directory)    
   
        
if __name__ == '__main__':
    unittest.main()