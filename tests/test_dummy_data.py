from sanityze.cleanser import *
from sanityze.spotters import *
import pandas as pd

def test_cleanser_with_dummy_data():

    # create Cleanser with default spotter
    c = Cleanser(include_default_spotters=True)

    assert len(c.chain) == 2,"Cleanser should have two spotter in the chain by default"

    # reading dummy data with pii
    df_with_pii = pd.read_csv('data_with_pii.csv')
    assert df_with_pii.shape == (20, 8), "Dummy Data with PII should have shape (20, 8)"
    # reading cleaned dummy data without hash
    df_with_pii_cleaned_non_hash = pd.read_csv('data_with_pii_cleaned_non_hash.csv')
    assert c.clean(df_with_pii).equals(df_with_pii_cleaned_non_hash), "PII should be cleaned with a fixed string"


    # reading dummy data without pii
    df_without_pii = pd.read_csv('data_without_pii.csv')
    df_without_pii_copy = df_without_pii.copy()
    assert df_without_pii.shape == (20, 5), "Dummy Data without PII should have shape (20, 8)"

    assert c.clean(df_without_pii).equals(df_without_pii_copy), "Data without PII should be the same after c.clean()"
    


    # create Cleanser with hash spotter
    c = Cleanser(include_default_spotters=False)
    s1 = EmailSpotter("EMAILS",True)
    s2 = CreditCardSpotter("CREDITCARDS",True)
    c.add_spotter(s1)
    c.add_spotter(s2)

    assert len(c.chain) == 2,"Cleanser should have two spotter in the chain by default"

    # reading cleaned dummy data with hash
    df_with_pii_cleaned_hash = pd.read_csv('data_with_pii_cleaned_hash.csv')
    assert c.clean(df_with_pii).equals(df_with_pii_cleaned_hash), "PII should be cleaned with hash"

    assert c.clean(df_without_pii).equals(df_without_pii_copy), "Data without PII should be the same after c.clean()"
