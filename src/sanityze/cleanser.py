import pandas as pd
from sanityze.spotters import * 

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
        if (include_default_spotters):
            self.chain = [EmailSpotter("DEFAULTEMAILS",hash_spotted),CreditCardSpotter("DEFAULCCS",hash_spotted)]
        else:
            self.chain = []
    
    def add_spotter(self, spotter) -> bool:
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

        Examples
        --------
        >>> c = Cleanser(include_default_spotters=False)
        >>> s1 = EmailSpotter("EMAILS",True)
        >>> c.add_spotter(s1)

        """
        if (spotter is None):
            raise ValueError("spotter cannot be None in Cleanser.add_spotter()")
        if (spotter in self.chain):
            return False
        for s in self.chain:
            if (s.getSpotterUID() == spotter.getSpotterUID()):
                return False
        self.chain.append(spotter)
    
    def remove_spotter(self, spotter_id) -> bool:
        """
        Remove a specific spotter from the Cleanser using the spotter's id
        
        Parameters
        ----------
        spotter_id : str
            The id of the spotter to remove
        verbose: bool, optional
            If True, the spotter will print out debug information. The default is False.
        
        Returns
        -------
        True if the spotter was removed, False if it was not removed.

        Examples
        --------
        >>> c = Cleanser(include_default_spotters=False)
        >>> s1 = EmailSpotter("EMAILADDRS",True)
        >>> c.remove_spotter("EMAILADDRS")

        """
        if (spotter_id is None):
            raise ValueError("spotter_id cannot be None in Cleanser.remove_spotter()")
        for s in self.chain:
            if (s.getSpotterUID() == spotter_id):
                self.chain.remove(s)
                return True
        return False
    
    def _log(self, message: str, verbose: bool) -> None:
        """
        Internal utility function to log messages to the console
        
        Parameters
        ----------
        verbose: bool
            The verbosity of the log
        message : str
            The message to log
        
        Returns
        -------
        None

        Examples
        --------
        (called by clean())

        """
        if (verbose):
            print(f"- {message}")

    def clean(self, df: pd.DataFrame, verbose=False) -> pd.DataFrame:
        """
        Sanitizes the data frame using the spotters added to the Cleanser
        
        Parameters
        ----------
        df : pd.DataFrame
            The data frame to sanitize
            
        Returns
        -------
        The sanitized data frame 
        
        Examples
        --------
        >>> df = pd.DataFrame(data = {'product_name': ['laptop', 'printer foo@gaga.com', 'tablet', 'desk 5555 5555 5555 4444', 'chair'],
                                    'price': [1200, 150, 300, 450, 200]})
        >>> c = Cleanser()
        >>> c.clean(df, verbose=False)
            product_name	price
        0	laptop	1200
        1	printer EMAILADDRS	150
        2	tablet	300
        3	desk 5555 5555 5555 4444	450
        4	chair	200
        
        """
        if (df is None):
            raise ValueError("df cannot be None in clean")
        if not isinstance(df,pd.DataFrame):
            raise TypeError("df must be a pandas DataFrame in clean")
        # we only operate on a copy of the data frame, leaving 
        # the original data frame intact
        df_copy = df.copy() 
        # iterate thru the data frame cells
        row_len, col_len = df.shape
        for i in range(row_len):
            for j in range(col_len):
                cell = df.iat[i,j]
                # iterate thru the spotters and redact content
                # if the cell is of type string
                if isinstance(cell, str):
                    for spotter in self.chain:
                        self._log(f"{spotter.getSpotterUID()}: Processing cell {cell} ", verbose)
                        cell = spotter.process(cell)
                        self._log(f"{spotter.getSpotterUID()}: Processed cell {cell} ", verbose)
                # update the cell in the copy of the data frame
                df_copy.iat[i,j] = cell
        return df_copy