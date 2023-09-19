from unittest import TestCase
import unittest
from utils import file
import os
import shutil

class TestFolder(TestCase):
    
    def test_init(self):
        # Create Test Folder & Creates the Folder
        f = file.Folder()
        
        # Check to see if the folder exists
        exist = os.path.isdir(f.directory)
        
        # If Folder Exists
        self.assertTrue(exist)
        
        # Deletes Folder
        shutil.rmtree(f.directory)
        
        
        # Try a Parameter Folder
        
        
        # Create Test File & Creates the File
        f = file.Folder("test")
        
        # Check to see if the folder exists
        exist = os.path.isdir(f.directory)
        
        # If Folder Exists
        self.assertTrue(exist)
        
        # Deletes Folder
        shutil.rmtree(f.directory)
        
    def test_exist(self):
        # Create Test Folder & Creates the Folder
        f = file.Folder()
        
        # Check to see if the folder exists
        ex = os.path.isdir(f.directory)
        
        fex = f.exists()
        
        # If Folder Exists
        self.assertEqual(ex,fex)
        
        # Deletes Folder
        shutil.rmtree(f.directory)
         
    def test_delete(self):
        # Create Test Folder & Creates the Folder
        f = file.Folder("test")
        
        # Delete File
        f.delete()
        
        # Check to see if the folder exists
        exist = os.path.isdir("test")
        
        # If Folder Exists
        self.assertFalse(exist)
        
    def test_rename(self):
        # Create Test Folder & Creates the Folder
        f = file.Folder("new")
        
        # Rename Folder
        f.rename("testFolder")
        
        # Check to see if the folder exists
        exist = os.path.isdir("testFolder")
        
        # If Folder Exists
        self.assertTrue(exist)
        
        # Deletes Folder
        shutil.rmtree(f.directory)
        
    def test_move(self):
        # Create Test Folder & Creates the Folder
        f = file.Folder("new")
        
        # Rename Folder
        f.move("testFolder")
        
        # Check to see if the folder exists
        exist = os.path.isdir("testFolder")
        
        # If Folder Exists
        self.assertTrue(exist)
        
        # Deletes Folder
        shutil.rmtree(f.directory)
   
        
if __name__ == '__main__':
    unittest.main()