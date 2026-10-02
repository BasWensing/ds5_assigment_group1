# LLM-opdracht: Blackjack-componenten

Kopieer de prompt hieronder naar een LLM om de bestaande Blackjack-projectstructuur in te vullen.

```text
Je bent een ervaren Python-programmeur. Implementeer een eenvoudige, modulaire
consoleversie van een enkele ronde standaard Blackjack in de bestaande
projectbestanden. Inspecteer eerst de bestaande bestanden en behoud de huidige
projectstructuur. Verplaats of hernoem geen bestanden.

Projectstructuur:
- blackjack/cards.py: kaarttypen, deck maken, schudden en kaarten trekken.
- blackjack/game.py: handwaarde, spelbeurten en uitslag bepalen.
- blackjack/cli.py: console-uitvoer, spelerinvoer en startpunt.
- blackjack/__init__.py: alleen noodzakelijke publieke exports.
- blackjack/examples/blackjack_example.py: klein voorbeeld dat de publieke
	interface gebruikt.
- blackjack/tests/test_blackjack.py: tests voor de spelregels en randgevallen.
- blackjack/Blackjack.md: bestaande spelbeschrijving; behoud deze en werk deze
	alleen bij als dat nodig is om de implementatie correct te documenteren.

Spelvereisten:
- Gebruik alleen de Python-standaardbibliotheek.
- Gebruik een standaard deck van 52 unieke kaarten.
- Gebruik de suits klaveren, ruiten, harten en schoppen.
- Gebruik de kaartwaarden 2 t/m 10, boer, vrouw, heer en aas.
- Schud het volledige deck aan het begin van iedere ronde.
- Verwijder iedere getrokken kaart uit het deck; kaarten worden niet vervangen.
- Deel de speler en dealer ieder twee kaarten.
- Toon voor iedere beslissing de volledige hand van speler en dealer en de som
	van beide handen. Verberg dus geen dealerkaart.
- Accepteer voor de speler uitsluitend `hit` en `stand`, zonder onderscheid
	tussen hoofdletters en kleine letters en met eventuele spaties aan de randen
	genegeerd.
- Toon bij iedere andere invoer een korte herinnering en vraag opnieuw. Toon
	de handen en sommen opnieuw voordat de volgende invoer wordt gevraagd.
- Een boer, vrouw en heer tellen als 10. Een aas telt als 11 tenzij de hand dan
	boven 21 uitkomt; verlaag in dat geval een of meer azen naar 1.
- De dealer trekt zolang zijn handwaarde lager is dan 17 en staat op 17 of
	hoger.
- Bepaal en meld winst, verlies, gelijkspel en bust. Herken een blackjack als
	een hand van precies twee kaarten met waarde 21.
- Toon aan het einde altijd de volledige handen, de sommen en een duidelijke
	uitkomst voor de speler.
- Speel een enkele ronde per programma-uitvoering. Voeg geen inzet, saldo,
	multiplayer of grafische interface toe.

Componentgrenzen:
1. `cards.py` beheert de representatie van kaarten en het deck. Gebruik een
	 eenvoudige consistente kaartrepresentatie die in de andere modules
	 geïmporteerd kan worden. Een kaart trekken verwijdert de kaart uit het deck.
2. `game.py` bevat de spelregels en moet waar praktisch mogelijk onafhankelijk
	 zijn van `input()` en `print()`. Gebruik hier functies voor handwaarde,
	 blackjack/bust en uitslag, plus de speler- en dealerbeurt.
3. `cli.py` verzorgt de presentatie en invoer. Houd het schermgedrag hier en
	 laat een `main()`-functie precies een ronde uitvoeren. Gebruik een
	 `if __name__ == "__main__":`-blok zodat de CLI als module gestart kan worden.
4. Het voorbeeld gebruikt de publieke projectinterface; dupliceer geen
	 spelregels in het voorbeeld.
5. De tests gebruiken vaste handen en gecontroleerde decks. Vertrouw niet op
	 willekeurige shuffle-uitkomsten of interactieve toetsenbordinvoer.

Tests moeten ten minste controleren:
- het deck bevat 52 unieke kaarten;
- trekken verwijdert een kaart en een leeg deck wordt duidelijk afgehandeld;
- numerieke kaarten, plaatjes, een aas en meerdere azen correct scoren;
- speler-bust, dealer-bust, winst, verlies, gelijkspel en blackjack;
- dealer trekt onder 17 en staat op 17 of hoger;
- alleen `hit` en `stand` worden geaccepteerd en ongeldige invoer leidt tot een
	nieuwe vraag.

Werkwijze en antwoord:
- Maak geen nieuwe projectbestanden aan tenzij een bestaande bestandsindeling
	het echt onmogelijk maakt om de vereisten uit te voeren.
- Schrijf de implementatie in de genoemde bestaande bestanden; geef niet alleen
	codevoorbeelden in je antwoord.
- Voer de beschikbare tests uit. Als tests niet uitvoerbaar zijn, zeg dat
	expliciet en verzin geen testresultaten.
- Geef na afloop kort aan welke bestanden zijn aangepast en welke controles
	zijn uitgevoerd.
```

De oorspronkelijke spelbeschrijving staat in [Blackjack.md](../Blackjack.md).

