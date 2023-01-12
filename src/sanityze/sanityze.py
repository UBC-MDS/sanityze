import pandas as pd

class Cleanser:
    """
    The main class for the sanityze package. It's purpose is to clean the data frame
    before it's consumed by the training or prediction pipeline.
    
    Parameters
    ----------
    include_default_spotters : bool, optional
        If True, the default spotters will be added to the Cleanser. The default is True.
    hash_spotted : bool, optional
        If True, the spotters will hash the values within the columns they spot. 
        The default is False.
    
    """
    def __init__(self, include_default_spotters=True, hash_spotted = False):
        pass
    
    """
    Add a specific spotter to the Cleanser
    
    Parameters
    ----------
    spotter : Spotter
        A subclass of Spotter to add to the Cleanser. Note that spotters are added
        at the end of the list. Adding the same spotter will return False

    Returns
    -------
    True if the spotter was added, False if it was not added.    
    """
    def add_spotter(self, spotter) -> bool:
        pass
    
    """
    Remove a specific spotter from the Cleanser using the spotter's id
    
    Parameters
    ----------
    spotter_id : str
        The id of the spotter to remove
    
    Returns
    -------
    True if the spotter was removed, False if it was not removed.
    """
    def remove_spotter(self, spotter_id) -> bool:
        pass
    
    """
    Sanitizes the data frame using the spotters added to the Cleanser
    
    Parameters
    ----------
    df : pd.DataFrame
        The data frame to sanitize
        
    Returns
    -------
    The sanitized data frame 
    
    """
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        pass