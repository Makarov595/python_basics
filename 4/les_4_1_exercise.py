import sys

name, production_in_hours, rate_per_hour, premium = sys.argv
print(float(production_in_hours) * float(rate_per_hour) + float(premium))
