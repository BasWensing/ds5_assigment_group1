# Opdracht 2
# Reeks toevoegen met getallen: An,c, A0 moeten erin. 
# Reeks moet binnen de [-1.5 0.5] voor de x en [-1 1] voor de y. Dennis.

import numpy as np
import pandas as pd
c = [] # maakt een lijst aan voor alle c's die we nodig hebben

import matplotlib.pyplot as plt
def draw_mandel(width): # Definieert hoe groot de afbeelding moet zijn
    plt.figure(figsize =(width,width)) # Definieert hoe groot de afbeelding moet zijn volgens en past dit toe and de figure

import numpy as np
c = [] # maakt een lijst aan voor alle c's die we nodig hebben
def complex(x,y): # Definieert de complex functie   
    for x_value in x: # Pakt alle x van de x lijst
        for y_value in y: # Pakt alle y van de y lijst
            c.append(x_value + y_value * 1j) # Rekened de x + y*i uit en voegt deze toe aan een list 

complex(x,y)
len(c)
print(c)

import numpy as np

x = []
y =[]

def generate_x_en_y(width): # Genereert de benodige x en y
    x.extend(np.linspace(-1.5, 1,width)) # Maakt alle benodige x   

    y.extend(np.linspace(-1, 1, width)) # Maakt alle benodige y
generate_x_en_y(200)

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


