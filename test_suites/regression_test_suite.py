import unittest

from tests.index.test_signup import TestSignup
from tests.index.test_search import TestSearch

t1 = unittest.TestLoader().loadTestsFromTestCase(TestSignup)
t2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)

regression_suite = unittest.TestSuite([t1, t2])

unittest.TextTestRunner().run(regression_suite)
