"""

Unittest

Unities can be: functions, methods, classes, modules, etc...

To create our tests we create classes that inherit unittest.TestCase class so then we can have
all 'assertions' presents in the module.

To run all tests, we use unittest.main()

See: https://docs.python.org/3/library/unittest.html

| *************************************************** |
|            Method          |       Checks that      |
|  ------------------------- | -----------------------|
|  assertEqual(a, b)	     |  a == b                |
|  assertNotEqual(a, b)	     |  a != b                |
|  assertTrue(x)	         |  bool(x) is True       |
|  assertFalse(x)	         |  bool(x) is False      |
|  assertIs(a, b)	         |  a is b                |
|  assertIsNot(a, b)	     |  a is not b            |
|  assertIsNone(x)	         |  x is None             |
|  assertIsNotNone(x)	     |  x is not None         |
|  assertIn(a, b)	         |  a in b                |
|  assertNotIn(a, b)         |  a not in b            |
|  assertIsInstance(a, b)    |  isinstance(a, b)      |
|  assertNotIsInstance(a, b) |  not isinstance(a, b)  |
| *************************************************** |

To execute the tests with unittest: python <module_name>.py

To execute the tests with unittest (verbose mode): python <module_name>.py -v

"""


import learning_unittest


t = learning_unittest.TestCase