# Opdracht 1
"""Print the average grade. Dennis"""
print(f"Average Grade: {average}")

"""Print lines. Dennis"""
print("--------------------")

'''Add each record to 'filtered_records' in the df 'Records' if the number is higher than 80.0. Dennis'''
filtered_records = [record for record in records if float(record['Grade']) >= 80.0]

'''Print "Student Report". Dennis '''
print("Student Report")

'''Print lines. Dennis'''
print("--------------")


for record in filtered_records:
    '''For each record, print name. Dennis'''
    print(f"Name: {record['Name']}")

    '''For each record, print grade. Dennis'''
    print(f"Grade: {record['Grade']}")

    '''Print lines. Dennis'''
    print("--------------------")

# Opdracht 2
# Reeks toevoegen met getallen: An,c, A0 moeten erin. 
# Reeks moet binnen de [-1.5 0.5] voor de x en [-1 1] voor de y. Dennis.
import pandas as pd
import numpy as np

# Stap 1: Sequence toevoegen
x_min = -1.5
x_max = 0.5
y_min = -1 
y_max = 1
n = 10000 # Aantal gegenereerde formulewaarden op interval [x_min, x_max]
c = x + y*i # Complexe set
index = 0 # Index itereren over lijst met functiewaarden

# Stap 2: lijst aanmaken voor functiewaarden
mandelbrot_numbers = []

# Stap 3: sequence genereren van 10000 getallen in range x = [-1.5, 0.5]
for index in range(x_min, x_max, n):
    mandelbrot_numbers.append(mandelbrot_numbers[index-1])**2 + c # Mandelbrot set
    