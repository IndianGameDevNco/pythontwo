from datetime import datetime, timedelta
from os import system, name as osname
from time import sleep as wait

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

while True:
    try:
        year = int(input('Enter the year you were born: '))
        month = int(input('Enter the month you were born (1-12): '))
        day = int(input('Enter the day you were born: '))
        birthdate = datetime(year, month, day)
        
        # Handle February 29 for non-leap years
        if birthdate.month == 2 and birthdate.day == 29:
            if not datetime(year, 3, 1).replace(day=28) == datetime(year, 2, 28):
                raise ValueError("Invalid date: Not a leap year")
        break
    except ValueError as e:
        print(f'\nInvalid date: {e}')
        wait(1)
        system('cls' if osname == 'nt' else 'clear')

today = datetime.now()

# Calculate age
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age = today.year - birthdate.year - 1
else:
    age = today.year - birthdate.year

print(f'\nYou were born on a {week[birthdate.weekday()]} and are {age} years old.\n')

# Calculate birthday occurrences
daymap = {day: 0 for day in week}

for y in range(birthdate.year, today.year + 1):
    try:
        bd = datetime(y, birthdate.month, birthdate.day)
    except ValueError:
        # Handle February 29 for non-leap years
        bd = datetime(y, 3, 1)
    daymap[week[bd.weekday()]] += 1

wait(1)
print(f'''\nYour birthday has occurred:
    {daymap['Monday']} times on Monday,
    {daymap['Tuesday']} times on Tuesday,
    {daymap['Wednesday']} times on Wednesday,
    {daymap['Thursday']} times on Thursday,
    {daymap['Friday']} times on Friday,
    {daymap['Saturday']} times on Saturday,
    {daymap['Sunday']} times on Sunday.\n''')

# Calculate next birthday
next_bday = datetime(today.year, birthdate.month, birthdate.day)
if next_bday < today:
    next_bday = datetime(today.year + 1, birthdate.month, birthdate.day)

while True:
    try:
        delta = next_bday - datetime.now()
        if delta.days < 0:
            next_bday = datetime(next_bday.year + 1, birthdate.month, birthdate.day)
            continue
            
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print('\033[?25l', end='')
        print(
            f'Next birthday in: '
            f'{days} days, '
            f'{hours:02} hours, '
            f'{minutes:02} minutes, '
            f'{seconds:02} seconds'.ljust(80),
            end='\r'
        )
        wait(1)
    except KeyboardInterrupt:
        break