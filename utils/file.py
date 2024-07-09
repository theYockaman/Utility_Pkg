
# Module Documentation
"""
File Objects: Easy to manipulate Files: TXT, JSON, CSV, and Folder.
"""

# Imported Modules
import os, json, pandas, abc
from joblib import dump, load
import pathlib
import shutil

__all__ = [
    "File"
    , "TXT"
    , "JSON"
    , "CSV"
    , "BIN"
    , "Folder"
    , "LOCAL_DIRECTORY"
]

# Local Directory from Main Functions
LOCAL_DIRECTORY = pathlib.Path().resolve()

# Inital File Object to Base around Specific Files
class File:
    def __init__(self, directory:str = None, extIntent:str = "txt", creation:bool = True) -> None:
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
        
        # Create Local Directory
        if "/" not in directory: directory = f"{LOCAL_DIRECTORY}/{directory}"
        
        # Intialize directory variable 
        self._directory = directory
        
        # Create the File
        if creation is True and not self.exists():
            self.create()
        
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
    def create(self) -> None:
        """Create the File Object

        :raises FileExistsError: File Already Exists
        """
        
        # Setup Directory to the Object's Directory
        if self.exists(): raise FileExistsError("File Already Exists")
        
        # Creates the File
        with open(self.directory,"x"):
            pass
     
    def delete(self) -> None:
        """Delete File Object

        :raises FileNotFoundError:
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
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
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
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
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
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
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
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
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
        # Rename the Directory
        os.rename(self._directory, newDirectory)
        
        # Setup Directory to the Object's Directory
        self._directory = newDirectory
    
    def copy(self, newDirectory:str) -> str:
        """Copy File

        :param newDirectory: Location for New File
        :type newDirectory: str
        :return: Directory of File
        :rtype: str
        """
        f = File(newDirectory,self.extension)
        f.write(self.read())
        
        return newDirectory
        
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
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
        return self.directory

# TXT File Object
class TXT(File):
    def __init__(self, directory:str = None, creation:bool = True) -> None:
        """Text File Object

        :param directory: Text File Directory, defaults to None
        :type directory: str, optional
        """
        super().__init__(directory,"txt", creation) 

# JSON File Object
class JSON(File):
    def __init__(self, directory:str = None, creation:bool = True) -> None:
        """JSON File Object

        :param directory: JSON File Directory, defaults to None
        :type directory: str, optional
        """
        
        super().__init__(directory,"json",creation)

    def create(self) -> None:
        """Create JSON File

        :param directory: JSON File Directory, defaults to None
        :type directory: str, optional
        :raises ValueError: No Directory
        """
        
        # Setup Directory to the Object's Directory
        if self.exists(): raise FileExistsError("File Already Exists")
        
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
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
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
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
        # Write to JSON File
        with open(self.directory, "w") as file:
            json.dump(data, file, indent = 6)

# CSV File Object
class CSV(File):
    def __init__(self, directory:str = None, creation:bool = True) -> None:
        """CSV File Object

        :param directory: CSV File Directory, defaults to None
        :type directory: str, optional
        """
        
        super().__init__(directory, "csv",creation)

    def read(self) -> pandas.DataFrame:
        """CSV Read File

        :raises ValueError: No Directory
        :raises TypeError: Directory is not a `str`
        :return: CSV File Data
        :rtype: pandas.DataFrame
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
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
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
        # Write to CSV
        df.to_csv(self.directory, index=True)

# Bin File Object
class BIN(File):
    def __init__(self, directory:str = None, creation:bool = True) -> None:
        """BIN File Object

        :param directory: BIN File Directory, defaults to None
        :type directory: str, optional
        """
        
        super().__init__(directory, "bin", creation)

    def read(self):
        """BIN Read File

        :raises ValueError: No Directory
        :raises TypeError: Directory is not a `str`
        :return: BIN File Data
        :rtype: pandas.DataFrame
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
        return load(self.directory)
    
    def write(self, obj:object) -> None:
        """Write to BIN File Data

        :param obj: Class or Object that you want to save for later
        :type df: object
        :raises ValueError: No Directory
        """
        # Setup Directory to the Object's Directory
        if not self.exists(): raise FileExistsError("File Does Not Exists")
        
        # Write to BIN
        dump(obj, self.directory, True)

 
# Folder Object
class Folder:
    def __init__(self, directory:str = None, creation:bool = True) -> None:
        """Folder Object

        :param directory: Folder Directory, defaults to None
        :type directory: str, optional
        """
        # Directory of File
        if directory is None: directory = f"{LOCAL_DIRECTORY}/new"
        
        # Create Local Directory
        if "/" not in directory: directory = f"{LOCAL_DIRECTORY}/{directory}"
        
        # Set Directory Variable
        self._directory = directory
        
        # Create the Directory
        if creation is True and not self.exists():
            self.create()
         
    @property
    def directory(self) -> str:
        return self._directory
    
    @property
    def content(self) -> list[str]:
        """Content in the Folder

        :return: Content in the Folder
        :rtype: list[str]
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise ValueError("Directory Does Not Exists")
        
        return [f"{self.directory}/{f}" for f in os.listdir(self.directory)]
    
    def exists(self) -> bool:
        """Checks Existance of the Folder

        :raises ValueError: No Directory
        :return: `True` Folder Exists, `False` Folder Does Not Exist
        :rtype: bool
        """
        # Setup Directory to the Object's Directory
        if self._directory is None: return False
        
        return os.path.isdir(self._directory)

    def create(self) -> None:
        """Create the Folder 

        :raises ValueError: No Directory
        """
        
        # Setup Directory to the Object's Directory
        if self.exists(): raise ValueError("Directory already Exists")
        
        try:
            os.makedirs(self.directory)
        except FileExistsError:
            pass
        
    def delete(self) -> None:
        """Delete Folder

        :raises ValueError: No Directory
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise ValueError("Directory Does Not Exists")
        
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
        if self.exists(): raise ValueError("Directory Does Not Exists")
        
        # Directory List
        directoryList = self._directory.split("/")[:-1]
        
        # File Type
        directory = "/".join(directoryList) +"/"+ name
        
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
        if not self.exists(): raise ValueError("Directory Does Not Exists")
        
        
        os.rename(self._directory, newDirectory)
        self._directory = newDirectory
    
    def fileExist(self, name:str) -> bool:
        """Check File Exists in Folder

        :param name: Name of File with Extension
        :type name: str
        :return: `True` file is in folder, `False` file is not in folder
        :rtype: bool
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists(): raise ValueError("Directory Does Not Exists")
        
        return os.path.isfile(self.directory+"/"+name) 
    
    def copy(self, newDirectory:str) -> str:
        Folder(newDirectory)

        for x in self.content:
            if os.path.isfile(x):
                file = File(x)
                file.copy(f"{newDirectory}/{file.name}.{file.extension}")
            else:
                folder = Folder(x)
                folder.copy(f"{newDirectory}/{folder.name}")
                
    @property
    def name(self) -> str:
        return self.directory.split("/")[-1]
    
    def __str__(self)-> str:
        """Folder String

        :return: Folder Directory
        :rtype: str
        """
        # Setup Directory to the Object's Directory
        if  not self.exists(): raise ValueError("Directory Does Not Exists")
        
        return self.directory
