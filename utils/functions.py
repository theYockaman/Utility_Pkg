
# Module Documentation
"""
Basic Functions to be used various projects, but to simplify the process while writing the code.
"""

# Import Modules
import traceback, sys, time

__all__ = [
    "printSyntax"
    , "printTraceback"
    , "checkType"
    , "Duration"
]
    
# Syntax Printer
def printSyntax(syntax, toPrint:bool = True) -> None:
    """Prints Syntax in Function or in Coding Projects

    :param syntax: Syntax that will run through a Print Statement
    :type syntax: Any
    :param toPrint: `True` prints the Syntax `False` does not print the Syntax, defaults to True
    :type toPrint: bool, optional
    :raises TypeError: toPrint Parameter is not a Boolean Type
    """
    
    # Check to Make sure toPrint Parameter is a Boolean Variable
    if not checkType({toPrint:[bool]}): raise TypeError("toPrint Parameter is not a Boolean Type")
    
    # Print Syntax
    if toPrint is True: print(syntax)
        
# Print Traceback
def printTraceback() -> None:
    """
    Prints the Traceback of Current Ran Code and Quits the Code
    """
    
    # Prints the Traceback
    print(traceback.format_exc())
    sys.exit()

# Checks Variable DataType
def checkType(variables:dict, raiseErrors:bool = False) -> bool:
    """Check Types of Variables

    :param variables: {Variable:[Types]} ex. {variableOne:[str,int,float]}
    :type variables: dict[list]
    :param raiseErrors: `True` raise Errors, `False` does not raise Errors
    :type raiseErrors: bool
    :raises ValueError: Variables Wrong Type: dict
    :return: `True` Types Valid with Variables , `False` Types Not Valid with Variables
    :rtype: bool
    """
    
    # Make sure Parameter is a Dictionary
    if not isinstance(variables, dict): raise ValueError("Variables Wrong Type: dict")
    
    # Return Value
    rValue = True
    
    
    # Iterate through each in Variables
    for key, value in variables.items():
        
        # List Variables
        if isinstance(value,list) or isinstance(value,set) or isinstance(value,tuple):
            
            # Check if Variable is None and None is not in the List
            if key is None and None not in value: 
                rValue = False
                break

            # Check if Variable is None and None is in the List
            if key is None and None in value: continue
            
            # Remove all None Values in the List
            if None in value: value.remove(None)
            
            # Check type in List
            boolValues = [checkType({key:x}) for x in value]
            
            if True in boolValues:
                continue
            else:
                rValue = False
                break
            
        else:
            # Check if Variable is None and Value is None
            if key is None and value is None: continue
            
            # Check Variable with Type
            if isinstance(key,value) is not True:
                rValue = False
                break
    
    # Throw Errors
    if rValue == False and raiseErrors == True:
        string = "Variables not the Correct Type:\n"
        for key, value in variables.items():
            string += f"{key.__name__}: {value}\n"
        
        raise TypeError(string)
        
    return rValue

# Check Duration of Code
class Duration: 
    def __init__(self) -> None:
        """
        Duration to find Length of time it takes to Run Code. Starts with the .start() function.
        """
        self.start()

    def start(self) -> None:
        """ 
        Grabs Start Time with Setting Final Time to None
        """
        
        self._t0 = time.time()
        self._t1 = None

    def end(self) -> None:
        """
        Sets the End Time and Prints the Time from .start() to .end()
        """
        
        self._t1 = time.time()
        time_lapse = self._t1 - self._t0

        minutes = int(time_lapse//60)
        seconds = int(time_lapse-(minutes *60))
        milliseconds = round((time_lapse - seconds) * (1000),2)
        
        print("{} minutes, {} seconds, {} milliseconds".format(minutes,seconds,milliseconds))


