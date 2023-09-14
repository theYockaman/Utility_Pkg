import numpy as np
import math
import pandas as pd
from .functions import checkType
from typing import Union

__all__ = [
    "sigmoid"
    , "average"
]


# Sigmoid Function
def sigmoid(x:Union[pd.DataFrame,pd.Series,int,float]) -> Union[pd.DataFrame,pd.Series,int,float]:
    """Calculate the Sigmoid

    :param x: Value(s) to Calculate the Sigmoid from
    :type x: Union[pd.DataFrame,pd.Series,int,float]
    :raises TypeError: Wrong Type: Change Input Type
    :return: Sigmoid Value(s)
    :rtype: Union[pd.DataFrame,pd.Series,int,float]
    """
    
    if checkType({x:[pd.DataFrame,pd.Series]}):
        return 1.0 / (1.0 + np.exp(-x))
    
    elif checkType({x:[int,float]}):
        return 1 / (1 + math.exp(-x))
    
    else:
        raise TypeError("Wrong Type: Change Input Type")

# Average Function
def average(x:list) -> Union[int,float]:
    """Average Value of a List

    :param x: Values to find the Average
    :type x: list
    :raises TypeError: Not a List Type
    :return: Average Value
    :rtype: Union[int,float]
    """
    
    if checkType({x:list}):
        return sum(x)/len(x)
    
    else:
        raise TypeError("Not a List Type")
    
    