# Blackjack in Python

Deze implementatie speelt een enkele ronde standaard Blackjack.

## Prompt voor een LLM

Gebruik de volgende tekst om een LLM opdracht te geven voor dit programma:

```text
Je bent een ervaren Python-programmeur. Schrijf een eenvoudige, goed leesbare
consoleversie van een enkele ronde Blackjack.

Vereisten:
- Gebruik een standaard deck van 52 kaarten.
- Gebruik de suits klaveren, ruiten, harten en schoppen.
- Gebruik de kaartwaarden 2 t/m 10, boer, vrouw, heer en aas.
- Schud het deck aan het begin van de ronde.
- Vervang kaarten niet nadat ze zijn gedeeld; verwijder getrokken kaarten uit
    het deck.
- Deel de speler en dealer elk twee kaarten.
- Toon voor iedere beslissing de volledige hand van de speler en dealer en de
    som van beide handen.
- De speler mag alleen `hit` of `stand` invoeren.
- Accepteer hoofdletters en kleine letters, maar toon bij iedere andere invoer
    een herinnering en vraag opnieuw om invoer.
- Bereken een aas als 11, behalve wanneer de hand daardoor boven 21 komt; dan
    telt het aas als 1.
- Laat de dealer kaarten trekken zolang de score lager is dan 17.
- Bepaal winst, verlies, blackjack, bust en gelijkspel.
- Toon aan het einde de volledige handen, beide sommen en een duidelijke
    uitkomst voor de speler.

Gebruik losse functies voor het maken van het deck, kaarten trekken,
handwaarden berekenen, de spelerbeurt, de dealerbeurt en het bepalen van de
winnaar. Voeg een `main()`-functie toe en gebruik een
`if __name__ == "__main__":`-blok.

Geef eerst kort aan hoe de oplossing werkt en geef daarna de volledige Python-
code in één codeblok. Gebruik alleen de Python-standaardbibliotheek.
```