
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
        
        # Directory of File
        if directory is None: directory = f"{LOCAL_DIRECTORY}/new.txt"
        
        if "/" in directory: directory = f"{LOCAL_DIRECTORY}/{directory}"
        
        # Check Directory Type
        if not checkType({directory:[str]}): raise TypeError("directory is not a `str`")
            
        # Intialize directory variable 
        self.directory = directory
        
        # Creates File if Does Not Exist
        if not self.exists(): self._create()
    
    def exists(self) -> bool:
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Directory Type
        if not checkType({self.directory:[str]}): raise TypeError("directory is not a `str`")
        
        # Checks if file exists
        return os.path.isfile(self.directory)

    @abc.abstractmethod
    def _create(self) -> None:
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Directory Type
        if not checkType({self.directory:[str]}): raise TypeError("directory is not a `str`")
        
        # Creates the File
        with open(self.directory,"x"):
            pass
     
    def delete(self) -> None:
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
            
        # Check Directory Type
        if not checkType({self.directory:[str]}): raise TypeError("directory is not a `str`")
        
        # Deletes the File
        os.remove(self.directory)
        
        self.directory = None
              
    @abc.abstractmethod
    def read(self) -> str:
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Directory Type
        if not checkType({self.directory:[str]}): raise TypeError("directory is not a `str`")
        
        # Reads the file
        with open(self.directory) as file:
            data = file.read()
            
        return data

    @abc.abstractmethod
    def write(self, data:str) -> None:
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Directory Type
        if not checkType({self.directory:[str], data:[str]}): raise TypeError("directory is not a `str`")
        
        # Writes to the file or input value into file
        with open(self.directory,"w") as file:
            file.write(data)
      
    def rename(self, name:str) -> None:
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Directory Type
        if not checkType({self.directory:[str],name:[str]}): raise TypeError("parameter is not a `str`")
        
        directoryList = self.directory.split("/")
        
        # File Type
        newDirectory = "/".join(directoryList[:-1])+"/" + name + '.' +self.extension
        if newDirectory[0] == "/": newDirectory = newDirectory[1:]
        
        # Rename File
        os.rename(self.directory, newDirectory)
        
        # Setup Directory to the Object's Directory
        self.directory = newDirectory
              
    def move(self, newDirectory:str) -> None:
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Directory Type
        if not checkType({self.directory:[str],newDirectory:[str]}): raise TypeError("directory is not a `str`")
        
        # Rename the Directory
        os.rename(self.directory, newDirectory)
        
        # Setup Directory to the Object's Directory
        self.directory = newDirectory
    
    @property
    def extension(self) -> str:
        directoryList = self.directory.split("/")
        return directoryList[-1].split(".")[-1]
    
    def __str__(self)-> str:
        
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
        :raises TypeError: Parameter Not Correct Type
        """
        
        # Check Parameter Types
        if not checkType({self.directory:[str]}):
            raise TypeError("Parameter Not Correct Type")
        
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
        :raises TypeError: Parameter Not Correct Type
        :return: JSON File Data
        :rtype: dict
        """
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Parameter Types
        if not checkType({self.directory:[str]}):
            raise TypeError("Parameter Not Correct Type")
        
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
        :raises TypeError: Parameter Not Correct Type
        """
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Parameter Types
        if not checkType({self.directory:[str]}):
            raise TypeError("Parameter Not Correct Type")
        
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
        
        
        # Check Parameter Types
        if not checkType({self.directory:[str]}):
            raise TypeError("Parameter Not Correct Type")
        
        # Get Dataframe
        try:
            df = pandas.read_csv(self.directory,index_col=0)
            
        except pandas.errors.EmptyDataError:
            df = pandas.DataFrame()
        
        # Return Dataframe of the CSV Data
        return df

    def write(self, df:pandas.DataFrame) -> None:
        """Write to CSV 

        :param df: Dataframe to Add to CSV
        :type df: pandas.DataFrame
        :param directory: CSV File Directory, defaults to None
        :type directory: str, optional
        :raises TypeError: Parameter Not Correct Type
        """
        
        
        # Check Parameter Types
        if not checkType({self.directory:[str]}):
            raise TypeError("Parameter Not Correct Type")
        
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
        
        # Set Directory Variable
        self.directory = directory
        
        # Creates File if Does Not Exist
        if not self.exists(): self.create()
    
    def exists(self) -> bool:
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Directory Type
        if not checkType({self.directory:[str]}): raise TypeError("directory is not a `str`")
        
        return os.path.isdir(self.directory)

    def create(self) -> None:
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        
        # Check Directory Type
        if not checkType({self.directory:[str]}): raise TypeError("directory is not a `str`")
        
        try:
            os.makedirs(self.directory)
        except FileExistsError:
            pass
        
    def delete(self) -> None:
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Directory Type
        if not checkType({self.directory:[str]}): raise TypeError("directory is not a `str`")
        
        # Deletes the File
        shutil.rmtree(self.directory)
        
        # Sets Directory to None
        self.directory = None
   
    def rename(self, name:str) -> None:
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Directory Type
        if not checkType({self.directory:[str]}): raise TypeError("directory is not a `str`")
        
        # Directory List
        directoryList = self.directory.split("/")[:-1]
        
        # File Type
        directory = "/".join(directoryList) + name
        
        # Rename File
        os.rename(self.directory, directory)
        self.directory = directory
             
    def move(self, newDirectory:str) -> None:
        
        # Setup Directory to the Object's Directory
        if self.directory is None: raise ValueError("No Directory")
        
        # Check Directory Type
        if not checkType({self.directory:[str]}): raise TypeError("directory is not a `str`")
        
        os.rename(self.directory, newDirectory)
        self.directory = newDirectory
    
    def fileExist(self, name:str) -> bool:
        return os.path.isfile(self.directory+"/"+name) 
    
    @property
    def files(self) -> list[File]:
        
        return [File(f"{LOCAL_DIRECTORY}/{f}") for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]
    
    def __str__(self)-> str:
        """Folder String

        :return: Folder Directory
        :rtype: str
        """
        if self.directory is None: return "No Directory Available"
        return self.directory



