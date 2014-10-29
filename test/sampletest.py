import unittest


class LoggedTestCase(unittest.TestCase):

    def test_sample(self):
        print "Sample test has run"
