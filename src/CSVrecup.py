import requests
import csv
import time
from datetime import datetime

CSV_FILE = "homeio_dataStress.csv"

KEYS_TO_EXTRACT = {
    'temp/A': 'tempInt',
    'otemp': 'tempExt',
    'ddtc/1/A': 'porteF1',
    'ddtc/2/A': 'porteF2',
    'rhm' : 'Humidity',
    'hour' : 'Heure',
    'wdsp' : 'VitesseVent'
}


def parse_poll_data(raw_text):
    data = {}
    lines = raw_text.split()
    for i in range(len(lines) - 1):
        key = lines[i]
        val = lines[i + 1]
        if key in KEYS_TO_EXTRACT:
            new_key = KEYS_TO_EXTRACT[key]
            try:
                if val.lower() == 'true':
                    data[new_key] = True
                elif val.lower() == 'false':
                    data[new_key] = False
                else:
                    val = float(val.replace(',', '.'))

                    # Correction pour otemp : Kelvin → Celsius
                    if key == 'otemp':
                        data[new_key] = round(val - 273.15, 2)
                    else:
                        data[new_key] = round(val, 3)  # On garde 3 décimales utiles
            except:
                data[new_key] = None
    return data



with open(CSV_FILE, mode='w', newline='') as f:
    writer = csv.writer(f)
    headers = ['timestamp'] + list(KEYS_TO_EXTRACT.values())
    writer.writerow(headers)

print("📡 Début de la collecte... ")


try:
    while True:
        response = requests.get("http://localhost:9797/poll")
        raw_text = response.text
        data = parse_poll_data(raw_text)

        if len(data) == len(KEYS_TO_EXTRACT):
            now = datetime.now().isoformat()
            row = [now] + [data[key] for key in KEYS_TO_EXTRACT.values()]
            with open(CSV_FILE, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(row)
            print(f"✅ Données enregistrées à {now}")
        else:
            print("Données incomplètes")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Collecte arrêtée par l'utilisateur.")
