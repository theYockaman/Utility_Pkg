import os
import shutil
from .file import File
from .utils import LOCAL_DIRECTORY

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
        """Checks existence of the Folder

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
   
    def rename(self, name:str) -> str:
        """Rename the Folder

        :param name: New Name of the Folder
        :type name: str
        :raises ValueError: No Directory
        :raises FileExistsError: Target Directory Already Exists
        :return: Directory of the Renamed Folder
        :rtype: str
        """
        
        # Setup Directory to the Object's Directory
        if not self.exists():
            raise ValueError("Directory does not exist")

        # Get parent directory
        parent = os.path.dirname(self._directory)
        new_path = os.path.join(parent, name)

        if os.path.exists(new_path):
            raise FileExistsError(f"Target directory '{new_path}' already exists")

        os.rename(self._directory, new_path)
        self._directory = new_path
        return self._directory
        
             
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
