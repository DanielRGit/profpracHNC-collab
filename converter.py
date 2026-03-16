import csv
import json

csv_file = 'plants.csv'   # your CSV file
json_file = 'data.json'

data = []

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)  # automatically reads headers
    for row in reader:
        # Create a JSON object with separate fields
        item = {
            "commonName": row['Common Name'].strip(),
            "scientificName": row['Scientific Name'].strip(),
            "group": row['Group'].strip(),
            "habitat": row['Habitat'].strip(),
            "lifecycle": row['Lifecycle (Jan-Dec)'].strip()
        }
        data.append(item)

# Save JSON file
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("data.json created with separate fields!")