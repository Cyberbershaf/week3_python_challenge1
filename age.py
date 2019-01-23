
print("This program determines whether someone is a minor, youth or elder")

current_year = 2019
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year

if age < 18:
    print("You are minor!")
elif age >= 18 and age <= 36:
    print("You are a youth!")
else:
    print("You are elder!")

print("Done, Thank you!")