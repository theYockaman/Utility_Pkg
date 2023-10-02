from unittest import TestCase
import unittest
from utils import file
import os




class TestFile(TestCase):
    
    def test_init(self):
        
        # Create Test File & Creates the File
        f = file.File()
        
        # Check to see if the file exists
        exist = os.path.isfile(f.directory)
        
        # If File Exists
        self.assertTrue(exist)
        
        # Deletes File
        os.remove(f.directory)
        
        
        # Try a Parameter File
        
        
        # Create Test File & Creates the File
        f = file.File("new.txt")
        
        # Check to see if the file exists
        exist = os.path.isfile(f.directory)
        
        # If File Exists
        self.assertTrue(exist)
        
        # Deletes File
        os.remove(f.directory)
        
    def test_delete(self):
        
        # Create File
        f = file.File()
        
        # Deletes File
        f.delete()
        
        # Check to see if the file exists
        exist = os.path.isfile("test.txt")
        
        # If File Exists
        self.assertFalse(exist)
        
    def test_exist(self):
        
        # Create Test File & Creates the File
        f = file.File()
        
        # Check to see if the file exists
        existOS = os.path.isfile(f.directory)
        existFile = f.exists()
        
        # If File Exists
        self.assertEqual(existOS,existFile)
        
        # Deletes File
        os.remove(f.directory)
        
    def test_read(self):
        
        # Create Test File & Creates the File
        f = file.File()
        
        # Read File
        data = f.read()
        
        # If File Exists
        self.assertEqual(data,"")
        
        # Deletes File
        os.remove(f.directory)
        
    def test_write(self):
        
        # Create Test File & Creates the File
        f = file.File()
        
        # Write to File
        f.write("Hello World")
        
        # Read File
        data = f.read()
        
        # If File Exists
        self.assertEqual("Hello World",data)
        
        # Deletes File
        os.remove(f.directory)    
        
    def test_rename(self):
        
        
        # Create Test File & Creates the File
        f = file.File("test.txt")
        
        # Rename
        f.rename("newName")
        
        # If File Exists
        self.assertEqual(f.directory,f"{file.LOCAL_DIRECTORY}/newName.txt")
        
        # Deletes File
        os.remove(f.directory)
  
    def test_move(self):
        
        # Create Test File & Creates the File
        f = file.File()
        
        # Move File
        f.move("test.txt")
        
        # If File Exists
        self.assertEqual(f.directory,"test.txt")
        
        # Deletes File
        os.remove(f.directory)
         
if __name__ == '__main__':
    unittest.main()