# Python Program to Get Current Date and Time

from datetime import date
from datetime import datetime

today = date.today()
print(today)

time = datetime.now()
print(time.strftime("%B %d, %Y %H:%M:%S"))
