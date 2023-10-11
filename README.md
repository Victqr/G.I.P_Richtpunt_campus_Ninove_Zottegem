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
|PROGRAMMEREN|	Victor|
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

## **Secundaire missie**

1. **gas sensor (MQ-X)**
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


2. **MenuRaspberry Pi GPS Logger**
   - Bron: [Open MenuRaspberry Pi GPS Logger](https://www.instructables.com/Raspberry-Pi-GPS-Logger/)
     - Een Raspberry Pi GPS Logger kan handig zijn in verschillende situaties waarin je de geografische locatie van een apparaat wilt volgen en registreren. Hier zijn een         paar redenen waarom je een Pi GPS Logger zou kunnen gebruiken:

       Navigatie en Tracking:

       Als je een project hebt waarin je de bewegingen van een object of persoon wilt volgen, zoals een voertuig, een wandelaar, of een dier, kan een GPS Logger nuttig            zijn. Het kan bijvoorbeeld worden gebruikt voor outdoor-activiteiten, zoals wandeltochten of geocaching.
       Wetenschappelijk Onderzoek:

       Voor onderzoek in geografie, ecologie, of andere wetenschappelijke disciplines kan het belangrijk zijn om de exacte locatie van gegevensverzameling vast te leggen.         Een GPS Logger op een Raspberry Pi kan hierbij van dienst zijn.
       Projecten met Ruimtelijke Analyse:

       Als je geïnteresseerd bent in het analyseren van gegevens op basis van geografische locatie, zoals het maken van kaarten of het bestuderen van patronen in beweging,        is een GPS Logger een waardevol hulpmiddel.
       Educative Purposes:

       Voor educatieve doeleinden kan een GPS Logger op een Raspberry Pi worden gebruikt om studenten te leren over geografie, navigatie, en het gebruik van GPS-                  technologie.
       Het gebruik van een Raspberry Pi voor GPS-logging biedt flexibiliteit, programmeermogelijkheden en de mogelijkheid om andere sensoren te integreren, afhankelijk van        je projectvereisten. Het is een kosteneffectieve manier om locatiegebaseerde gegevens vast te leggen en te verwerken.

3. **Back-UP opslag**
     - Absoluut, back-upopslag is een cruciaal element in missies waar betrouwbaarheid en volledigheid van gegevens van groot belang zijn. Hier zijn enkele redenen                waarom je
       zou kunnen kiezen voor back-upopslag in plaats van radiocommunicatie voor het vergelijken van verloren gegevens:

       Betrouwbaarheid van Gegevens:
       Radiocommunicatie kan onderbroken worden door verschillende factoren zoals atmosferische storingen, interferentie of technische problemen. Back-upopslag biedt een          fysieke oplossing om ervoor te zorgen dat alle gegevens veilig worden bewaard, zelfs als er communicatieproblemen optreden.

       Missie Duur:
       Als de CanSat gedurende een langere periode zelfstandig werkt, kan het gebruik van back-upopslag nuttig zijn. Het vermijdt datagegevensverlies dat zou kunnen               optreden tijdens momenten waarop er geen communicatie mogelijk is.

       Data-analyse na de Missie:
       Het hebben van alle gegevens opgeslagen op een fysiek medium vergemakkelijkt de analyse na de missie. Onderzoekers kunnen de gegevens rustig bestuderen zonder de           beperkingen van real-time monitoring.
