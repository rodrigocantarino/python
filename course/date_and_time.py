"""

Date and Time

"""

import datetime

print(dir(datetime))

print('---------------------------------------')

print(datetime.MINYEAR)
print(datetime.MAXYEAR)

print('---------------------------------------')

# 2019-05-16 20:48:47.107852
print(datetime.datetime.now())

# datetime.datetime(year, month, day, hour, minutes, seconds, microseconds)
# datetime.datetime(2019, 5, 16, 20, 48, 47, 107904)
print(repr(datetime.datetime.now()))

print('---------------------------------------')

start = datetime.datetime.now()
print(start)

start = start.replace(year=2020, month=4, day=19, hour=20, minute=0, microsecond=123406)
print(start)

print('---------------------------------------')

event = datetime.datetime(2020, 4, 19, 0)

print(type(event))
print(event)

print('19/04/2020')

print('---------------------------------------')

birthday = input('Birthday (dd/mm/yyyy): ')
birthday = birthday.split('/')
print(birthday)

birthday = datetime.datetime(int(birthday[2]), int(birthday[1]), int(birthday[0]))
print(birthday)

print('---------------------------------------')

event = datetime.datetime.now()

print(event.year)
print(event.month)
print(event.day)
print(event.hour)
print(event.minute)
print(event.second)
print(event.microsecond)

print(dir(event))

