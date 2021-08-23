#/usr/bin/python3
#
#Class
print("=" * 100)
print("10.8 Dates and Times")
print("=" * 100)
#dates are easily constructed and formatted

from datetime import date
now = date.today()
print(now)
print(now.strftime("%Y-%m-%d %T"))

birthday = date(1970,8,22)
age = now - birthday
print(age.days/365)

