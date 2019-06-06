# generic date testing -- not used in program
from datetime import datetime, date, timedelta

def main():
    #get today's date
    today = date.today()
    print("Today's date is", today)
    today = datetime.now()
    print("Today's datetime:", today)
    print("Time only:", datetime.time(datetime.now()))

today = date.today()
print ("date parts:", today.day, today.month, today.year)
print ("Day of week number:", today.weekday())

wd = date.weekday(today)
days = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print ("Today is day number %d", wd)
print("Which is a " + days[wd])

now = datetime.now()
print ("Full year: ", now.strftime("%Y"))
print ("year: ", now.strftime("%y"))
print(now.strftime("%a, %A, %d, %D, %b, %B, %y, %Y "))

# local date and time
print("Local time")
print(now.strftime("%c"))
print(now.strftime("%X"))
print(now.strftime("%x"))
print("12 or 24 hour time:")
print(now.strftime("%I:%M:%S %p"))
print(now.strftime("%H:%M"))

# time delta function
print(timedelta(days=365, hours=8, minutes=15))

print("Today is: " + str(datetime.now()))
print("One year from now it will be: " + str(datetime.now() + timedelta(days=365)))
print("One week and four days from now is: " + str(datetime.now() + timedelta(weeks=1, days=4)))


today = date.today()
nyd = date(today.year, 1, 1)
if nyd < today:
    print("New Year's day went by %d days ago" %((today-nyd).days))

myBday = date(1951, 11, 14)
print("My Birthday was %d years ago" % ((today-myBday).days))
print("My Birthdate: ", myBday)
days_passed = (today-myBday).days
print("My years: ", days_passed // 365)
print("My years: ", days_passed / 365)













if __name__=="__main__":
    main()