import hashlib
import re

class Spotter():
    """
    The Spotter interface to be implemented

    Attributes
    ----------
    uid : str
        uid of the spotter
    hashSpotted : bool, optional
        False by default, whether to hash or replace the spotted sensitive information

    Methods
    -------
    getSpotterUID()
        return the Spotter uid
    
    isHashSpotted()
        return whether the hashSpotted is True or False
    
    process(text)
        process the text depending on the hashSpotted value, if it is hash, replace it with hash
        otherwise, replace it with some default value
    """
    # please add the following line in the subclass
    # spotter_uid = "<uid of the spotter>"
    def __init__(self, uid: str, hashSpotted=False):
        self.uid = uid
        self.hashSpotted = hashSpotted

    def getSpotterUID(self) -> str:
        """Getting the spotter uid

        Returns
        -------
        self.uid : str
            the spotter uid
        """
        return self.uid

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


class CreditCardSpotter(Spotter):
    """
    The Credit Card Spotter Subclass

    Attributes
    ----------
    uid : str
        uid of the spotter, "CREDITCARD"
    hashSpotted : bool, optional
        False by default, whether to hash or replace the spotted sensitive information

    Methods
    -------
    getSpotterUID()
        return the Spotter uid, "CREDITCARD"
    
    isHashSpotted()
        return whether the hashSpotted is True or False
    
    process(text)
        process the text depending on the hashSpotted value, if hashSpotted is True, replace the spotted credit card number with hash
        otherwise, replace the spotted credit card number with some default value
    """
    def getSpotterUID(self) -> str:
        """Getting the credit card spotter uid

        Returns
        -------
        "CREDITCARD" : str
            a fixed str value for CreditCardSpotter
        """
        return "CREDITCARD"

    def process(self, text: str) -> str:
        """Process the given text, if hashSpotted is True, replace the spotted credit card number with hash,
        otherwise, replace the spotted credit card number with some default values
        
        Parameters
        ----------
        text : str
            The text to be spotted & modified

        Returns
        -------
        new_text : str
            the text with credit card number replaced by a hash or the default string value
        """
        # spot credit card using regex / other packages
        # if self.isHashSpotted():
        #     new_text = text.replace_hash()
        # else:
        #     new_text = text.replace_dummy()
        pass

class EmailSpotter(Spotter):
    """
    The Email Spotter Subclass

    Attributes
    ----------
    uid : str
        uid of the spotter, "EMAILADDRS"
    hashSpotted : bool, optional
        False by default, whether to hash or replace the spotted sensitive information

    Methods
    -------
    getSpotterUID()
        return the Spotter uid, "EMAILADDRS"
    
    isHashSpotted()
        return whether the hashSpotted is True or False
    
    process(text)
        process the text depending on the hashSpotted value, if hashSpotted is True, replace the spotted email with hash
        otherwise, replace the spotted email with some default value
    """
    def getSpotterUID(self) -> str:
        """Getting the email spotter uid

        Returns
        -------
        "EMAILADDRS" : str
            a fixed str value for EmailSpotter
        """
        return "EMAILADDRS"

    def process(self, text: str) -> str:
        """Process the given text, if hashSpotted is True, replace the spotted email with hash,
        otherwise, replace the spotted email with some default values
        
        Parameters
        ----------
        text : str
            The text to be spotted & modified

        Returns
        -------
        new_text : str
            the text with email replaced by a hash or the default string value
        """
        # base preprocessing (if needed)
        
        dummy_text = "{{EMAILADDRS}}"
        
        # email regex (adapted from [https://scrubadub.readthedocs.io/en/stable/_modules/scrubadub/detectors/email.html#EmailDetector:~:text=regex%20%3D%20re,.IGNORECASE)])
        regex = re.compile((
            r"\b[a-z0-9!#$%&'*+\/=?^_`{|}~-]"             # start with this character
            r"(?:"
            r"    [\.a-z0-9!#$%&'*+\/=?^_`{|}~-]{0,62}"   # valid next characters (max length 64 chars before @)
            r"    [a-z0-9!#$%&'*+\/=?^_`{|}~-]"           # end with this character
            r")?"
            r"(?:@|\sat\s)"                               # @ or the word 'at' instead
            r"[a-z0-9]"                                   # domain starts like this
            r"(?:"
            r"    (?=[a-z0-9-]*(\.|\sdot\s))"             # A lookahead to ensure there is a dot in the domain
            r"    (?:\.|\sdot\s|[a-z0-9-]){0,251}"        # might have a '.' or the word 'dot' instead
            r"    [a-z0-9]"                               # domain has max 253 chars, ends with one of these
            r")+\b"
        ), re.VERBOSE | re.IGNORECASE)
        
        if self.isHashSpotted():            
            text = re.sub(regex, lambda x:hashlib.md5(x.group().encode()).hexdigest(), text)
            new_text = text
        else:
            new_text = re.sub(regex, dummy_text, text)

        return new_text