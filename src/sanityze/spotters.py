class Spotter():
    """
    The Spotter interface to be implemented

    Attributes
    ----------
    name : str
        name of the spotter
    hashSpotted : bool, optional
        False by default, whether to hash or replace the spotted sensitive information

    Methods
    -------
    getSpotterName()
        return the Spotter name
    
    isHashSpotted()
        return whether the hashSpotted is True or False
    
    process(text)
        process the text depending on the hashSpotted value, if it is hash, replace it with hash
        otherwise, replace it with some default value
    """
    # please add the following line in the subclass
    # spotter_name = "<name of the spotter>"
    def __init__(self, name: str, hashSpotted=False):
        self.name = name
        self.hashSpotted = hashSpotted

    def getSpotterName(self) -> str:
        """Getting the spotter name

        Returns
        -------
        self.name : str
            the spotter name
        """
        return self.name

    def isHashSpotted(self) -> bool:
        """Getting the value of hashSpotted

        Returns
        -------
        self.hashSpotted : bool
            the Truth value of hashSpotted
        """
        return self.hashSpotted

    def process(self, text: str) -> str:
        """Process the given text, if hashSpotted is True, replace the spotted text with hash,
        otherwise, replace the spotted text with some default values
        
        Parameters
        ----------
        text : str
            The text to be spotted & modified

        Returns
        -------
        new_text : str
            
        """
        # # to be implemented in the specific spotter level
        # if self.isHashSpotted():
        #     new_text = "hash"
        # else:
        #     new_text = ""
        # return new_text
        pass
