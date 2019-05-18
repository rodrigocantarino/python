"""
Unittest
"""


class Robot:

    def __init__(self, name, battery=100, ability=[]):
        self.__name = name
        self.__battery = battery
        self.__ability = ability

    @property
    def name(self):
        return self.__name

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, battery):
        self.__battery = battery

    @property
    def ability(self):
        return self.__ability

    def charge_battery(self):
        self.__battery = 100

    def greattings(self):
        if self.__battery > 0:
            self.__battery -= 1
            return f"BEEP BOOOP,BEEP BOOOP, I AM {self.__name.upper()} the Robot!!! Take me to your Leader!!!"
        return "Battery low! I need a charge!!!"

    def learn_ability(self, new_ability, cost):
        if self.__battery >= cost:
            self.__ability.append(new_ability)
            self.__battery -= cost
            return f"Ability {self.__ability.upper()} successfully learned!"
        return f"Battery low to learn a new ability! Charge me first!!!"



