
# Module Documentation
"""
Basic Functions to be used various projects, but to simplify the process while writing the code.
"""

# Import Modules
import traceback, sys, time

__all__ = [
    "printSyntax"
    , "printTraceback"
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
# def checkType(variables:list, values:list, throwError:bool = True) -> bool:
#     """Checks the Data Types of Variables

#     :param variables: List of Variables ex. [variableOne, variableTwo]
#     :type variables: list
#     :param values: List of the Values of each Variable ex. [typeVariableOne, typeVariableTwo] or [str, int, float]
#     :type values: list
#     :param throwError: `True` Throws Errors `False` Does not Throw Errors, defaults to True
#     :type throwError: bool, optional
#     :raises ValueError: variables not `list` type
#     :raises ValueError: values not `list` type
#     :raises ValueError: throwError not `bool` type
#     :return: `True` if Variable and Types Match `False` if Variables do not Match
#     :rtype: bool
#     """
#     # Setup New isinstance() Function
#     tc1 = typesentry.Config()
#     is_typed = tc1.is_type
    
#     # Make sure Parameter is a Dictionary
#     if not isinstance(variables, list): raise ValueError("variables not `list` type")
    
#     # Make sure Parameter is a Dictionary
#     if not isinstance(values, list): raise ValueError("values not `list` type")
    
#     # Make sure Parameter is a Dictionary
#     if not isinstance(throwError, bool): raise ValueError("throwError not `bool` type")
    
    
    
#     # Iterate through each in Variables
#     for variable, value in zip(variables, values):
        
#         # Null Variable Value
#         if variable is None and value is None: continue
        
#         try:
#             isinstance(value,(list,set,tuple))
#         except TypeError:
            
#             if not is_typed(variable, value):
#                 # Throw Errors
#                 if throwError: raise TypeError(f"{variable} not `{str(value)}` type")
                
#                 return False
            
#         if isinstance(value,(list,set,tuple)):
                
#                 if variable is None and None not in value: return False

#                 if variable is None and None in value: continue
                
#                 if None in value: value.remove(None)
                
                
                
#                 if any(is_typed(variable,v) for v in value):
#                     continue
                
#                 else:
#                     for v in value:
#                         if not is_typed(variable,v):
#                             # Throw Errors
#                             if throwError: raise TypeError(f"{variable} not `{str(value)}` type")
                            
#                             return False
                
#         else:
#             if not is_typed(variable, value):
#                 # Throw Errors
#                 if throwError: raise TypeError(f"{variable} not `{str(value)}` type")
                
#                 return False
        
        
        
        
                
#     return True

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


