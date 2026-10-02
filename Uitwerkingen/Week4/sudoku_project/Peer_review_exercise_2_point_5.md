# Peer Review: Sudoku Application (Exercise 2.5)

**Reviewer:** [Jouw Naam / Groepslid]  
**Auteur:** [Naam van de auteur]  
**Project:** Python Tkinter 9x9 Sudoku  

---

## Overall Verdict
De applicatie werkt goed en voldoet aan alle basiseisen van de opdracht. De code is netjes gestructureerd via een MVC-architectuur en de scheiding tussen logica (`board.py`, `solver.py`) en de GUI (`gui.py`) is helder doorgevoerd.

---

## Beoordeling op Kwaliteitscriteria

| Criterium | Score | Opmerkingen |
| :--- | :---: | :--- |
| **1. Correctness** | **4 / 5** | Het backtracking-algoritme werkt snel en correct. De validatiecontrole op rijen, kolommen en 3x3 blokken is foutloos. |
| **2. Readability** | **5 / 5** | Nette docstrings en typenotaties (`typing`). De code volgt de PEP 8 richtlijnen goed. |
| **3. User-Input Handling** | **4 / 5** | Invoering is beperkt tot cijfers 1-9 via `validatecommand`. Foutieve keuzes worden visueel (rood) en via de statusbalk aangegeven. |
| **4. GUI Design** | **4 / 5** | Overzichtelijke $9 \times 9$ layout met duidelijke 3x3 subgrid-randen. Functionele knoppen voor Hints, Oplossen en Laden. |
| **5. Edge-Case Handling** | **3.5 / 5** | Goede afhandeling van ongeldige bestandsformaten (`ValueError`). *Punt van aandacht:* Een onoplosbare Sudoku invoeren blokkeert tijdelijk de GUI tijdens het zoeken. |

---

## Verbeterpunten (Refactoring Tips)
1. **Performance bij onoplosbare borden:** Gebruik een `threading`-aanpak voor de solver in `gui.py` om te voorkomen dat het Tkinter-scherm bevriest bij complexe/onoplosbare puzzels.
2. **Reset-knop:** Voeg een knop toe om het bord snel terug te zetten naar de initiële staat.