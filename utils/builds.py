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
    indexPage = File(f"{CURRENT_DIR}/templates/{bType.upper()}/index.{bType}",bType).copy(f"index.{bType}")
    
    
    
    # Base File Type, CSS, JS Folders
    bFolder = Folder(bType.upper())
    jsFolder = Folder('JS')
    
    contentFolder = Folder('Content')
    Folder(f"{contentFolder.directory}/Icons")
    if php: Folder('Events')
    Folder('Templates')
    
    # Add Files to Folders and Add Folders
    
    # Main JS File
    File(f"{CURRENT_DIR}/templates/JS/main.js",'js',False).copy(f"{jsFolder.directory}/main.js")
    
    # JQuery File
    File(f'{CURRENT_DIR}/templates/JS/jquery-3.7.1.js','js',False).copy(f'{jsFolder.directory}/jquery.js')
    
    # CSS Folder
    Folder(f'{CURRENT_DIR}/templates/CSS').copy(f'CSS')
    
    # Add HTML/PHP File
    File(f'{CURRENT_DIR}/templates/HTML/other.html','html').copy(f"{bType.upper()}/other.{bType}")
    
    # PHP Files
    if bType == 'php': File(f'{CURRENT_DIR}/templates/PHP/init.php','php',False).copy(f"{bFolder.directory}/init.php")
    
    # Add README.md
    File(f'{CURRENT_DIR}/templates/MD/README.md','md').copy('README.md')
    
    
    
    
    
    
    
    
    