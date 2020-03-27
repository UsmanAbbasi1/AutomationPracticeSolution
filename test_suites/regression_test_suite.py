import unittest

from tests.index.test_login import TestLogin
from tests.index.test_search import TestSearch

t1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
t2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)

regression_suite = unittest.TestSuite([t1, t2])

unittest.TextTestRunner().run(regression_suite)
