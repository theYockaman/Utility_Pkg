import typing

__all__ = [
    "split"
]

def split(string:str, splitString:typing.Union[str,list[str]]) -> list[str]:
    if isinstance(splitString,str):
        return string.split(splitString)
    
    elif isinstance(splitString, list):
        final = string.split(splitString[0])
        splitString = splitString[1:]
        
        for s in splitString:
            temp = []
            for x in final:
                temp.extend(x.split(s))
            final = temp
            
        for x in final:
            if x == "":
                final.remove(x)
            
        return final
                
    else:
        raise TypeError()


