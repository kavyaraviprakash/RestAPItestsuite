import unittest

TC_customer_login=__import__("TC_login")
TC_customer_forgotpwd = __import__("Tc_forgot_pwd")
TC_customer_signup= __import__("TC_SignUp")
TC_customer_logout=__import__("TC_Logout")
TC_customer_changepwd=__import__("TC_Change_pwd")


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(TC_customer_login))
suite.addTests(loader.loadTestsFromModule(TC_customer_forgotpwd))
suite.addTests(loader.loadTestsFromModule(TC_customer_logout))
#suite.addTests(loader.loadTestsFromModule(TC_customer_changepwd))


runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)