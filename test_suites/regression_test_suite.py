import unittest

from tests.index.test_login import TestLogin

t1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)

regression_suite = unittest.TestSuite([t1])

unittest.TextTestRunner().run(regression_suite)
