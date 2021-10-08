import unittest

TC_contact_us=__import__("TC_contact_us")
TC_currency_selection = __import__("TC_currency_selection")
Tc_navbar= __import__("Tc_navbar")
Tc_order= __import__("Tc_order")
TC_language_translation= __import__("TC_language_translation")


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(TC_contact_us))
suite.addTests(loader.loadTestsFromModule(TC_currency_selection))
suite.addTests(loader.loadTestsFromModule(Tc_navbar))
suite.addTests(loader.loadTestsFromModule(Tc_order))
suite.addTests(loader.loadTestsFromModule(TC_language_translation))

#suite.addTests(loader.loadTestsFromModule(TC_customer_changepwd))


runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)