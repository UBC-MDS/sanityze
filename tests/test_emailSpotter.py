from sanityze.cleanser import *
from sanityze.spotters import *

def test_email_spotter():
    # Initialize an email spotter object
    emailSpotter_hash = EmailSpotter("EMAILADDRS", True)

    # test case 1: replace email with hash (catching 2 emails)
    assert 'My email address is 4b06d8d4bc9491edb00684048e40c4d8 and 967f3839a35c04041ea6e75b7a917b04 Thank you.' \
        == emailSpotter_hash.process("My email address is caesar@gmail.com and aaaa@yahoo.mail.com Thank you.")

    # test case 2: replace email with fixed string
    emailSpotter_notHash = EmailSpotter("", False)
    assert 'My email address is EMAILADDRS and EMAILADDRS Thank you.' \
        == emailSpotter_notHash.process("My email address is caesar@gmail.com and aaaa@yahoo.mail.com Thank you.")

    # test case 3: check whether the email spotter can work on different types of email (replace with hash)
    assert 'My email address is 00345d02eb20733e49077c9618f0d598 and ba68a57288bf24140628f37aadbb7920 Thank you.' \
        == emailSpotter_hash.process("My email address is 123456abcd@yahoo.com and zzzzz123@yahoo.mail Thank you.")

    # test case 4: check whether the email spotter can work on different types of email (replace with fixed string)
    assert 'Email address: EMAILADDRS, another email address is EMAILADDRS' \
     == emailSpotter_notHash.process("Email address: 123456abcd@yahoo.com, another email address is zzzzz123@yahoo.mail")

    # test case 5: check whether the email spotter can detect 'aaa at gmail.com' format (replace with hash)
    assert 'Email address: c6598176e9f6a7c8c1208494c1a189e2, another email address is be4deee3dfc06dea00b95bf6be0a26f1' \
    == emailSpotter_hash.process("Email address: 123456abcd at hotmail.com, another email address is zzzzz123 at onedrive.com")

    # test case 6: check whether the email spotter can detect 'aaa at gmail.com' format (replace with fixed string)
    assert 'Email address: EMAILADDRS, another email address is EMAILADDRS' \
    == emailSpotter_notHash.process("Email address: 123456abcd at outlook.ca, another email address is zzzzz123 at gmail.mail")



