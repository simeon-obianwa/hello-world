# Hello World Software with a friendly age calculator

print("Hello World!")

name = input("What is your name? ")
age = int(input("How old are you? "))

years_to_120 = 120 - age
birth_year = 2026 - age

print(f"Hello, {name}!")
print(f"You were likely born in {birth_year}.")
print(f"You will turn 120 in about {years_to_120} years.")

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")