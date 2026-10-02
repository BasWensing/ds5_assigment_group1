# LLM-prompt: uitleg bij de Blackjack-code

Gebruik deze prompt met de inhoud van `Dennis4.py` om een begrijpelijke uitleg van het huidige programma te laten maken. Plak de code onderaan de prompt of voeg het Python-bestand toe aan de LLM-conversatie.

```text
Je bent een geduldige Python-docent. Leg de meegeleverde Blackjack-code uit
in begrijpelijk Nederlands voor iemand die Python leert.

Schrijf de uitleg over de code zoals die werkelijk is aangeleverd. Verzin geen
functionaliteit en beweer niet dat een functie iets doet als dat niet uit de
code blijkt. Schrijf geen nieuwe implementatie en pas de code niet aan.

Gebruik deze indeling:
1. Doel van het programma: leg in enkele zinnen uit wat de speler kan doen en
   wat er aan het einde wordt getoond.
2. Belangrijke gegevens: leg uit hoe kaarten als `(waarde, soort)` worden
   voorgesteld en waarvoor de constanten voor soorten, kaartwaarden en
   plaatjes worden gebruikt.
3. Functies: beschrijf in de volgorde van de code wat iedere functie ontvangt,
   wat zij doet en wat zij teruggeeft of afdrukt.
4. Spelverloop: beschrijf stap voor stap wat er gebeurt vanaf het starten van
   `main()` tot en met de einduitslag.
5. Voorbeelden: reken ten minste een hand met een aas voor, bijvoorbeeld aas
   plus 7 en aas plus 9 plus 5. Laat zien waarom de aaswaarde zo nodig van 11
   naar 1 wordt verlaagd.
6. Beperkingen: benoem kort wat de code niet apart afhandelt of wat afwijkt
   van standaard Blackjack-regels.

Leg Python-begrippen zoals tuple, lijst, functie, `while`-lus, `if`-voorwaarde,
`append()` en `pop()` kort uit wanneer ze voor het begrip nodig zijn. Houd de
taal eenvoudig, maar laat belangrijke details niet weg. Gebruik geen lange
technische uitweidingen.

Let in het bijzonder op deze feitelijke details van de aangeleverde code:
- `create_deck()` maakt 52 kaarten met vier soorten en dertien waarden.
- `calculate_hand_value()` telt plaatjes als 10 en verlaagt azen van 11 naar 1
  zolang de totale waarde boven 21 ligt.
- `deal_card()` verwijdert de laatste kaart uit de decklijst en geeft een
  `ValueError` als de lijst leeg is.
- De speler mag `hit` of `stand` invoeren; invoer wordt getrimd en naar kleine
  letters omgezet. Andere invoer toont een herinnering.
- De dealer trekt zolang de handwaarde lager is dan 17.
- `determine_winner()` vergelijkt handwaarden, behandelt bust en gelijkspel,
  maar herkent natuurlijke Blackjack (21 met precies twee kaarten) niet als
  aparte uitkomst.
- De volledige handen en sommen worden getoond; er wordt geen dealerkaart
  verborgen.

Sluit af met een korte samenvatting van de belangrijkste functies. Als een
observatie hierboven niet overeenkomt met de meegeleverde code, volg dan de
code en meld het verschil.

Python-code:
[PLAK HIER DE VOLLEDIGE INHOUD VAN Dennis4.py OF VOEG HET BESTAND TOE]
```
