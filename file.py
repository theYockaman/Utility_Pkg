from typing import Union
import os
import json
import pandas as pd
from abc import abstractmethod, abstractstaticmethod




# Inital File Object to Base around Specific Files
class File:
    def __init__(self, directory:str = None) -> None:
        
        # Directory of File
        if directory is None: 
            directory = f"{os.path.dirname(os.path.abspath(__file__))}/new.txt"
            
        self.directory = directory
        
        # Creates File if Does Not Exist
        if not self.exists(self.directory): self.create(self.directory)
    
    @staticmethod
    def exists(directory:str) -> bool:
        return os.path.isfile(directory)

    @abstractmethod
    def create(self, directory:str = None) -> None:
        if directory is None:
            with open(self.directory,"x"):
                pass
        else:
            with open(directory,"x"):
                pass
     
    def delete(self, directory:str = None) -> None:
        
        if directory is None:
            # Deletes the File
            os.remove(self.directory)
            
            # Sets Directory to None
            self.directory = None
        else:
            # Deletes the File
            os.remove(directory)
            
    @abstractmethod
    def read(self) -> str:
        # Reads the file
        with open(self.directory) as file:
            data = file.read()
        return data

    @abstractmethod
    def write(self, data:str) -> None:
        with open(self.directory) as file:
            file.write(data)
      
    def rename(self, name:str) -> None:
        # Directory List
        directoryList = self.directory.split("/")
        
        # File Type
        fileType = directoryList[-1].split(".")[-1]
        directory = "/".join(directoryList) + name + fileType
        
        # Rename File
        os.rename(self.directory, directory)
        self.directory = directory
             
    def move(self, newDirectory:str) -> None:
        os.rename(self.directory, newDirectory)
        self.directory = newDirectory
    
    def __str__(self)-> str:
        if self.directory is None: return "No Directory Available"
        return self.directory

# TXT File Object
class TXT(File):
    def __init__(self, directory:str = None) -> None:
        """Txt File Object

        :param directory: Directory of TXT File, defaults to None
        :type directory: str, optional
        """
        super().__init__(directory) 

# JSON File Object
class JSON(File):
    def __init__(self, directory:str = None) -> None:
        
        if directory is None: f"{os.path.dirname(os.path.abspath(__file__))}/new.json"
        
        super().__init__(directory)

    def create(self, directory:str) -> None:
        with open(directory,'x') as file:
            file.close()
            
        with open(directory, "w") as file:
            json.dump({}, file, indent = 6)

    def read(self) -> dict:
        with open(self.directory, "r") as file:
            data = json.load(file)
        return data

    def write(self, data:dict) -> None:
        with open(self.directory, "w") as file:
            json.dump(data, file, indent = 6)

# CSV File Object
class CSV(File):
    def __init__(self, directory:str = None) -> None:
        if directory is None: directory = f"{os.path.dirname(os.path.abspath(__file__))}/new.csv"
        super().__init__(directory)

    def read(self) -> pd.DataFrame:
        df= pd.read_csv(self.directory)
        return df.loc[:, ~df.columns.str.contains('^Unnamed')]

    def write(self, df:pd.DataFrame) -> None:
        df.to_csv(self.directory)

# Folder Object
class Folder:
    def __init__(self, directory:str = None) -> None:
        # Directory of File
        if directory is None: directory = f"{os.path.dirname(os.path.abspath(__file__))}/new/"
        self.directory = directory
        
        # Creates File if Does Not Exist
        if not self.exists(self.directory): self.create(self.directory)
    
    def exists(self, directory:str = None) -> bool:
        if directory is None: directory = self.directory
        return os.path.isdir(directory)

    def create(self, directory:str = None) -> None:
        if directory is None: directory = self.directory
        
        os.makedirs(directory)
        
    def delete(self, directory:str = None) -> None:
        if directory is None: directory = self.directory
        
        # Deletes the File
        os.remove(directory)
        
        # Sets Directory to None
        self.directory = None
   
    def rename(self, name:str) -> None:
        # Directory List
        directoryList = self.directory.split("/")[:-1]
        
        # File Type
        directory = "/".join(directoryList) + name
        
        # Rename File
        os.rename(self.directory, directory)
        self.directory = directory
             
    def move(self, newDirectory:str) -> bool:
        os.rename(self.directory, newDirectory)
        self.directory = newDirectory
    
    def add(self, new):
        pass
      
    def __str__(self)-> str:
        if self.directory is None: return "No Directory Available"
        return self.directory



