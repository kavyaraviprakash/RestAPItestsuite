import unittest

TC_add_to_cart=__import__("TC_add_to_cart")
Tc_checkout = __import__("Tc_checkout")
TC_payment= __import__("TC_payment")


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(TC_add_to_cart))
suite.addTests(loader.loadTestsFromModule(Tc_checkout))
suite.addTests(loader.loadTestsFromModule(TC_payment))
#suite.addTests(loader.loadTestsFromModule(TC_customer_changepwd))


runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)