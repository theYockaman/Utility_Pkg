from os.path import exists
from os import remove
import sqlite3 
from pandas import DataFrame, read_sql_query

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
        return f"{self.name} {self._convertType(self.dtype)}"

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def dype(self) -> type:
        return self._dtype

# Table Object for SQLite Database
class Table:
    def __init__(self, name:str, connection:sqlite3.Connection, columns:list[Column] = None, **kwargs) -> None:
        """_summary_

        :param name: Name of the Table
        :type name: str
        :param connection: Connection to the Database
        :type connection: sqlite3.Connection
        :param columns: Columns in the Database, defaults to None
        :type columns: list[Column], optional
        :raises ValueError: "Table Does Not Exists And Requires `columns` parameter to be filled"
        """
        # Name, Connection, & Columns
        self._name = name
        self._connection = connection
        self._columns = columns
        
        # Checking Existance of the Table
        if not  self.exist():
            if columns is None: raise ValueError("Table Does Not Exists And Requires `columns` parameter to be filled")

            self.create()
            
        # Pass on Keyword Arguments
        self.__dict__.update(kwargs)
    
    def exist(self, name:str = None, connection:sqlite3.Connection = None) -> bool:
        """Checks Existance of Table in Database

        :param name: Name of the Table, defaults to None
        :type name: str, optional
        :param connection: Connection to Database, defaults to None
        :type connection: sqlite3.Connection, optional
        :return: `True` Table Exists, `False` Table Does Not Exist
        :rtype: bool
        """
        # Set Name & Connection to Self
        if name is None or connection is None:
            name = self._name
            connection = self._connection
            
        # Checks Existance of Table
        return connection.execute(f"SELECT name FROM sqlite_master WHERE type ='table' AND name ='{name}';").fetchone() is not None
          
    def create(self, name:str = None, columns:list[Column] = None, connection:sqlite3.Connection = None) -> None:
        
        # Set Name & Connection to Self
        if name is None or columns is None or connection is None:
            name = self._name
            columns = self._columns
            connection = self._connection
        
        
        if not Table.exist(name,connection):
    
            # Creates the SQL Code
            sql = f"CREATE TABLE {name} ("
            
            for column in columns:
                if column == columns[-1]:
                    sql += column.sql
                else:
                    sql += f"{column.sql}, "
                
            sql += ") ;"
            # Creating Tables
            connection.execute(sql)
            connection.commit()
        
    def delete(self, name:str = None, connection:sqlite3.Connection = None) -> None:
        """Deletes Table from Database

        :param name: Name of the Table, defaults to None
        :type name: str, optional
        :param connection: Connection to Database, defaults to None
        :type connection: sqlite3.Connection, optional
        """
        # Set Name & Connection to Self
        if name is None or connection is None:
            name = self._name
            connection = self._connection
        
        # Checking the existance of the Table in the Database
        if Table.exist(name, connection): 
        
            # Deleting the Table
            connection.execute(f"DROP TABLE {name};")
            connection.commit()
        
    def update(self, df:DataFrame) -> None:
        """Changes DataFrame to Database Table

        :param df: DataFrame to Update Database
        :type df: DataFrame
        """
        
        # Turns DataFrame into 
        df.to_sql(self._name,self._connection, if_exists='replace', index = False)
   
    @property
    def data(self) -> DataFrame:
        """Data DataFrame in the Table Database

        :return: Table Data
        :rtype: DataFrame
        """
        # Dataframe stored in Database Table
        return read_sql_query(f"SELECT * FROM {self._name}", self._connection)

# Database Object for SQLite Database
class Database:
    def __init__(self, directory:str, **kwargs) -> None:
        """Database Object for SQLite

        :param directory: SQLite Database Directory
        :type directory: str
        """
        
        # Database Directory
        self._directory = directory
        
        # Create Database if does not Exist
        if not self.exist(): self.create()
        
        # Database Connection
        self._connection = sqlite3.connect(directory,timeout=8)
        
        # Pass on Keyword Arguments
        self.__dict__.update(kwargs)
        
    def exist(self, directory:str = None) -> bool:
        """Checks Existance of Database

        :param directory: Directory of SQLite Database, defaults to self.directory
        :type directory: str, optional
        :raises ValueError: "Not a .db file directory"
        :return: `True` Database Exists, `False` Database Does Not Exist
        :rtype: bool
        """
        # Assign Directory to Self if Directory is none existance
        if directory == None: directory = self._directory
        
        # Checks to see if Directory is a .db file
        if directory[-3:] != ".db": raise ValueError("Not a .db file directory")
        
        # Checks Directory Existance
        return exists(directory)
    
    def create(self, directory:str = None) -> None:
        """Creates Database

        :param directory: Database Directory, defaults to self.directory
        :type directory: str, optional
        """
        
        # Assign Directory to Self if Directory is none existance
        if directory == None: directory = self._directory
        
        # Checks to see if the Database already exists
        if not Database.exist(directory):
        
            # Creation of the Database File
            with open(directory,"x") as file:
                pass
    
    def delete(self, directory:str = None) -> None:
        """Delete Database

        :param directory: Database Directory, defaults to None
        :type directory: str, optional
        """
        
        # Assign Directory to Self if Directory is none existance
        if directory == None: directory = self._directory
        
        # Checks to see if the Database already exists
        if Database.exist(directory):
            remove(directory)
    
    @property
    def tables(self) -> list[Table]:
        """Returns Tables Stored in Database

        :return: Tables Stored in Database
        :rtype: list[Table]
        """
        # Table Names
        tableNames = [name[0] for name in self._connection.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
        
        # Create a Table Objects
        return [Table(name, self._connection) for name in tableNames]
    
    @property
    def name(self) -> str:
        return self._name
              
    @property
    def connection(self) -> sqlite3.Connection:
        return self._connection   
              