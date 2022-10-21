
from datetime import date
name = input("Enter your name: ") # user input
current_age = int(input("Enter your age: ")) # user input
#calculating the 100th year, considering 2020 as the current year
hundredth_year = 2022 + (100 - current_age)
print(f'{name} will become 100 years old in the year {hundredth_year}.')
