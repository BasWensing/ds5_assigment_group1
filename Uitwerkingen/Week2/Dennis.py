# Opdracht 2
# Reeks toevoegen met getallen: An,c, A0 moeten erin. 
# Reeks moet binnen de [-1.5 0.5] voor de x en [-1 1] voor de y. Dennis.

import numpy as np
import pandas as pd
c = [] # maakt een lijst aan voor alle c's die we nodig hebben
def complex(x,y): # Definieert de complex functie   
    c.append(x + y*1j) # Rekent de x + y*i uit en voegt deze toe aan een list


import matplotlib.pyplot as plt
def draw_mandel(width): # Definieert hoe groot de afbeelding moet zijn
    plt.figure(figsize =(width,width)) # Definieert hoe groot de afbeelding moet zijn volgens en past dit toe and de figure

# Stap 1.1 parameters toevoegen
x_min = -1.5
x_max = 0.5
y_min = -1 
y_max = 1
n = 10 # Aantal gegenereerde formulewaarden op interval [x_min, x_max]
a_n = a_n-1+c
a0 = 0
step = abs((x_max - x_min) / n)
print(step)
index = 0 # Index itereren over lijst met functiewaarden

# Stap 1.2: sequence van n = 1000000 getallen 
x = np.arange(x_min, (x_max+step), step)
print(x)

# Stap 2: sequence genereren van 10000 getallen in range x = [-1.5, 0.5]
for i in x:

