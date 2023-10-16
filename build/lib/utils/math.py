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
    
    # Check X Type
    checkType([x],[[pd.DataFrame,pd.Series,int,float]])
    
    # Different Sigmoid X Types 
    if checkType([x],[[pd.DataFrame,pd.Series]],False):
        return 1.0 / (1.0 + np.exp(-x))
    
    elif checkType([x],[[int,float]],False):
        return 1 / (1 + math.exp(-x))
    
# Average Function
def average(x:list) -> Union[int,float]:
    """Average Value of a List

    :param x: Values to find the Average
    :type x: list
    :return: Average Value
    :rtype: Union[int,float]
    """
    
    # Check X Type
    checkType([x],[list])
    
    # Calculate Average
    return sum(x)/len(x)
    
    