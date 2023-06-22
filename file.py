from typing import Union
import os
import json
import pandas as pd

# Inital File Object to Base around Specific Files
class File:
    def __init__(self, directory:str = f"{os.path.dirname(os.path.abspath(__file__))}/new.txt") -> None:
        """File object to help manipulate files with ease.

        :param directory: Directory of the File, defaults to f"{os.path.dirname(os.path.abspath(__file__))}/new.txt"
        :type directory: str, optional
        """
        # Directory of File
        self.directory = directory
        
        # Creates File if Does Not Exist
        if not self.exists(self.directory): self.create(self.directory)
    
    @staticmethod
    def exists(directory:str) -> bool:
        """Check File Existance

        :param directory: Directory of the File
        :type directory: str
        :return: `True` File Exists and `False` File Does Not Exist
        :rtype: bool
        """
        try:
            return os.path.isfile(directory)
        except:
            return False

    @staticmethod
    def create(directory:str) -> bool:
        """Create a New File

        :param directory: Directory of File
        :type directory: str
        :return: `True` if File is Created, `False` if File is Not Created
        :rtype: bool
        """
        try:
            with open(directory,"x") as file:
                pass
            return True
        except:
            return False
        
    def delete(self) -> bool:
        """Delete File that Exists

        :return: `True` If File is Deleted, `False` If File is Not Deleted
        :rtype: bool
        """
        try:
            # Deletes the File
            os.remove(self.directory)
            
            # Sets Directory to None
            self.directory = None
            return True
        except:
            return False

    def read(self) -> Union[str,bool]:
        """Reads File

        :return: What is stored in the file
        :rtype: Union[str,bool]
        """
        try:
            # Reads the file
            with open(self.directory) as file:
                data = file.read()
            return data
        except:
            return False

    def write(self, data:str) -> bool:
        """Writes to the data to the File

        :param data: Data to add to File
        :type data: str
        :return: `True` if the File was wrote, `False` if the File did not Write
        :rtype: bool
        """
        try:
            with open(self.directory) as file:
                file.write(data)
            return True
        except:
            return False
      
    def rename(self, name:str) -> bool:
        """Renames the File

        :param name: New Name to rename the File
        :type name: str
        :return: `True` File name was Changed, `False` File name did not Change
        :rtype: bool
        """
        try:
            # Directory List
            directoryList = self.directory.split("/")
            
            # File Type
            fileType = directoryList[-1].split(".")[-1]
            directory = "/".join(directoryList) + name + fileType
            
            # Rename File
            os.rename(self.directory, directory)
            self.directory = directory
            
            return True
        except:
            return False
             
    def move(self, newDirectory:str) -> bool:
        """Moves file to another Location with File in it

        :param newDirectory: New Directory Location
        :type newDirectory: str
        :return: `True` If the File was moved, `False` File not Moved
        :rtype: bool
        """
        try:
            os.rename(self.directory, newDirectory)
            self.directory = newDirectory
            
            return True
        except:
            return False
    
    def __str__(self)-> str:
        """String of the Directory

        :return: Directory of the File
        :rtype: str
        """
        if self.directory is None: return "No Directory Available"
        return self.directory

# TXT File Object
class TXT(File):
    def __init__(self, directory:str = f"{os.path.dirname(os.path.abspath(__file__))}/new.txt") -> None:
        """Txt File Object

        :param directory: Directory of TXT File, defaults to f"{os.path.dirname(os.path.abspath(__file__))}/new.txt"
        :type directory: str, optional
        """
        super().__init__(directory) 

# JSON File Object
class JSON(File):
    def __init__(self, directory:str = f"{os.path.dirname(os.path.abspath(__file__))}/new.json") -> None:
        """JSON File Object

        :param directory: Directory of JSON, defaults to f"{os.path.dirname(os.path.abspath(__file__))}/new.json"
        :type directory: str, optional
        """
        super().__init__(directory)

    @staticmethod
    def create(directory:str) -> bool:
        """Create JSON File

        :param directory: Directory of JSON File
        :type directory: str
        :return: `True` File is Created, `False` File is Not Created
        :rtype: bool
        """
        try:
            if not JSON.exists(directory):
                with open(directory,'x') as file:
                    file.close()
                with open(directory, "w") as file:
                    json.dump({}, file, indent = 6)
                return True
            return False
        except:
            return False

    def read(self) -> Union[dict,bool]:
        """Read JSON File

        :return: Dict of the JSON, `False` Not Reads File
        :rtype: Union[dict,bool]
        """
        try:
            with open(self.directory, "r") as file:
                data = json.load(file)
            return data
        except:
            return False

    def write(self, data:dict) -> bool:
        """Writes to JSON File

        :param data: Data to write to JSON File
        :type data: dict
        :return: `True` if the JSON is written to, `False` if the JSON did not write
        :rtype: bool
        """
        try:
            with open(self.directory, "w") as file:
                json.dump(data, file, indent = 6)
            return True
        except:
            return False

# CSV File Object
class CSV(File):
    def __init__(self, directory:str =f"{os.path.dirname(os.path.abspath(__file__))}/new.csv") -> None:
        """CSV File Object

        :param directory: Directory of CSV File, defaults to f"{os.path.dirname(os.path.abspath(__file__))}/new.csv"
        :type directory: str, optional
        """
        super().__init__(directory)

    def read(self) -> Union[pd.DataFrame,bool]:
        """Reads in CSV File 

        :return: pd.DataFrame of the CSV File, `False` File was not read
        :rtype: Union[pd.DataFrame,bool]
        """
        try:
            df= pd.read_csv(self.directory)
            return df.loc[:, ~df.columns.str.contains('^Unnamed')]
        except:
            return False

    def write(self, df:pd.DataFrame) -> bool:
        try:
            df.to_csv(self.directory)
            return True
        except:
            return False

    def append(self, df:Union[pd.DataFrame,pd.Series]) -> bool:
        try:
            if isinstance(df,pd.DataFrame):
                self.write(pd.concat([self.read(),df],ignore_index=True))
            elif isinstance(df,pd.Series):
                self.write(pd.concat([self.read(),df.to_frame()],axis=1))
            return True
        except:
            return False

# Folder Object
class Folder:
    def __init__(self, directory:str = f"{os.path.dirname(os.path.abspath(__file__))}/new/") -> None:
        """File object to help manipulate files with ease.

        :param directory: Directory of the File, defaults to f"{os.path.dirname(os.path.abspath(__file__))}/new/"
        :type directory: str, optional
        """
        # Directory of File
        self.directory = directory
        
        # Creates File if Does Not Exist
        if not self.exists(self.directory): self.create(self.directory)
    
    @staticmethod
    def exists(directory:str) -> bool:
        """Check File Existance

        :param directory: Directory of the File
        :type directory: str
        :return: `True` File Exists and `False` File Does Not Exist
        :rtype: bool
        """
        try:
            return os.path.isdir(directory)
        except:
            return False

    @staticmethod
    def create(directory:str) -> bool:
        """Create a New File

        :param directory: Directory of File
        :type directory: str
        :return: `True` if File is Created, `False` if File is Not Created
        :rtype: bool
        """
        try:
            os.makedirs(directory)
            return True
        except:
            return False
        
    def delete(self) -> bool:
        """Delete File that Exists

        :return: `True` If File is Deleted, `False` If File is Not Deleted
        :rtype: bool
        """
        try:
            # Deletes the File
            os.remove(self.directory)
            
            # Sets Directory to None
            self.directory = None
            return True
        except:
            return False
   
    def rename(self, name:str) -> bool:
        """Renames the File

        :param name: New Name to rename the File
        :type name: str
        :return: `True` File name was Changed, `False` File name did not Change
        :rtype: bool
        """
        try:
            # Directory List
            directoryList = self.directory.split("/")[:-1]
            
            # File Type
            directory = "/".join(directoryList) + name
            
            # Rename File
            os.rename(self.directory, directory)
            self.directory = directory
            
            return True
        except:
            return False
             
    def move(self, newDirectory:str) -> bool:
        """Moves file to another Location with File in it

        :param newDirectory: New Directory Location
        :type newDirectory: str
        :return: `True` If the File was moved, `False` File not Moved
        :rtype: bool
        """
        try:
            os.rename(self.directory, newDirectory)
            self.directory = newDirectory
            
            return True
        except:
            return False
    
    def add(self, new):
        pass
    
    
    def __str__(self)-> str:
        """String of the Directory

        :return: Directory of the File
        :rtype: str
        """
        if self.directory is None: return "No Directory Available"
        return self.directory



