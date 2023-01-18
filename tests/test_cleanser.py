from sanityze.cleanser import *
from sanityze.spotters import *

# check that the Cleanser class is initialized property
def test_cleanser_init_default():
    c = Cleanser()
    assert(len(c.chain) > 0,"Cleanser should have at least one spotter in the chain")

# Init with no spotters
def test_cleanser_init_no_spotters():
    c = Cleanser(include_default_spotters=True)
    assert(len(c.chain) == 0,"Cleanser should have no spotters in the chain when include_default_spotters is False")
  
# Init with no spotters, add/remove later  (EmailSpotter)
def test_cleanser_add_remove_e():
    c = Cleanser(include_default_spotters=False)
    s = EmailSpotter("EMAILS",False)
    c.add_spotter(s)
    assert(len(c.chain) == 1,"Cleanser should have one spotter in the chain")
    assert(c.chain[0] == s,"Cleanser should have the EmailSpotter in the chain")
    c.remove_spotter("EMAILS")
    assert(len(c.chain) == 0,"Cleanser should have no spotters in the chain")

# Init with no spotters, add/remove later  (CreditCardSpotter)
def test_cleanser_add_remove_c():
    c = Cleanser(include_default_spotters=False)
    s = CreditCardSpotter("CREDITCARDS",False)
    c.add_spotter(s)
    assert(len(c.chain) == 1,"Cleanser should have one spotter in the chain")
    assert(c.chain[0] == s,"Cleanser should have the CreditCardSpotter in the chain")
    c.remove_spotter("CREDITCARDS")
    assert(len(c.chain) == 0,"Cleanser should have no spotters in the chain")
    
# Init with no spotters, add/remove all spotters later  (EmailSpotter, CreditCardSpotter)
def test_cleanser_add_remove_all():
    c = Cleanser(include_default_spotters=False)
    s1 = EmailSpotter("EMAILS",False)
    s2 = CreditCardSpotter("CREDITCARDS",False)
    c.add_spotter(s1)
    assert(len(c.chain) == 1,"Cleanser should have one spotter in the chain")
    c.add_spotter(s2)
    assert(len(c.chain) == 2,"Cleanser should have two spotters in the chain")
    c.remove_spotter("EMAILS")
    assert(len(c.chain) == 1,"Cleanser should one spotter in the chain")
    c.remove_spotter('CREDITCARDS')
    assert(len(c.chain) == 1,"Cleanser should no spotters in the chain")

def test_add_duplicate_spotters():
    c = Cleanser(include_default_spotters=False)
    s1 = EmailSpotter("EMAILS",False)
    s2 = EmailSpotter("EMAILS",False)
    a1 = c.add_spotter(s1)
    a2 = c.add_spotter(s2)
    assert(a1 == True,"Cleanser should have added the first spotter")
    assert(a2 == False,"Cleanser should not have added the second spotter")
    assert(len(c.chain) == 0,"Cleanser should have not spotters in the chain")
    
