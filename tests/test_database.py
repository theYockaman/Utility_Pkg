from unittest import TestCase
import unittest
from utils import database
import os


class TestDatabase(TestCase):
    
    def test_init(self):
        
        # Create Test Database
        d = database.Database()
        
        # Check to see if the file exists
        exist = os.path.isfile(d.directory)
        
        # If File Exists
        self.assertTrue(exist)
        
        self.assertEqual(d.tables, [])
        
        # Deletes File
        os.remove(d.directory)
        
        
        # Try a Parameter File
        
        
        # Create Test File & Creates the File
        d = database.Database("test.db")
        
        # Check to see if the file exists
        exist = os.path.isfile(d.directory)
        
        # If File Exists
        self.assertTrue(exist)
        
        self.assertEqual(d.tables, [])
        
        # Deletes File
        os.remove(d.directory)
       
    def test_exist(self):
        
        # Create Test Database
        d = database.Database()
        
        # Check to see if the file exists
        existT = os.path.isfile(d.directory)
        existD = d.exists()
        
        # If File Exists
        self.assertEqual(existT, existD)
        
        # Deletes File
        os.remove(d.directory)

    def test_delete(self):
        
        # Create Test Database
        d = database.Database()
        
        # Delete File
        d.delete()
        
       
        # If File Exists
        self.assertEqual(d.directory,None)

    def test_addTable(self):
        
        # Create Test Database
        d = database.Database()
        
        columns = [database.Column("First Name", str),database.Column("Last Name", str)]
        
        d.addTable("tableName",columns)
        
        # Check in Tables Variable
        self.assertIn("tableName",[x.name for x in d.tables])
    
        # Check in the Database File
        self.assertIn("tableName",[name[0] for name in d.connection.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()])
        
        
        # Deletes File
        os.remove(d.directory)
        
    def test_removeTable(self):
        
        # Create Test Database
        d = database.Database()
        
        # Check to see if the file exists
        columns = [database.Column("First Name", str),database.Column("Last Name", str)]
        
        d.addTable("tableName",columns)
        d.removeTable("tableName")
        
        # Check in Tables Variable
        self.assertNotIn("tableName",[x.name for x in d.tables])
    
        # Check in the Database File
        self.assertNotIn("tableName",[name[0] for name in d.connection.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()])
        
        # Deletes File
        os.remove(d.directory)
        
  
  
        
if __name__ == '__main__':
    unittest.main()