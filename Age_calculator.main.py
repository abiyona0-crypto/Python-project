#This is a small website that helps you to calculate ur Age in years, months, days, weeks, total days, hours, minutes with just one single input

print('~~~~~~~~~~~~~~AGE CALCULATOR~~~~~~~~~~~~~~')
print('Would you like to calculate your age in years, months, days, weeks, total days, hours, minutes?')
print('Please enter your date of birth in the format DD-MM-YYYY')
Year= int(input('Enter your year of birth: '))
Month= int(input('Enter your month of birth: '))
Day= int(input('Enter your day of birth: '))

#asking whether they want to calculate their age in years, months, days, weeks, total days, hours, minutes
print('1. Would you rather calculate your age in years')
print('2. Would you rather calculate your age in months')
print('3. Would you rather calculate your age in days')
print('4. Would you rather calculate your age in weeks')
print('5. Would you rather calculate your age in total days')
print('6. Would you rather calculate your age in hours')
print('7. Would you rather calculate your age in minutes')
choice = int(input('Enter your choice: '))

#age calculation
from datetime import date
today = date.today()
birth_date = date(Year, Month, Day)


#Their choice will determine what calculation will be done
# #IN YEARS
if choice == 1:
    print('You have chosen to calculate your age in years')
    age_in_years = today.year - birth_date.year
    print('You have been alive for: ', age_in_years)

#IN MONTHS
elif choice == 2:
    print('You have chosen to calculate your age in months')
    age_in_months = (today.year - birth_date.year) * 12 + today.month - birth_date.month
    print('You have been alive for: ', age_in_months)

#IN DAYS
elif choice == 3:
    print('You have chosen to calculate your age in days')
    age_in_days = (today - birth_date).days
    print('You have been alive for: ', age_in_days)

#IN WEEKS
elif choice == 4:
    print('You have chosen to calculate your age in weeks')
    age_in_weeks = (today - birth_date).days // 7
    print('You have been alive for: ', age_in_weeks)

#IN TOTAL DAYS
elif choice == 5:
    print('You have chosen to calculate your age in total days')
    age_in_total_days = (today - birth_date).days
    print('You have been alive for: ', age_in_total_days)

#IN HOURS
elif choice == 6:
    print('You have chosen to calculate your age in hours')
    age_in_hours = (today - birth_date).days * 24
    print('You have been alive for: ', age_in_hours)

#IN MINUTES
elif choice == 7:
    print('You have chosen to calculate your age in minutes')
    age_in_minutes = (today - birth_date).days * 24 * 60
    print('You have been alive for: ', age_in_minutes)

#You can also calculate what was the day you were born on
from datetime import date
today = date.today()
birth_date = date(Year, Month, Day)

print('Would you like to know which was the day when you were born on??')
Choice=input("1. Yes or 2. no")
if Choice == '1':
    day_of_week = birth_date.strftime("%A")
    print('You were born on a: ', day_of_week)
else:
    print('Thank you for using the Age Calculator')































