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
    CURRENT_DIR = os.path.dirname(__file__).replace('\\','/')
    PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
    
    # Base File Type
    bType = 'html'
    if php: bType = 'php'
    

    # Index Page Creation
    print(f'{CURRENT_DIR}/templates/{bType.upper()}/index.{bType}')
    print(PARENT_DIR)
    File(f'{CURRENT_DIR}/templates/{bType.upper()}/index.{bType}',bType, False).copy(f'index.{bType}')
    
    # Base File Type, CSS, JS Folders
    bFolder = Folder(bType.upper())
    jsFolder = Folder('JS')
    Folder('Content')
    
    # Add Files to Folders
    File(f"{CURRENT_DIR}/templates/JS/main.js",'js',False).copy(f"{jsFolder.directory}/main.js")
    
    # JQuery File
    File(f'{CURRENT_DIR}/templates/JS/jquery-3.7.1.js','js',False).copy(f'{jsFolder.directory}/jquery.js')
    
    # Reset CSS File
    Folder(f'{CURRENT_DIR}/templates/CSS').copy(f'CSS')
    
    # Add HTML/PHP File
    File(f'{CURRENT_DIR}/templates/HTML/other.html','html').copy(f"{bType.upper()}/other.{bType}")
    
    # PHP Files
    if bType == 'php': 
        File(f'{CURRENT_DIR}/templates/PHP/init.php','php',False).copy(f"{bFolder.directory}/init.php")
    
    
    
    
    
    
    
    
    