
# Module Documentation
"""
File Objects: Easy to manipulate Files: TXT, JSON, CSV, and Folder.
"""

# Imported Modules
import os, json, pandas, abc
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
    def __init__(self, directory:str = None, extIntent:str = "txt") -> None:
        """File Object

        :param directory: Directory of the File, defaults to None
        :type directory: str, optional
        :raises TypeError: Directory is not a `str`
        """
        
        # Intended Extension
        self._extIntent = extIntent
        
        # Directory of File
        
        # Create a File if None
        if directory is None: directory = f"{LOCAL_DIRECTORY}/new.{extIntent}"
        
        # Check Directory Type
        checkType([directory],[str])
        
        # Create Local Directory
        if "/" not in directory: directory = f"{LOCAL_DIRECTORY}/{directory}"
        
        # Intialize directory variable 
        self._directory = directory
        
        # Check if File Directory is the Correct Type
        if not self.isType(): raise TypeError("Directory Not Correct Extension")
        
        # Creates File if Does Not Exist
        if not self.exists(): self._create()
        
    def isType(self) -> bool:
        """Check File Extension make Sure it is Correct

        :return:`True` Type is Correct, `False` Type is not Correct
        :rtype: bool
        """
        if self.extension != self._extIntent:
            return False
        return True
        
    def exists(self) -> bool:
        """Checks Existence of the File Object

        :return: `True` if the File Exists, `False` if the File Does Not Exist
        :rtype: bool
        """
        
        # Setup Directory to the Object's Directory
        if self._directory is None: return False
        
        # Checks if file exists
        return os.path.isfile(self._directory)

    @abc.abstractmethod
    def _create(self) -> None:
        """Create the File Object

        :raises FileExistsError:
        """
        
        # Setup Directory to the Object's Directory
        if self.exists(): raise FileExistsError()
        
        # Creates the File
        with open(self.directory,"x"):
            pass
     
    def delete(self) -> None:
        """Delete File Object

        :raises FileNotFoundError:
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise FileNotFoundError()
        
        # Deletes the File
        os.remove(self._directory)
        
        # Clear Directory
        self._directory = None
              
    @abc.abstractmethod
    def read(self) -> str:
        """Read the File Object

        :raises FileNotFoundError:
        :return: Value Read from File Object
        :rtype: str
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise FileNotFoundError()
        
        # Reads the file
        with open(self.directory) as file:
            data = file.read()
            
        return data

    @abc.abstractmethod
    def write(self, data:str) -> None:
        """Write to File Object

        :param data: Data to write to the File
        :type data: str
        :raises FileNotFoundError:
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise FileNotFoundError()
        
        # Check Directory Type
        checkType([data],[str])
        
        # Writes to the file or input value into file
        with open(self.directory,"w") as file:
            file.write(data)
      
    def rename(self, name:str) -> None:
        """Rename the File Object

        :param name: New Name for the File Object
        :type name: str
        :raises FileNotFoundError:
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise FileNotFoundError()
        
        # Check Directory Type
        checkType([name],[str])
        
        directoryList = self.directory.split("/")
        
        # File Type
        newDirectory = "/".join(directoryList[:-1])+"/" + name + '.' +self.extension
        
        if newDirectory[0] == "/": newDirectory = newDirectory
        
        # Rename File
        os.rename(self.directory, newDirectory)
        
        # Setup Directory to the Object's Directory
        self._directory = newDirectory
              
    def move(self, newDirectory:str) -> None:
        """Move File Object to a new Location

        :param newDirectory: New Directory in Location
        :type newDirectory: str
        :raises FileNotFoundError:
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise FileNotFoundError()
        
        # Check Directory Type
        checkType([newDirectory],[str])
        
        # Rename the Directory
        os.rename(self._directory, newDirectory)
        
        # Setup Directory to the Object's Directory
        self._directory = newDirectory
    
    @property
    def directory(self) -> str:
        """Directory of the File

        :return: Directory of the File
        :rtype: str
        """
        return self._directory
    
    @property
    def extension(self) -> str:
        """File Object Extension

        :return: File Object Extension
        :rtype: str
        """
        directoryList = self._directory.split("/")
        return directoryList[-1].split(".")[-1]
    
    @property
    def name(self) -> str:
        """Name of the File Object

        :return: Name of the File Object
        :rtype: str
        """
        return self.directory.split("/")[-1].split(".")[0]
    
    def __str__(self)-> str:
        """Directory of the File Object

        :return: Directory of the File Object
        :rtype: str
        """
        
        # Fill in No Directory
        if self.directory is None: return "No Directory Avaliable"
        
        return self.directory

# TXT File Object
class TXT(File):
    def __init__(self, directory:str = None) -> None:
        """Text File Object

        :param directory: Text File Directory, defaults to None
        :type directory: str, optional
        """
        super().__init__(directory,"txt") 

# JSON File Object
class JSON(File):
    def __init__(self, directory:str = None) -> None:
        """JSON File Object

        :param directory: JSON File Directory, defaults to None
        :type directory: str, optional
        """
        
        super().__init__(directory,"json")

    def _create(self) -> None:
        """Create JSON File

        :param directory: JSON File Directory, defaults to None
        :type directory: str, optional
        :raises ValueError: No Directory
        """
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
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
        :raises ValueError: No Directory
        :return: JSON File Data
        :rtype: dict
        """
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Reading in the Data
        with open(self.directory, "r") as file:
            data = json.load(file)
            
        return data

    def write(self, data:dict) -> None:
        """Write to JSON File

        :param data: New JSON File Data
        :type data: dict
        :param directory: Directory of the JSON File, defaults to None
        :type directory: str, optional
        :raises TypeError: Directory is not a `str`
        """
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Parameter Types
        checkType([data],[dict])
        
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
        
        super().__init__(directory, "csv")

    def read(self) -> pandas.DataFrame:
        """CSV Read File

        :raises ValueError: No Directory
        :raises TypeError: Directory is not a `str`
        :return: CSV File Data
        :rtype: pandas.DataFrame
        """
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Get Dataframe
        try:
            df = pandas.read_csv(self.directory,index_col=0)
            
        except pandas.errors.EmptyDataError:
            df = pandas.DataFrame()
        
        # Return Dataframe of the CSV Data
        return df

    def write(self, df:pandas.DataFrame) -> None:
        """Write to CSV File Data

        :param df: Dataframe to write CSV
        :type df: pandas.DataFrame
        :raises ValueError: _description_
        :raises TypeError: _description_
        """
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Parameter Types
        checkType([df],[pandas.DataFrame])
        
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
        
        # Check Directory Type
        checkType([directory],[str])
        
        # Set Directory Variable
        self._directory = directory
        
        # Creates File if Does Not Exist
        if not self.exists(): self._create()
    
    @property
    def directory(self) -> str:
        return self._directory
    
    @property
    def files(self) -> list[File]:
        """Files in the Folder

        :return: Files in the Folder
        :rtype: list[File]
        """
        
        return [File(f"{LOCAL_DIRECTORY}/{f}") for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]
    
    def exists(self) -> bool:
        """Checks Existance of the Folder

        :raises ValueError: No Directory
        :return: `True` Folder Exists, `False` Folder Does Not Exist
        :rtype: bool
        """
        # Setup Directory to the Object's Directory
        if self._directory is None: return False
        
        return os.path.isdir(self._directory)

    def _create(self) -> None:
        """Create the Folder 

        :raises ValueError: No Directory
        """
        
        # Setup Directory to the Object's Directory
        if self.exists(): raise ValueError("Directory already")
        
        try:
            os.makedirs(self.directory)
        except FileExistsError:
            pass
        
    def delete(self) -> None:
        """Delete Folder

        :raises ValueError: No Directory
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise ValueError("No Directory")
        
        # Deletes the File
        shutil.rmtree(self.directory)
        
        # Sets Directory to None
        self._directory = None
   
    def rename(self, name:str) -> None:
        """Rename the Folder

        :param name: New Name of the Folder
        :type name: str
        :raises ValueError: No Directory
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise ValueError("No Directory")
        
        # Check Name Type
        checkType([name],[str])
        
        # Directory List
        directoryList = self._directory.split("/")[:-1]
        
        # File Type
        directory = "/".join(directoryList) + name
        
        # Rename File
        os.rename(self._directory, directory)
        self._directory = directory
             
    def move(self, newDirectory:str) -> None:
        """Move File to new location

        :param newDirectory: New Directory to move file too
        :type newDirectory: str
        :raises ValueError: No Directory
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise ValueError("No Directory")
        
        # Check Directory Type
        checkType([newDirectory],[str])
        
        os.rename(self._directory, newDirectory)
        self._directory = newDirectory
    
    def fileExist(self, name:str) -> bool:
        """Check File Exists in Folder

        :param name: Name of File with Extension
        :type name: str
        :return: `True` file is in folder, `False` file is not in folder
        :rtype: bool
        """
        # Check Name Parameter
        checkType([name],[str])
        
        return os.path.isfile(self.directory+"/"+name) 
    
    def __str__(self)-> str:
        """Folder String

        :return: Folder Directory
        :rtype: str
        """
        if self.directory is None: return "No Directory Available"
        return self.directory
