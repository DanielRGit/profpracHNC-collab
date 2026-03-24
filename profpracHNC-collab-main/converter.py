import csv
import json

csv_file = 'plants.csv'   # Your CSV file
json_file = 'data.json'

data = []

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)  # Uses CSV headers automatically
    for row in reader:
        data.append({
            "commonName": row.get('Common Name', '').strip(),
            "scientificName": row.get('Scientific Name', '').strip(),
            "group": row.get('Group', '').strip(),
            "habitat": row.get('Habitat', '').strip(),
            "lifecycle": row.get('Lifecycle (Jan-Dec)', '').strip(),
            "identification": row.get('Identification Features', '').strip(),
            "heightSize": row.get('Height/Size', '').strip(),
            "native": row.get('Native?', '').strip(),
            "notes": row.get('Cultural / Edible / Medicinal / Historical Notes', '').strip()
        })

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("data.json created with extended fields!")