# G.I.P Richtpunt campus Ninove Zottegem
G.I.P Victor Limpens 6EE


## **G.I.P Project CanSat**

Wat is CanSat?

- Een CanSat is een samenvoeging van de woorden "Can" en "Satellite" (blikje en satelliet). Het is een educatief en onderzoeksproject dat wordt gebruikt in de ruimtevaart en wetenschappelijke gemeenschap. Het doel ervan is om studenten en onderzoekers in staat te stellen te experimenteren met ruimtevaarttechnologie en wetenschappelijke metingen te verrichten met een klein, goedkoop en eenvoudig te lanceren apparaat.

- Een CanSat is meestal ter grootte van een blikje frisdrank of iets groter. Het bevat sensoren en apparatuur die gegevens kunnen verzamelen, zoals temperatuur, luchtdruk, hoogte, snelheid en meer, terwijl het in de lucht is. Dit apparaat wordt dan gelanceerd in de ruimte met behulp van een raket of een ballon.

- Waarom is dit belangrijk? Ten eerste is het een geweldige leerervaring voor studenten in technische en wetenschappelijke vakgebieden. Ze kunnen leren over ruimtevaarttechnologie, dataverzameling en analyse, en teamwork terwijl ze hun eigen CanSat-missie plannen en uitvoeren.

- Bovendien kunnen CanSats nuttige gegevens opleveren voor verschillende toepassingen, zoals weermetingen, milieuonderzoek of technologietests. Het zijn als kleine, betaalbare satellieten die kortstondige missies kunnen uitvoeren en waardevolle informatie kunnen verzamelen.

- Dus, CanSat is een educatief en onderzoeksinitiatief waarmee studenten en onderzoekers praktische ervaring kunnen opdoen in de ruimtevaart en wetenschap, terwijl ze tegelijkertijd gegevens verzamelen die nuttig kunnen zijn voor verschillende toepassingen.

****

## inhoudsopgave
<a name="inhoudsopgave"></a>

| File      | Inhoud                 |
|    ---    |          ---           |
| `1.0`     | schetsen               |
| `1.0.1`   |  cansat                |
| `1.0.2`   |  pcb                   |
| `1.0.3`   |  indeling              |
| `1.0.4`   |  elektrische schema's  |
|           |                        |
| `2.0`     | tekenigen officieel    |
| `2.0.1`   | cansat                 |
| `2.0.2`   | pcb                    |
| `2.0.3`   | indeling               |
| `2.0.4`   | elektrische schema's   |


   Delen    | 1.0 | 1.0.1 | 1.0.2 | 1.0.3 | 1.0.4 | 2.0 | 2.0.1 | 2.0.2 | 2.0.3 | 2.0.4 
   ---      | --- | ---   | ---   |---    |---    | --- |---    |---    |---    |--- 
   Status   |❌|❌|❌|❌|❌|❌|❌|❌|❌|❌ 
   Teamlid   |❌|❌|❌|❌|❌|❌|❌|❌|❌|❌ 


|TAAK|	NAAM |
|    ---    |          ---           |
|COMMUNICATIE|	Stijn |
|3D PRINTING|	Siebe|
|PROGRAMEREN|	Victor|
|SOLDEREN|	Xander|
|MONTEREN|	Gilles|
|DATA COMMUNICATIE|	Gilles en Xander|
|PARACHUTE|	Victor en Stijn|
|BEGELEIDER|	Van Eesbeek|

   

****

1. **PI DS18B20 Temperatuursensor**:
   - Datasheet: [DS18B20 Datasheet](https://www.digikey.be/en/htmldatasheets/production/1668/0/0/1/ds18b20z-t-r)
   - Handleiding: [Raspberry Pi DS18B20 Temperatuursensor Handleiding](https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/)
   
   Deze sensor wordt gebruikt om de temperatuur te meten en kan worden aangesloten op een Raspberry Pi.

2. **Luchtdruk en Temperatuur**:
   - Bron: [BMP180 Sensor](https://raspberrytips.nl/bmp180/)
   
   De BMP180-sensor wordt vaak gebruikt om zowel luchtdruk als temperatuur te meten. Deze kan worden aangesloten op een Raspberry Pi.

3. **GPS-ontvanger met Raspberry Pi 4**:
   - Handleiding: [Hoe een GPS-ontvanger te gebruiken met Raspberry Pi 4](https://maker.pro/raspberry-pi/tutorial/how-to-use-a-gps-receiver-with-raspberry-pi-4)
   - code uitleg: [link](https://microcontrollerslab.com/neo-6m-gps-module-raspberry-pi-pico-micropython/)

   Deze handleiding legt uit hoe je een GPS-ontvanger kunt aansluiten op een Raspberry Pi 4 om GPS-coördinaten te verkrijgen.

4. **Gelaagde Opstelling**:
     - Eerste laag: Temperatuur- en luchtdrukmeting en andere sensoren.
     - Tweede laag: GPS en coördinaten.
     - Derde laag: Raspberry Pi en opslag.
     - Vierde laag: Radiocommunicatie.

5. **Radiocommunicatie op CanSat**:
   - Gebruik een radiomodule op je CanSat om gegevens te verzenden. Je hebt waarschijnlijk een UHF- of VHF-zender nodig, afhankelijk van de gewenste afstand en regelgeving in je gebied.

6. **Ontwikkel de zelfgemaakte satelliet**:
   - Ontwerp en bouw een kleine satelliet die in staat is om de signalen van de CanSat op te vangen. Dit vereist kennis van satelliettechnologie en communicatiesystemen.

7. **Grondstation**:
   - Stel een grondstation op met een antenne en een ontvanger die in staat is om de signalen van de zelfgemaakte satelliet te ontvangen. Je hebt software nodig om de gegevens te decoderen.

8. **Frequentiecoördinatie**:
   - Zorg ervoor dat je de juiste frequentiecoördinatie hebt voor je radiosignalen om storingen te voorkomen en wettelijke voorschriften te volgen.

9. **Raspberry Pico**:
   - Bron: [Raspberry Pico](https://picockpit.com/raspberry-pi/nl/alles-over-de-raspberry-pi-pico/)
   - Bron: [Raspberry Pico Documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

10. **gas sensor (MQ-X)**
   - Bron: [gas sensor (MQ-X)](https://tutorials-raspberrypi.com/configure-and-read-out-the-raspberry-pi-gas-sensor-mq-x/)
     - Het gebruik van een gas sensor, zoals de MQ-serie, bij het meten van gasconcentraties in de lucht met een CanSat kan verschillende voordelen hebben,              
       afhankelijk van het doel van je project. Hier zijn een paar redenen waarom je een gas sensor zou kunnen overwegen:
   
       Veiligheid en Milieu-monitoring:

       Een gas sensor kan worden gebruikt om de concentratie van bepaalde gassen in de lucht te meten. Dit is handig als je de luchtkwaliteit wilt controleren en                  mogelijk schadelijke gassen wilt identificeren.
       Wetenschappelijk Onderzoek:

       Als je een wetenschappelijk experiment uitvoert waarbij je de aanwezigheid van specifieke gassen moet meten, kan een gas sensor waardevolle gegevens leveren.
       Toepassingen in Atmosferische Wetenschappen:

       Voor projecten gericht op het bestuderen van de atmosfeer of het uitvoeren van meteorologische metingen, kan een gas sensor nuttige informatie bieden over de               samenstelling van de lucht.
       Bewustmaking over Luchtkwaliteit:

       Het meten van gassen zoals koolmonoxide, koolstofdioxide, of andere verontreinigende stoffen kan worden gebruikt om bewustzijn te creëren over luchtkwaliteit en de         impact van menselijke activiteiten.
       Aanvullende Gegevensverzameling:

       Een gas sensor kan worden toegevoegd als aanvulling op andere sensoren om een meer uitgebreid beeld te krijgen van de omgevingscondities waarin de CanSat zich              bevindt.
       Bij het gebruik van een gas sensor is het belangrijk om te weten welke specifieke gassen de sensor kan detecteren en hoe gevoelig en specifiek de sensor is voor die        gassen. Daarnaast moet je rekening houden met de kalibratie van de sensor om nauwkeurige metingen te verkrijgen.
