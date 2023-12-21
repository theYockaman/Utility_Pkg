from .file import *
import os




__all__= [
    "createWebsite"
]

def createWebsite(php:bool = False) -> None:
    """Create Website with all Files

    :param php: PHP website vs. HTML, defaults to False
    :type php: bool, optional
    """
    
    # Base File Type
    bType = 'html'
    if php: bType = 'php'
    

    # Index Page Creation
    
    # Base File Type, CSS, JS Folders
    bFolder = Folder(bType.upper())
    jsFolder = Folder('JS')
    Folder('Content')
    
    # Add Files to Folders
    
    File(f"./templates/JS/main.js",'js',False).copy(f"{jsFolder.directory}/main.js")
    
    # JQuery File
    File(f'./templates/JS/jquery-3.7.1.js','js',False).copy(f'{jsFolder.directory}/jquery.js')
    
    # Reset CSS File
    Folder(f'./templates/CSS').copy(f'CSS')
    
    # Add HTML/PHP File
    File(f'./templates/HTML/other.html','html').copy(f"{bType.upper()}/other.{bType}")
    
    # PHP Files
    if bType == 'php': 
        File(f'./templates/PHP/init.php','php',False).copy(f"{bFolder.directory}/init.php")
    
    
    
    
    
    
    
    
    