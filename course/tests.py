import unittest

from activities import eat, sleep, funny


class ActivitiesTests(unittest.TestCase):

    def test_eat_healthy(self):
        """Testing healthy food."""
        self.assertEqual(
            eat('fish', True),
            "I'm eating fish because it's healthy!"
        )

    def test_eat_unhealthy(self):
        """Testing unhealthy food."""
        self.assertEqual(
            eat('pizza', healthy=False),
            "I'm eating pizza because we only live once!"
        )

    def test_sleep_good(self):
        """Testing sleep good!"""
        self.assertEqual(
            sleep(8),
            "I slept very good!"
        )

    def test_sleep_a_lot(self):
        """Testing sleep a lot!"""
        self.assertEqual(
            sleep(18),
            "I slept a lot!"
        )

    def test_sleep_a_few(self):
        """Testing sleep a few!"""
        self.assertEqual(
            sleep(4),
            "I slept a few!"
        )

    def test_is_funny(self):
        # Use this way when the function is not implemented. AssertionError: None != False
        # self.assertEqual(funny('Sérgio Malandro'), False)

        # Return True when the function is not implemented. None is considered False in this context.
        self.assertFalse(funny('Sérgio Malandro'))
        self.assertTrue(funny('Jim Carrey'), 'Jim Carrey should be funny...')


if __name__ == '__main__':
    unittest.main()

