import unittest

from Package1.TC_Login import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReceipt import PaymentReceiptTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReceiptTest)

#Create Test Suite
masterTestSuite = unittest.TestSuite([tc1,tc2, tc3, tc4])# Master Test Suite
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)