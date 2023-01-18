from sanityze import sanityze
from sanityze import spotters

#create spotter objects for testing
cc_Spotter_hash = spotters.CreditCardSpotter(uid="CREDITCARD", hashSpotted=True)

cc_Spotter_no_hash = spotters.CreditCardSpotter(uid="CREDITCARD", hashSpotted=False)

# test string to detect credit card presence, fake credit card numbers generated from: https://www.creditcardvalidator.org/generator

fake_cc = {"VISA" : "4556129404313766", 
           "MASTERCARD" : "5567554868135971",  
           "AMEX" : "345160678082328", 
           "DINERS" : "3013130458900846", 
           "DISCOVER" : "6011087735246416",
           "JCB" : "3538159804477445"
           }

# test string for credit card md5 hashes
cc_number = "VISA, 4929688015693122"
credit_hash = "VISA, 34c2171639b834dce4b1c0183a91d427"

# strings of equal length to credit cards
number_string = "5628404238239405, 5673289472024660, 8709, 356785, 1111111111111111"

# test string for full credit card info
full_cc_info = "VISA, 4916363769587210, 10/2023, 992"

# check if uid corect UID is returned 
def test_creditcard_spotter_uid():
    assert cc_Spotter_hash.getSpotterUID() == "CREDITCARD"

# check if correct hashSpotted boolean is returned 
def test_creditcard_spotter_hash_bool():
    assert cc_Spotter_hash.isHashSpotted() == True
    assert cc_Spotter_no_hash.isHashSpotted() == False

# check random numbers the same length of a credit card do not get replaced 
def test_creditcard_spotter_random_number():
    assert number_string == cc_Spotter_no_hash.process(number_string)

# check included credit card patterns are matched and replaced
def test_creditcard_spotter_cc_match():

    for cc in fake_cc.values():
        assert "CREDITCARD" == cc_Spotter_no_hash.process(cc)

# check if cc number in a string is replaced
def test_creditcard_spotter_full_cc():
    assert "VISA, CREDITCARD, 10/2023, 992" == cc_Spotter_no_hash.process(full_cc_info)

# check correct hashes are replaced
def test_creditcard_spotter_hash():
    assert credit_hash == cc_Spotter_hash.process(cc_number)
