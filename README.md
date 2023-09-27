# G.I.P Richtpunt campus Ninove Zottegem
G.I.P Victor Limpens 6EE


### **G.I.P Project CanSat**

Wat is CanSat?

- Een CanSat is een samenvoeging van de woorden "Can" en "Satellite" (blikje en satelliet). Het is een educatief en onderzoeksproject dat wordt gebruikt in de ruimtevaart en wetenschappelijke gemeenschap. Het doel ervan is om studenten en onderzoekers in staat te stellen te experimenteren met ruimtevaarttechnologie en wetenschappelijke metingen te verrichten met een klein, goedkoop en eenvoudig te lanceren apparaat.

- Een CanSat is meestal ter grootte van een blikje frisdrank of iets groter. Het bevat sensoren en apparatuur die gegevens kunnen verzamelen, zoals temperatuur, luchtdruk, hoogte, snelheid en meer, terwijl het in de lucht is. Dit apparaat wordt dan gelanceerd in de ruimte met behulp van een raket of een ballon.

- Waarom is dit belangrijk? Ten eerste is het een geweldige leerervaring voor studenten in technische en wetenschappelijke vakgebieden. Ze kunnen leren over ruimtevaarttechnologie, dataverzameling en analyse, en teamwork terwijl ze hun eigen CanSat-missie plannen en uitvoeren.

- Bovendien kunnen CanSats nuttige gegevens opleveren voor verschillende toepassingen, zoals weermetingen, milieuonderzoek of technologietests. Het zijn als kleine, betaalbare satellieten die kortstondige missies kunnen uitvoeren en waardevolle informatie kunnen verzamelen.

- Dus, CanSat is een educatief en onderzoeksinitiatief waarmee studenten en onderzoekers praktische ervaring kunnen opdoen in de ruimtevaart en wetenschap, terwijl ze tegelijkertijd gegevens verzamelen die nuttig kunnen zijn voor verschillende toepassingen.

****

## inhoudsopgave
<a name="inhoudsopgave"></a>
 ## Hoofdstuk 1

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

