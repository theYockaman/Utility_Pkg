
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

    def end(self) -> dict:
        """
        Sets the End Time and Prints the Time from .start() to .end()
        """
        
        self._t1 = time.time()
        time_lapse = self._t1 - self._t0

        minutes = int(time_lapse//60)
        seconds = int(time_lapse-(minutes *60))
        milliseconds = round((time_lapse - seconds) * (1000),2)
        
        print("{} minutes, {} seconds, {} milliseconds".format(minutes,seconds,milliseconds))
        
        return {"minutes":minutes, "seconds":seconds, "milliseconds":milliseconds}
