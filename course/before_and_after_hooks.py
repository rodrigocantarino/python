"""

Unittests - Before and after Hooks


Hooks are the tests itself. Is he test execution.

setup() -> is executed before each test method. Is useful to create objects instances and other data.

tearDown() -> is executed at the end of each test method. Is useful to delete data or
to close connections with databases.


"""

import unittest


class ModuleTest(unittest.TestCase):

    def setUp(self):
        # setUp() configurations
        pass

    def test_first(self):
        # Here the setUp() will be executed before the test_first() method.
        # Here the tearDown() will be executed after the test_first() method.
        pass

    def test_second(self):
        # Here the setUp() will be executed before the test_first() method.
        # Here the tearDown() will be executed after the test_first() method.
        pass

    def tearDown(self):
        # tearDown() configurations
        pass

