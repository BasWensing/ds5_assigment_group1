# Opdracht 2
# Reeks toevoegen met getallen: An,c, A0 moeten erin. 
# Reeks moet binnen de [-1.5 0.5] voor de x en [-1 1] voor de y. Dennis.

import numpy as np
import pandas as pd
c = [] # maakt een lijst aan voor alle c's die we nodig hebben

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def draw_mandel(width): # Definieert hoe groot de afbeelding moet zijn
    plt.figure(figsize =(width,width)) # Definieert hoe groot de afbeelding moet zijn volgens en past dit toe and de figure

width = 200
x = []
y = []

x_min = -1.5
x_max = 0.5
y_min = -1 
y_max = 1

def generate_x_en_y(width): # Genereert de benodige x en y
    x.extend(np.linspace(x_min, x_max, width)) # Maakt alle benodige x   

    y.extend(np.linspace(y_min, y_max, width)) # Maakt alle benodige y
generate_x_en_y(width)

def complex(x,y): # Definieert de complex functie   
    index1 = 0
    for x_value in x: # Pakt alle x van de x lijst
        for y_value in y: # Pakt alle y van de y lijst
            c.append(x_value + y_value * 1j) # Rekened de x + y*i uit en voegt deze toe aan een list
            index1 += 1

complex(x,y)
len(c)

# Stap 1.1 parameters toevoegen

n = 10 # Aantal gegenereerde formulewaarden op interval [x_min, x_max
a0 = 0
step = abs((x_max - x_min) / n)
index = 0 # Index itereren over lijst met functiewaarden

print(c)
sequence_mandelbrot = []
max_stappen = 100
# Stap 2: sequence genereren van n getallen in range x = [-1.5, 0.5]
for c_waarde in c:
    an_oud = 0  # Op 0 beginnen voor elk nieuw complex getal
    n = 0
    # oude waarde checken
    while abs(an_oud) <= 2 and n < max_stappen:
        an_nieuw = an_oud**2 + c_waarde  # Nieuwe waarde berekenen
        an_oud = an_nieuw                # Update an_oud voor volgende stap
        n += 1 # n = n+1
    sequence_mandelbrot.append(abs(an_oud)) # Afbeelding 90 graden draaien
print(sequence_mandelbrot)

# figuur tekenen met functie draw_mandel
def draw_mandel_heatmap(width):
    grid = np.array(sequence_mandelbrot).reshape(width,width)# figuur met 90 graden naar links draaien
    grid_gedraaid = np.rot90(grid) # figuur met 90 graden naar links draaien
    plt.figure(figsize =(8,6))
    plt.title('Visualisatie van Mandelbrot (Heatmap)',fontsize=20)
    kleuren = LinearSegmentedColormap.from_list(
        "zwart_blauw",
        ["black", "blue"])

    plt.imshow(
        grid_gedraaid,
        cmap=kleuren,
        vmin=0,
        vmax=2
    )

    plt.colorbar(label="Waarde |aₙ|")
    plt.xlabel('x')
    plt.ylabel('y')

    plt.tight_layout()
    plt.show()

draw_mandel_heatmap(200)


# Opdracht 3.1: parameters
k = 5 # aantal nodes rond 1 middelpunt. Dennis
di = [2, 1, 1, 3, 2] # aantal pagina-ranks die nummer i bezit. Dennis
sum_di = sum(di) # som van alle pagina-ranks. Dennis
pi = # waarschijnlijkheid dat pagina k+i linkt met punt i. Dennis
M = 4 # al bestaande, verschillende pagina's van het sternetwerk. Dennis
N = 400 # aantal webpagina's. Dennis

# Opdracht 3.2: parameters
G = # een NetworkX-grafiek
alpha = 0.85 # damp-parameter voor functie PageRank. Dennis
personalization = dict{} # 'Keys': iedere node in grafiek, 'value': nonzero-personalisatiewaarde voor iedere node. Default: 'None'. Dennis
weight = # Keys: edge-data sleutel om als gewicht te gebruiken. Als het 'None' is, worden de gewichten op 1 gezet. Default: 'weight'. Dennis
pagerank = dict() # Dictionary van nodes met 'PageRank' als 'value' (waarde). 'Return'-waarde. Dennis
