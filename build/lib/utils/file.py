
# Module Documentation
"""
File Objects (OOO): Easy to manipulate 
"""

# Imported Modules
import os, json, pandas, abc
from .functions import checkType
import pathlib

__all__ = [
    "File"
    , "TXT"
    , "JSON"
    , "CSV"
    , "Folder"
    , "LOCAL_DIRECTORY"
]

LOCAL_DIRECTORY = pathlib.Path().resolve()

# Inital File Object to Base around Specific Files
class File:
    def __init__(self, directory:str = None) -> None:
        """File Object to easily manipulate files

        :param directory: File Directory, defaults to None
        :type directory: str, optional
        :raises TypeError: directory is not a `str`
        """
        
        # Directory of File
        if directory is None: directory = f"{LOCAL_DIRECTORY}/new.txt"
        
        # Check Directory Type
        if not checkType({directory:[str]}): raise TypeError("directory is not a `str`")
            
        # Intialize directory variable 
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
        # Setup Directory to the Object's Directory
        if directory is None: self.directory
        
        # Check Directory Type
        if not checkType({directory:[str]}): raise TypeError("directory is not a `str`")
        
        # Checks if file exists
        return os.path.isfile(directory)

    @abc.abstractmethod
    def create(self, directory:str = None) -> None:
        """Creates File

        :param directory: File Directory, defaults to None
        :type directory: str, optional
        """
        
        # Setup Directory to the Object's Directory
        if directory is None: directory = self.directory
        
        # Check Directory Type
        if not checkType({directory:[str]}): raise TypeError("directory is not a `str`")
        
        # Creates the File
        with open(directory,"x"):
            pass
     
    def delete(self, directory:str = None) -> None:
        """Deletes File

        :param directory: File Directory, defaults to None
        :type directory: str, optional
        """
        
        # Setup Directory to the Object's Directory
        if directory is None: 
            directory = self.directory
            self.directory = None
            
        # Check Directory Type
        if not checkType({directory:[str]}): raise TypeError("directory is not a `str`")
        
        # Deletes the File
        os.remove(directory)
              
    @abc.abstractmethod
    def read(self, directory:str = None) -> str:
        """Read File Data

        :param directory: Directory of File, defaults to None
        :type directory: str, optional
        :return: File Data
        :rtype: str
        """
        
        # Setup Directory to the Object's Directory
        if directory is None: directory = self.directory
        
        # Check Directory Type
        if not checkType({directory:[str]}): raise TypeError("directory is not a `str`")
        
        # Reads the file
        with open(directory) as file:
            data = file.read()
            
        return data

    @abc.abstractmethod
    def write(self, data:str, directory:str = None) -> None:
        """Write to Directory

        :param data: Info/Data to add to the file
        :type data: str
        :param directory: File Directory that writes too, defaults to None
        :type directory: str, optional
        """
        
        # Setup Directory to the Object's Directory
        if directory is None: directory = self.directory
        
        # Check Directory Type
        if not checkType({directory:[str], data:[str]}): raise TypeError("directory is not a `str`")
        
        # Writes to the file or input value into file
        with open(directory) as file:
            file.write(data)
      
    def rename(self, name:str, directory:str = None) -> None:
        """Rename the File

        :param name: New Name of the File
        :type name: str
        :param directory: Directory of File want to Rename, defaults to None
        :type directory: str, optional
        """
        
        # Setup Directory to the Object's Directory
        if directory is None: directory = self.directory
        
        # Check Directory Type
        if not checkType({directory:[str],name:[str]}): raise TypeError("parameter is not a `str`")
        
        # Directory List
        directoryList = directory.split("/")
        
        # File Type
        fileType = directoryList[-1].split(".")[-1]
        newDirectory = "/".join(directoryList) + name + fileType
        
        # Rename File
        os.rename(directory, newDirectory)
        
        # Setup Directory to the Object's Directory
        if directory is None:  self.directory = directory
              
    def move(self, newDirectory:str, oldDirectory:str = None) -> None:
        """Move the file from one Directory to another One

        :param newDirectory: Final Destination Directory
        :type newDirectory: str
        :param oldDirectory: Starting Orginal Directory, defaults to None
        :type oldDirectory: str, optional
        """
        
        # Setup Directory to the Object's Directory
        if oldDirectory is None: oldDirectory = self.directory
        
        # Check Directory Type
        if not checkType({oldDirectory:[str],newDirectory:[str]}): raise TypeError("directory is not a `str`")
        
        # Rename the Directory
        os.rename(oldDirectory, newDirectory)
        
        # Setup Directory to the Object's Directory
        if oldDirectory is None: self.directory = newDirectory
    
    def __str__(self)-> str:
        """File String

        :return: Directory of File
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

    def create(self, directory:str = None) -> None:
        """Create JSON File

        :param directory: JSON File Directory, defaults to None
        :type directory: str, optional
        :raises TypeError: Parameter Not Correct Type
        """
        
        # Setup Directory to the Object's Directory
        if directory is None: directory = self.directory
        
        # Check Parameter Types
        if not checkType({directory:[str]}):
            raise TypeError("Parameter Not Correct Type")
        
        # Create a JSON File 
        with open(directory,'x') as file:
            file.close()
            
        # Make the JSON File Empty
        with open(directory, "w") as file:
            json.dump({}, file, indent = 6)

    def read(self, directory:str = None) -> dict:
        """Read in JSON File

        :param directory: Directory of JSON File, defaults to None
        :type directory: str, optional
        :raises TypeError: Parameter Not Correct Type
        :return: JSON File Data
        :rtype: dict
        """
        
        # Setup Directory to the Object's Directory
        if directory is None: directory = self.directory
        
        # Check Parameter Types
        if not checkType({directory:[str]}):
            raise TypeError("Parameter Not Correct Type")
        
        # Reading in the Data
        with open(directory, "r") as file:
            data = json.load(file)
            
        return data

    def write(self, data:dict, directory:str = None) -> None:
        """Write to JSON File

        :param data: New JSON File Data
        :type data: dict
        :param directory: Directory of the JSON File, defaults to None
        :type directory: str, optional
        :raises TypeError: Parameter Not Correct Type
        """
        
        # Setup Directory to the Object's Directory
        if directory is None: directory = self.directory
        
        # Check Parameter Types
        if not checkType({directory:[str],data:[dict]}):
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

    def read(self, directory:str = None) -> pandas.DataFrame:
        """Read in CSV File

        :param directory: Directory of the CSV File, defaults to None
        :type directory: str, optional
        :raises TypeError: Parameter Not Correct Type
        :return: CSV Data
        :rtype: pandas.DataFrame
        """
        
        # Setup Directory to the Object's Directory
        if directory is None: directory = self.directory
        
        # Check Parameter Types
        if not checkType({directory:[str]}):
            raise TypeError("Parameter Not Correct Type")
        
        # Read in CSV as a Dataframe
        df = pandas.read_csv(self.directory)
        
        # Return Dataframe of the CSV Data
        return df.loc[:, ~df.columns.str.contains('^Unnamed')]

    def write(self, df:pandas.DataFrame, directory:str = None) -> None:
        """Write to CSV 

        :param df: Dataframe to Add to CSV
        :type df: pandas.DataFrame
        :param directory: CSV File Directory, defaults to None
        :type directory: str, optional
        :raises TypeError: Parameter Not Correct Type
        """
        
        # Setup Directory to the Object's Directory
        if directory is None: directory = self.directory
        
        # Check Parameter Types
        if not checkType({directory:[str]}):
            raise TypeError("Parameter Not Correct Type")
         
        # Write to CSV
        df.to_csv(directory)

# Folder Object
class Folder:
    def __init__(self, directory:str = None) -> None:
        """Folder Object

        :param directory: Folder Directory, defaults to None
        :type directory: str, optional
        """
        # Directory of File
        if directory is None: directory = f"{LOCAL_DIRECTORY}/new/"
        
        # Set Directory Variable
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



