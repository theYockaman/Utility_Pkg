from unittest import TestCase
import unittest, pandas
from utils import database
import os


class TestTable(TestCase):
       
    def test_exists(self):
        
        # Create Test Database
        d = database.Database()
        
        self.assertEqual(len(d.tables),0)
        
        columns = [database.Column("First Name", str),database.Column("Last Name", str)]
        d.addTable("tableName",columns)
        
        self.assertTrue(d.tables[0].exists())
        
        # Deletes File
        os.remove(d.directory)

    def test_delete(self):
        
        # Create Test Database
        d = database.Database()
        
        columns = [database.Column("First Name", str),database.Column("Last Name", str)]
        d.addTable("tableName",columns)
        
        self.assertTrue(d.tables[0].exists())
        d.removeTable("tableName")
        self.assertEqual(len(d.tables),0)
        
        # Deletes File
        os.remove(d.directory)

    def test_update(self):
        
        # Create Test Database
        d = database.Database()
        
        columns = [database.Column("First Name", str),database.Column("Last Name", str)]
        d.addTable("tableName",columns)
        
        
        df = pandas.DataFrame({"First Name":["Nathan"],"Last Name":["Yockey"]})
        
        d.tables[0].update(df)
        
        pandas.testing.assert_frame_equal(d.tables[0].data,df)
        
        # Deletes File
        os.remove(d.directory)
        
 
  
        
if __name__ == '__main__':
    unittest.main()