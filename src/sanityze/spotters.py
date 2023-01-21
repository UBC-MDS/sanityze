import re
import hashlib

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

    Examples
    --------
    Spotter should be initialized in a subclass level, therefore, skipping examples in the parent class
    >>> 

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

        Examples
        --------
        >>> sub_spotter.getSpotterUID()
        "<sub class spotter UID>"
        """
        return self.uid

    def isHashSpotted(self) -> bool:
        """Getting the value of hashSpotted

        Returns
        -------
        self.hashSpotted : bool
            the Truth value of hashSpotted
        
        Examples
        --------
        >>> sub_spotter.isHashSpotted()
        TRUE
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
    
    Examples
    --------
    >>> CreditCardSpotter("CREDITCARDS",True)
    <sanityze.spotters.CreditCardSpotter object at 0x000001207F7B5880>

    
    """
    def getSpotterUID(self) -> str:
        """Getting the credit card spotter uid

        Returns
        -------
        "CREDITCARD" : str
            a fixed str value for CreditCardSpotter

        Examples
        --------
        >>> cc = CreditCardSpotter("CREDITCARDS",True)
        >>> cc.getSpotterUID()
        CREDITCARD
        
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
        
        Examples
        --------
        >>> cc = CreditCardSpotter("CREDITCARDS", False)
        >>> cc.process("4556129404313766")
        CREDITCARD

        """
        # Regexes from:
        # http://www.regular-expressions.info/creditcard.html

        # taken from the alphagov fork of scrubadub: https://github.com/alphagov/scrubadub

        # credit card patterns to match
        cc_pattern = re.compile((
            r"(?:4[0-9]{12}(?:[0-9]{3})?"  		# Visa
            r"|(?:5[1-5][0-9]{2}"          		# MasterCard
            r"|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}"
            r"|3[47][0-9]{13}"             		# American Express
            r"|3(?:0[0-5]|[68][0-9])[0-9]{13}"   	# Diners Club
            r"|6(?:011|5[0-9]{2})[0-9]{12}"      	# Discover
            r"|(?:2131|1800|35\d{3})\d{11})"      	# JCB
         ), re.VERBOSE)

        # sets replacement value based on output of isHashSpotted()
        if self.isHashSpotted():
            replacement = hashlib.md5(text.encode()).hexdigest()
        else:
            replacement = self.getSpotterUID()
        
        # replaces cc number with replacement value
        clean_str = re.sub(cc_pattern, replacement, text)

        return(clean_str)


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

        Examples
        --------
        >>> ee = EmailSpotter("EMAILS", False)
        >>> ee.getSpotterUID()
        EMAILADDRS

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

        Examples
        --------
        >>> ee = EmailSpotter("EMAILS", False)
        >>> ee.process("abcd1234@gmail.com")
        EMAILADDRS

        """
        # base preprocessing (if needed)
                
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
            new_text = re.sub(regex, self.getSpotterUID(), text)

        return new_text