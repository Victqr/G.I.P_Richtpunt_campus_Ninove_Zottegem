# G.I.P Richtpunt campus Ninove Zottegem
G.I.P Victor Limpens 6EE


**G.I.P Project CanSat**

Naam CanSat

Can -> Blikje van 33cl

Sat -> mini satelliet 

Wat is CanSat?

Een team van 4 tot 6 leerlingen gaan de uitdaging aan om alle belangrijke subsystemen van een satelliet te bouwen en te doen passen in een blikje van 33 cl: de elektrische voeding, de sensoren en het communicatiesysteem. Hun satelliet(CanSat) bevat eigenlijk 2 missies:
Een primaire missie: luchtdruk, temperatuur en hoogte meten en de data verzenden naar het grondstation tijdens de vlucht, en een veilige landing van je satellietje voorzien (meestal met een parachute).
Een secundaire missie: een zelfbedacht experiment of technische uitdaging die je satelliet uitvoert tijdens het stijgen of dalen.

****

## inhoudsopgave
<a name="inhoudsopgave"></a>

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

