
# Module Documentation
"""
File Objects (OOO): Easy to manipulate 
"""

# Imported Modules
import os, json, pandas, abc, csv
from .functions import checkType
import pathlib
import shutil

__all__ = [
    "File"
    , "TXT"
    , "JSON"
    , "CSV"
    , "Folder"
    , "LOCAL_DIRECTORY"
]

# Local Directory from Main Functions
LOCAL_DIRECTORY = pathlib.Path().resolve()

# Inital File Object to Base around Specific Files
class File:
    def __init__(self, directory:str = None) -> None:
        """File Object to help Manipulate Files with Ease

        :param directory: Directory of File, defaults to None
        :type directory: str, optional
        :raises TypeError: Directory is not a `str`
        """
        
        # Directory of File
        if directory is None: directory = f"{LOCAL_DIRECTORY}/new.txt"
        
        # Local Directory File
        if "/" not in directory: directory = f"{LOCAL_DIRECTORY}/{directory}"
        
        
        # Check Parameter Types
        checkType({directory:str},True)
            
        # Intialize directory variable 
        self.directory = directory
        
        # Creates File if Does Not Exist
        if not self.exists(): self._create()
    
    def exists(self) -> bool:
        """Checks if File Exists

        :return: If File exists `True`, If File Does Not Exist `False`
        :rtype: bool
        """
        
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        # Checks if file exists
        return os.path.isfile(self.directory)

    @abc.abstractmethod
    def _create(self) -> None:
        """Create the File under the File Object

        """
        
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        # Creates the File
        with open(self.directory,"x"):
            pass
     
    def delete(self) -> None:
        """Delete the File

        """
        
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        # Deletes the File
        os.remove(self.directory)
        
        self.directory = None
              
    @abc.abstractmethod
    def read(self) -> str:
        """Reads in File's Contents

        :return: Content from File
        :rtype: str
        """
        
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        # Reads the file
        with open(self.directory) as file:
            data = file.read()
            
        return data

    @abc.abstractmethod
    def write(self, data:str) -> None:
        """Write to File

        :param data: Data to add to File
        :type data: str
        """
        
        # Check Parameter Types
        checkType({self.directory:str,data:str},True)
        
        # Writes to the file or input value into file
        with open(self.directory,"w") as file:
            file.write(data)
      
    def rename(self, name:str) -> None:
        """Rename the File

        :param name: New Name for File
        :type name: str
        """
        
        # Check Parameter Types
        checkType({self.directory:str,name:str},True)
      
        # Create Directory List  
        directoryList = self.directory.split("/")
        
        # File Type
        newDirectory = "/"+"/".join(directoryList[:-1])+"/" + name + '.' +self.extension
        
        if newDirectory[0] == "/": newDirectory = newDirectory[1:]
        
        # Rename File
        os.rename(self.directory, newDirectory)
        
        # Setup Directory to the Object's Directory
        self.directory = newDirectory
              
    def move(self, newDirectory:str) -> None:
        """Move file to a new Directory

        :param newDirectory: New Directory with file name and extension
        :type newDirectory: str
        """
        
        # Check Parameter Types
        checkType({self.directory:str, newDirectory:str},True)
        
        # Rename the Directory
        os.rename(self.directory, newDirectory)
        
        # Setup Directory to the Object's Directory
        self.directory = newDirectory
    
    @property
    def extension(self) -> str:
        """File Extension

        :return: File Extension
        :rtype: str
        """
        
        checkType({self.directory:str},True)
        
        directoryList = self.directory.split("/")
        return directoryList[-1].split(".")[-1]
    
    def __str__(self)-> str:
        """File Directory

        :return: File Directory
        :rtype: str
        """
        
        # Fill in No Directory
        if self.directory is None: return "No Directory Avaliable"
        
        return str(self.directory)

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
        """JSON File Object

        :param directory: JSON File Directory, defaults to None
        :type directory: str, optional
        """
        
        # Setup a New File
        if directory is None: f"{LOCAL_DIRECTORY}/new.json"
        
        super().__init__(directory)

    def _create(self) -> None:
        """Create JSON File

        :param directory: JSON File Directory, defaults to None
        :type directory: str, optional
        """
        
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        # Create a JSON File 
        with open(self.directory,'x') as file:
            file.close()
            
        # Make the JSON File Empty
        with open(self.directory, "w") as file:
            json.dump({}, file, indent = 6)

    def read(self) -> dict:
        """Read in JSON File

        :param directory: Directory of JSON File, defaults to None
        :type directory: str, optional
        :return: JSON File Data
        :rtype: dict
        """
        
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        # Reading in the Data
        with open(self.directory, "r") as file:
            data = json.load(file)
            
        return data

    def write(self, data:dict) -> None:
        """Write to JSON File

        :param data: New JSON File Data
        :type data: dict
        """
        
        # Check Parameter Types
        checkType({self.directory:str,data:dict},True)
        
        # Write to JSON File
        with open(self.directory, "w") as file:
            json.dump(data, file, indent = 6)

# CSV File Object
class CSV(File):
    def __init__(self, directory:str = None) -> None:
        """CSV File Object

        :param directory: CSV File Directory, defaults to None
        :type directory: str, optional
        """
        
        # Setup a New File
        if directory is None: directory = f"{LOCAL_DIRECTORY}/new.csv"
        
        super().__init__(directory)

    def read(self) -> pandas.DataFrame:
        """Read in CSV Data

        :return: CSV Data
        :rtype: pandas.DataFrame
        """
        
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        # Get Dataframe
        try:
            df = pandas.read_csv(self.directory,index_col=0)
            
        except pandas.errors.EmptyDataError:
            df = pandas.DataFrame()
        
        # Return Dataframe of the CSV Data
        return df

    def write(self, df:pandas.DataFrame) -> None:
        """Write to CSV

        :param df: Dataframe of Info to Write
        :type df: pandas.DataFrame
        """
        
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        # Write to CSV
        df.to_csv(self.directory, index=True)
        
# Folder Object
class Folder:
    def __init__(self, directory:str = None) -> None:
        """Folder Object

        :param directory: Folder Directory, defaults to None
        :type directory: str, optional
        """
        # Directory of File
        if directory is None: directory = f"{LOCAL_DIRECTORY}/new"
        
        # Local Directory
        if "/" not in directory: directory = f"{LOCAL_DIRECTORY}/{directory}"
        
        # Set Directory Variable
        self.directory = directory
        
        # Creates File if Does Not Exist
        if not self.exists(): self._create()
    
    def exists(self) -> bool:
        """Check Existance of the Folder

        :return: _description_
        :rtype: bool
        """
        
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        return os.path.isdir(self.directory)

    def _create(self) -> None:
        """Create Folder for Object
        """
        
       # Check Parameter Types
        checkType({self.directory:str},True)
        
        # Creates File
        try:
            os.makedirs(self.directory)
        except FileExistsError:
            pass
        
    def delete(self) -> None:
        """Delete Folder Object
        """
        
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        # Deletes the File
        shutil.rmtree(self.directory)
        
        # Sets Directory to None
        self.directory = None
   
    def rename(self, name:str) -> None:
        """Rename Folder

        :param name: New Name of Folder
        :type name: str
        """
        
        # Check Parameter Types
        checkType({self.directory:str, name:str},True)
        
        # Directory List
        directoryList = self.directory.split("/")[:-1]
        
        # File Type
        directory = "/"+"/".join(directoryList) + name
        
        # Rename File
        os.rename(self.directory, directory)
        self.directory = directory
             
    def move(self, newDirectory:str) -> None:
        """Move Folder from one Directory to another

        :param newDirectory: New Directory with Name of Current Folder
        :type newDirectory: str
        """
        
        # Check Parameter Types
        checkType({self.directory:str, newDirectory:str},True)
        
        os.rename(self.directory, newDirectory)
        self.directory = newDirectory
    
    def fileExist(self, name:str) -> bool:
        """Check File Exist in Folder

        :param name: File Name with Extension
        :type name: str
        :return: `True` if the File Exists, `False` if the File Does Not Exist
        :rtype: bool
        """
        
        # Check Parameter Types
        checkType({self.directory:str, name:str},True)
        
        return os.path.isfile(self.directory+"/"+name) 
    
    def createFile(self, name:str) -> str:
        """Create File in Folder

        :param name: Name with Extension of the File
        :type name: str
        :return: File Directory
        :rtype: str
        """
        # Check Parameter Types
        checkType({self.directory:str, name:str},True)
        
        return File(f"{self.directory}/{name}").directory
    
    def createFolder(self, name:str) -> str:
        """Create Folder in Current Folder

        :param name: Name of the New Folder
        :type name: str
        :return: Directory of the New Folder Created
        :rtype: str
        """
        # Check Parameter Types
        checkType({self.directory:str, name:str},True)
        
        return Folder(f"{self.directory}/{name}").directory
    
    @property
    def files(self) -> list[str]:
        """Files in the Folder

        :return: File Directories
        :rtype: list[str]
        """
        
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        return [f"{LOCAL_DIRECTORY}/{f}" for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]
    
    @property
    def folders(self) -> list[str]:
        """Folders in the Current Folder

        :return: Folders Directories
        :rtype: list[str]
        """
        # Check Parameter Types
        checkType({self.directory:str},True)
        
        return [f"{LOCAL_DIRECTORY}/{f}" for f in os.listdir(self.directory) if os.path.isdir(os.path.join(self.directory, f))]
        
    def __str__(self)-> str:
        """Folder String

        :return: Folder Directory
        :rtype: str
        """
        if self.directory is None: return "No Directory Available"
        return self.directory
