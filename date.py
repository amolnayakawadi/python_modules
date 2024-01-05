### Datetime

import datetime

d = datetime.date(2024,1,5)
print(d)
print(type(d))


today = datetime.date.today()
print(today)

t = datetime.time(12,25,45)
print(t)
print(type(t))

now = datetime.datetime.now()
print(now)

diff = datetime.timedelta(days = 100, hours=20)
print(diff)

info = (d + diff)
print(info)

data = now.strftime("%B")
print(data)