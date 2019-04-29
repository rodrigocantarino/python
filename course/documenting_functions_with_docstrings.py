"""
Documenting functions with docstrings
"""


def powered_number(num=2, power_to=2):
    """
    Power a number
    :param num:
    :param power_to int:
    :return int:
    """
    return num**power_to


print(help(powered_number))

print(powered_number.__doc__)
