"""

Datetime Delta

"""

import datetime

start_date = datetime.datetime.now()
end_date = datetime.datetime(2020, 1, 30, 9, 0, 0)

delta_date = end_date - start_date

print(delta_date)
print(f"{delta_date.days} days!!!")
print(f"{delta_date.seconds} seconds!!!")
print(type(delta_date))

print('---------------------------------------')


bank_slip_generated = datetime.datetime.now()
bank_slip_rule = datetime.timedelta(days=5)

bank_slip_due_date = bank_slip_generated + bank_slip_rule

print(f"bank_slip_generated: {bank_slip_generated}")
print(f"bank_slip_rule; {bank_slip_rule}")
print(f"bank_slip_due_date: {bank_slip_due_date}")

