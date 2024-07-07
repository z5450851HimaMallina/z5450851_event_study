# EXERCISE-1 pay calculator

hours = input()
hours = float(hours)

if hours <= 35:
    pay = hours * 51.45

else:
    regular_pay = 35 * 51.45
    overtime = (hours - 35) * 88.9
    pay = regular_pay + overtime

print(pay)



















