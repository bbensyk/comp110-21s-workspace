"""A vaccination calculator."""

__author__ = "730442945"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
pop: int = int(input("Population: "))
doses: int = int(input("Doses Administered: "))
per_day: int = int(input("Doses per day: "))
target_percent: int = int(input("Target percent vaccinated: "))

doses_halved: int = doses / 2
half_per_day: int = per_day / 2
percent: float = target_percent / 100

target: float = pop * percent - doses_halved
days: float = target / half_per_day

days_number: int = round(days)

today: datetime = datetime.today()
day_change: timedelta = timedelta(days_number)
final: datetime = today + day_change

target_string: str = str(target_percent)
days_string: str = str(days_number)

wwr = "We will reach "
vi = "% vaccination in "
dwf = " days, which falls on "
date = (final.strftime("%B %d, %Y"))

output = wwr + target_string + vi + days_string + dwf + date 

print(output)