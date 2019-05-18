import unittest

from robot import Robot


class RobotTests(unittest.TestCase):

    def setUp(self):
        print('Executing self().')
        self.daileon = Robot('Giant Warrior DAILEON', battery=50)

    def test_charge_battery(self):
        self.daileon.charge_battery()
        self.assertEqual(self.daileon.battery, 100)

    def test_greattings(self):
        self.assertEqual(
            self.daileon.greattings(),
            "BEEP BOOOP,BEEP BOOOP, I AM GIANT WARRIOR DAILEON the Robot!!! Take me to your Leader!!!"
        )

        self.assertEqual(self.daileon.battery, 49, "The battery should be 49%.")

    def tearDown(self):
        print('Executing tearDown().')


if __name__ == '__main__':
    unittest.main()