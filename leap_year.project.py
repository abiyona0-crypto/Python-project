#A programme to find out whether a specific year is leap year or not
print('~~~~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~~~~')
print('If you want to find out whether an year is leap year or not, THIS is the exact place to checck it!!!!')
print('Please enter the desired year')

#Asking for the users input
year = int(input('Enter a year: '))
if year % 4 == 0:
    print('Its a leap year!!')
else:
    print('Its not a leap year...')