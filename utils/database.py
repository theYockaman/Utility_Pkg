
# Module Documentation
"""
Database Module:
    This module is used to manipulate database on an OOO level so then others who might not know SQL can work with databases easily.
"""


# Import Modules
import sqlite3, pandas, typing
from .functions import checkType
from .file import File

__all__ = [
    "Column"
    , "Database"
    , "Table"
    , "TableExistsError"
    , "TableNotFoundError"
    , "DatabaseExistsError"
    , "DatabaseNotFoundError"
]

# Exceptions
class TableExistsError(Exception):
    def __init__(self, *args: object) -> None:
        """Table Already Exists
        """
        super().__init__(*args)

class TableNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        """Table Not Found
        """
        super().__init__(*args)

class DatabaseExistsError(Exception):
    def __init__(self, *args: object) -> None:
        """Database Already Exists
        """
        super().__init__(*args)

class DatabaseNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        """Database Not Found
        """
        super().__init__(*args)

# Column Object for SQLite Database
class Column:
    def __init__(self, name:str, dtype:type, **kwargs) -> None:
        """Column for SQLite Table Database

        :param name: Column Name
        :type name: str
        :param dtype: DataType of Column
        :type dtype: type
        """
        
        # Column Name 
        self._name = name
        
        # Column Data Type
        self._dtype = dtype
        
        # Add Keyword Arguments
        self.__dict__.update(kwargs)
        
    @staticmethod
    def _convertType(type:type)-> str:
        """Convert Type into SQL Datatype

        :param type: Type in Python you want to Convert
        :type type: type
        :return: SQL Datatype
        :rtype: str
        """
        
        # Convert Type to SQLite Datatype
        dictionary = {int:"INTEGER",float:"REAL",str:"TEXT",bool:"BOOLEAN"}
        
        return dictionary.get(type)

    @property
    def sql(self) -> str:
        """SQL Code

        :return: SQL Code to create Column
        :rtype: str
        """
        
        # SQL code for Column Creation
        return f"{self._name} {self._convertType(self._dtype)}"
  
# Table Object for SQLite Database
class Table:
    def __init__(self, name:str, connection:sqlite3.Connection, columns:list[Column] = None, **kwargs) -> None:
        
        # Name, Connection, & Columns
        self._name = name
        self._connection = connection
        self._columns = columns
        
        # Checking Existance of the Table
        if not self.exists():
            
            # Check Column Parameter Filled
            if columns is None: raise TableNotFoundError("Table Does Not Exist, columns required to create")

            # Create Table
            self._create()
            
        # Pass on Keyword Arguments
        self.__dict__.update(kwargs)
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def columns(self) -> list[Column]:
        return self._columns
    
    def exists(self) -> bool:
        """Table Exists

        :return: `True` if it Exists, `False` if it does not Exist
        :rtype: bool
        """
            
        # Checks Existance of Table
        if self._connection is None: return False
        
        return self._connection.execute(f"SELECT name FROM sqlite_master WHERE type ='table' AND name ='{self._name}';").fetchone() is not None
          
    def _create(self) -> None:
        """Create Table in Database

        :raises TableNotFoundError:
        """
        
        # If the Table Does Not Exist
        if not self.exists():
    
            # Creates the SQL Code
            sql = f"CREATE TABLE {self._name} ("
            
            # Adds Each Column in the Table
            for column in self._columns:
                
                # Add each Column 
                sql += column.sql
                
                # If Last Column
                if column != self._columns[-1]:
                    sql += ", "
                
            sql += ") ;"
            
            # Creating Tables
            self._connection.execute(sql)
            self._connection.commit()
            
        else:
            raise TableNotFoundError()
        
    def delete(self) -> None:
        """Delete Table from Database

        :raises TableNotFoundError:
        """
        
        # Checking the existance of the Table in the Database
        if self.exists(): 
        
            # Deleting the Table
            self._connection.execute(f"DROP TABLE {self._name};")
            self._connection.commit()
            self._connection = None
            
        else:
            raise TableNotFoundError()
        
    def update(self, df:pandas.DataFrame) -> None:
        """Changes DataFrame to Database Table

        :param df: DataFrame to Update Database
        :type df: DataFrame
        :raises TableNotFoundError:
        """
        
        # Checking the existance of the Table in the Database
        if self.exists(): 
        
            # Turns DataFrame into 
            df.to_sql(self._name,self._connection, if_exists='replace', index = False)
            
        else:
            raise TableNotFoundError()
    
    @property
    def data(self) -> pandas.DataFrame:
        """Data DataFrame in the Table Database

        :return: Table Data
        :rtype: DataFrame
        """
        # Dataframe stored in Database Table
        return pandas.read_sql_query(f"SELECT * FROM {self._name}", self._connection)

# Database Object for SQLite Database
class Database:
    def __init__(self, directory:str = None, **kwargs) -> None:
    
        
        # File Creation
        self._file = File(directory, "db")
        
        # Database Directory
        self._directory = self._file.directory
        
        # Database Connection
        self._connection = sqlite3.connect(self._directory, timeout=8)
    
        
        # Pass on Keyword Arguments
        self.__dict__.update(kwargs)
      
    @property
    def directory(self) -> str:
        """Directory of the Database File

        :return: Database File (.db)
        :rtype: str
        """
        return self._directory  
        
    @property
    def connection(self) -> sqlite3.Connection:
        """Connection of the Database

        :return: Connection to the Database
        :rtype: sqlite3.Connection
        """
        return self._connection  
        
    @property
    def tables(self) -> list[Table]:
        return self._getTables()   
         
    def exists(self) -> bool:
        return self._file.exists()  
         
    def delete(self) -> None:
        """Delete Database

        :raises DatabaseNotFoundError:
        """
        
        # Checks to see if the Database already exists
        if self._file.exists():
            
            # Delete File 
            self._file.delete()
            
            # Clear Variables
            self._directory = None
            self._connection = None
            self._tables = None
            
        else:
            raise DatabaseNotFoundError()
    
    def addTable(self, name:str, columns:list[Column] = None) -> Table:
        """Add Table to Database

        :param name: Table Name/ Table Object
        :type name: str
        :param columns: Columns of Table 
        :type columns: list[Column]
        :return: Table Added to Database
        :rtype: Table
        """
        
        # Check Directory Type
        checkType([name, columns],[str, list])
        
        # Create Table
        t = Table( name, self._connection, columns)
        
        # Add Table to List of Tables
        self._tables.append(t)
        
        return t
      
    def removeTable(self, name:str) -> None:
        """Remove Table

        :param name: Name of the Table
        :type name: str
        :raises TableNotFoundError: 
        """
        
        # Check Name Type
        checkType([name],[str])
        
        # Check if it Table Exists
        if name not in [x.name for x in self._tables]: raise TableNotFoundError()
        
        # Remove the Table
        for x in self._tables:
            if name == x.name:
                
                # Delete Table
                x.delete()
                self._tables.remove(x)
            
        
             
    def _getTables(self) -> list[Table]:
        """Gathers Tables in the Database

        :return: Tables in the Database
        :rtype: list[Table]
        """
        
        # Table Names
        tableNames = [name[0] for name in self._connection.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
        
        # Create a Table Objects
        return [Table(name, self._connection) for name in tableNames]
         
         
         
    isinstance