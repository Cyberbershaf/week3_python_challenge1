
import datetime

print("This program determines whether someone is a minor, youth or elder")

current_date = datetime.date.today() #Getting current date
current_year = current_date.year #Converting current date to year
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year

if age < 18:
    print("You are minor!")
elif age >= 18 and age <= 36:
    print("You are a youth!")
else:
    print("You are elder!")

print("Done, Thank you!")

#By MUYIVU SHAFIQ
