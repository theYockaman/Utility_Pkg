
from .. import file


__all__ = [
    "coverPage"
    , "createReadMe"
]

# Help Create the Basic Structure to the Application
def coverPage(title:str, actions:dict):
    
    # Loop for the Application
    while True:
        
        # Application Cover Title
        print(title)
        
        # Prints out Actions
        actionNumber = {}
        lastNumber = 0
        for x, (name, action) in enumerate(actions.items()):
            print(f"{x+1}. {name}")
            lastNumber = x+1
            actionNumber.update({x+1:action})
            
        lastNumber+=1
            
        # Prints the Quit
        print(f'{lastNumber}. Quit Application\n')
        
        # Input By Anwser
        try:   
            anwser = int(input('Input Number Above: '))
            print()
        except:
            print("Try a Different Value\n")
            continue
        
        # Action Taken
        if anwser not in actionNumber.keys() and anwser != lastNumber:
            print("Not in Range of Numbers\n")
            continue
        
        if anwser == lastNumber:
            break
        else:
            actionNumber[anwser]()
            print()
            

# Create README.md from Package
def createReadMe(packageDirectory:str, storeDirectory:str = None):
    
    # Folder of the Package
    package = file.Folder(packageDirectory)
    
    # Create README.md
    if storeDirectory is None: 
        f = file.File("README.md")
    else:
        f = file.File(f"{storeDirectory}/README.md")
    
    # Recieve the Documentation
    for x in package.files:
        x = file.File(x)
        
        if "py" == x.extension:
            fileData = x.read()
            
            print(fileData)
            #classList = fileData.split("class")
            #fList = fileData.split('"""')
            break
        
        
        
        
        
        
    data = ""
    
    f.write(data)
        
    
            
            
            