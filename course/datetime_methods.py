"""

Datetime methods

"""

import datetime, timeit, functools
from textblob import TextBlob


now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=3)))
today = datetime.datetime.today()

print('---------------------------------------')
print('---------------------------------------')
print(now)
print(type(now))
print(repr(now))
print('---------------------------------------')
print(today)
print(type(today))
print(repr(today))
print('---------------------------------------')

# Ex.: Changes on server tomorrow midnight
maintenance = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
print(maintenance)
print(maintenance.weekday())  # 0 = Monday -> 6 = Sunday

print('---------------------------------------')
print('---------------------------------------')
print('---------------------------------------')

birthday = '19/04/1985'  # input('Birthday (dd/mm/yyyy): ')
print('Birthday (dd/mm/yyyy):', end=' ')
birthday = birthday.split('/')

birthday = datetime.datetime(year=int(birthday[2]), month=int(birthday[1]), day=int(birthday[0]))
print(birthday)
print(birthday.weekday())  # 4 = Friday

print('---------------------------------------')

birthday = '19/04/1985'  # input('Birthday (dd/mm/yyyy): ')
birthday = datetime.datetime.strptime(birthday, '%d/%m/%Y')

print(f"datetime.datetime.strptime(birthday, '%d/%m/%Y'): {birthday}")

print('---------------------------------------')
print('---------------------------------------')
print('---------------------------------------')
print('---------------------------------------')

today = datetime.datetime.today()
today.strftime('%d/%m/%y')

# See: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print(today.strftime('%d/%m/%y'))
print(today.strftime('%d/%m/%Y'))
print(today.strftime('%d/%B/%Y'))
print(today.strftime('%d/%b/%Y'))

print('---------------------------------------')


def format_date(date):
    return f"{today.day} de {TextBlob(date.strftime('%B')).translate(to='pt-br')} de {today.year}"


print(format_date(today))

print('---------------------------------------')
print('---------------------------------------')
print('---------------------------------------')

print('Working just with hour: ')

print(datetime.time())
print(datetime.time(12, 30, 0))

print('****************************************')

# Loop for
time = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(time)

# List Comprehension
time = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(time)

# Map
time = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(time)

print('****************************************')


def test(n):
    summ = 0
    for num in range(n * 200):
        summ = summ + num ** num + 5
    return summ


print(timeit.timeit(functools.partial(test, 2), number=10000))  # It takes 13.193370 seconds to execute
