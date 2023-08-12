# Imported Modules
import os
import json
import pandas as pd
from abc import abstractmethod

# Inital File Object to Base around Specific Files
class File:
    def __init__(self, directory:str = None) -> None:
        """File Object to easily manipulate files

        :param directory: File Directory, defaults to None
        :type directory: str, optional
        """
        
        # Directory of File
        if directory is None: directory = f"{os.path.dirname(os.path.abspath(__file__))}/new.txt"
        self.directory = directory
        
        # Creates File if Does Not Exist
        if not self.exists(self.directory): self.create(self.directory)
    
    def exists(self, directory:str = None) -> bool:
        """Checks if File Exists

        :param directory: File Directory, defaults to None
        :type directory: str, optional
        :return: `True` File Exists, `False` File Does Not Exist
        :rtype: bool
        """
        if directory is None: self.directory
        return os.path.isfile(directory)

    @abstractmethod
    def create(self, directory:str = None) -> None:
        """Creates File

        :param directory: File Directory, defaults to None
        :type directory: str, optional
        """
        if directory is None: directory = self.directory
        with open(directory,"x"):
            pass
     
    def delete(self, directory:str = None) -> None:
        """Deletes File

        :param directory: File Directory, defaults to None
        :type directory: str, optional
        """
        if directory is None: 
            directory = self.directory
            self.directory = None
        
        # Deletes the File
        os.remove(directory)
              
    @abstractmethod
    def read(self) -> str:
        """Read File

        :return: Content in File
        :rtype: str
        """
        # Reads the file
        with open(self.directory) as file:
            data = file.read()
        return data

    @abstractmethod
    def write(self, data:str) -> None:
        """Write Data to File

        :param data: Data to Write
        :type data: str
        """
        with open(self.directory) as file:
            file.write(data)
      
    def rename(self, name:str) -> None:
        """Rename the File

        :param name: New File Name
        :type name: str
        """
        # Directory List
        directoryList = self.directory.split("/")
        
        # File Type
        fileType = directoryList[-1].split(".")[-1]
        directory = "/".join(directoryList) + name + fileType
        
        # Rename File
        os.rename(self.directory, directory)
        self.directory = directory
             
    def move(self, newDirectory:str) -> None:
        """Move File to new location

        :param newDirectory: New File Directory
        :type newDirectory: str
        """
        os.rename(self.directory, newDirectory)
        self.directory = newDirectory
    
    def __str__(self)-> str:
        """File String

        :return: Directory of File
        :rtype: str
        """
        if self.directory is None: return "No Directory Available"
        return self.directory

# TXT File Object
class TXT(File):
    def __init__(self, directory:str = None) -> None:
        """Text File Object

        :param directory: Text File Directory, defaults to None
        :type directory: str, optional
        """
        super().__init__(directory) 

# JSON File Object
class JSON(File):
    def __init__(self, directory:str = None) -> None:
        """Json File Object

        :param directory: Json File Directory, defaults to None
        :type directory: str, optional
        """
        
        if directory is None: f"{os.path.dirname(os.path.abspath(__file__))}/new.json"
        super().__init__(directory)

    def create(self, directory:str = None) -> None:
        """Create Json File

        :param directory: Json File Directory, defaults to None
        :type directory: str, optional
        """
        if directory is None: directory = self.directory
            
        with open(directory,'x') as file:
            file.close()
            
        with open(directory, "w") as file:
            json.dump({}, file, indent = 6)

    def read(self) -> dict:
        """Read Content of Json File

        :return: Json Content
        :rtype: dict
        """
        with open(self.directory, "r") as file:
            data = json.load(file)
        return data

    def write(self, data:dict) -> None:
        """Write to Json File

        :param data: Data to write to Json File
        :type data: dict
        """
        with open(self.directory, "w") as file:
            json.dump(data, file, indent = 6)

# CSV File Object
class CSV(File):
    def __init__(self, directory:str = None) -> None:
        """Csv File Object

        :param directory: Csv File Directory, defaults to None
        :type directory: str, optional
        """
        if directory is None: directory = f"{os.path.dirname(os.path.abspath(__file__))}/new.csv"
        super().__init__(directory)

    def read(self) -> pd.DataFrame:
        """Read Csv File

        :return: Conent of Csv
        :rtype: pd.DataFrame
        """
        df = pd.read_csv(self.directory)
        return df.loc[:, ~df.columns.str.contains('^Unnamed')]

    def write(self, df:pd.DataFrame) -> None:
        """Write to Csv File

        :param df: Content to Write
        :type df: pd.DataFrame
        """
        df.to_csv(self.directory)

# Folder Object
class Folder:
    def __init__(self, directory:str = None) -> None:
        """Folder Object

        :param directory: Folder Directory, defaults to None
        :type directory: str, optional
        """
        # Directory of File
        if directory is None: directory = f"{os.path.dirname(os.path.abspath(__file__))}/new/"
        self.directory = directory
        
        # Creates File if Does Not Exist
        if not self.exists(self.directory): self.create(self.directory)
    
    def exists(self, directory:str = None) -> bool:
        """Checks if the Folder exists

        :param directory: Folder Directory, defaults to None
        :type directory: str, optional
        :return: `True` Folder Exists, `False` Folder Does Not Exist
        :rtype: bool
        """
        if directory is None: directory = self.directory
        return os.path.isdir(directory)

    def create(self, directory:str = None) -> None:
        """Create Folder

        :param directory: Folder Directory, defaults to None
        :type directory: str, optional
        """
        if directory is None: directory = self.directory
        os.makedirs(directory)
        
    def delete(self, directory:str = None) -> None:
        """Delete Folder

        :param directory: Folder Directory, defaults to None
        :type directory: str, optional
        """
        if directory is None: directory = self.directory
        
        # Deletes the File
        os.remove(directory)
        
        # Sets Directory to None
        self.directory = None
   
    def rename(self, name:str) -> None:
        """Rename Folder

        :param name: New Folder Name
        :type name: str
        """
        # Directory List
        directoryList = self.directory.split("/")[:-1]
        
        # File Type
        directory = "/".join(directoryList) + name
        
        # Rename File
        os.rename(self.directory, directory)
        self.directory = directory
             
    def move(self, newDirectory:str) -> None:
        """Move Folder

        :param newDirectory: New Folder Directory
        :type newDirectory: str
        """
        os.rename(self.directory, newDirectory)
        self.directory = newDirectory
    
    def __str__(self)-> str:
        """Folder String

        :return: Folder Directory
        :rtype: str
        """
        if self.directory is None: return "No Directory Available"
        return self.directory



