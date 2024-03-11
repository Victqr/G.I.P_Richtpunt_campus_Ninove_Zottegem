import csv

# Open het tekstbestand om te lezen
with open('data_2024-03-11_10-30-04.txt', 'r') as txtfile:
    lines = txtfile.readlines()

# Verwijder eventuele nieuwe regel karakters
lines = [line.strip() for line in lines]

# Bepaal de scheidingsteken voor het CSV-bestand (bijvoorbeeld een komma)
delimiter = ','

# Open een CSV-bestand om te schrijven
with open('output.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=delimiter)

    # Schrijf elke regel van het tekstbestand als een rij in het CSV-bestand
    for line in lines:
        # Split elke regel op basis van het scheidingsteken in het tekstbestand (bijvoorbeeld een spatie)
        data = line.split()

        # Schrijf de data naar het CSV-bestand
        csvwriter.writerow(data)

print("Conversie voltooid!")

