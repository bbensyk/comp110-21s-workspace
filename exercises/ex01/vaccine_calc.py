"""A vaccination calculator."""

__author__ = "YOUR PID HERE"

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
Pop: int = int(input("Population: "))
DoAd: int = int(input("Doses Administered: "))
DpD: int = int(input("Doses per day: "))
TpV: int = int(input("Target percent vaccinated: "))

dah: int = DoAd / 2
dpdh: int = DpD / 2
Percent: float = TpV / 100

Target: float = Pop * Percent - dah
Days: float = Target / dpdh

a: int = round(Days)

today: datetime = datetime.today()
b: timedelta = timedelta(a)
final: datetime = today + b

Tp: str = str(TpV)
A: str = str(a)

wwr = "We will reach "
vi = "% vaccination in "
dwf = " days, which falls on "
date = (final.strftime("%B %d, %Y"))

output = wwr + Tp + vi + A + dwf + date 

print(output)