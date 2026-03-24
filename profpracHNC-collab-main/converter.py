import csv
import json
import os
import re

csv_file = 'plants.csv'
json_file = 'data.json'
image_folder = 'images'

def normalize(text):
    """Convert text to a standard format for matching"""
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text)  # replace anything not a-z/0-9 with -
    return text.strip('-')

data = []

# Build image lookup
image_map = {}
for file in os.listdir(image_folder):
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        name = os.path.splitext(file)[0]
        key = normalize(name)
        image_map[key] = file

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        common_name = row.get('Common Name', '').strip()
        key = normalize(common_name)

        entry = {
            "commonName": common_name,
            "scientificName": row.get('Scientific Name', '').strip(),
            "group": row.get('Group', '').strip(),
            "habitat": row.get('Habitat', '').strip(),
            "lifecycle": row.get('Lifecycle (Jan-Dec)', '').strip(),
            "identification": row.get('Identification Features', '').strip(),
            "heightSize": row.get('Height/Size', '').strip(),
            "native": row.get('Native?', '').strip(),
            "notes": row.get('Cultural / Edible / Medicinal / Historical Notes', '').strip(),
            "image": image_map.get(key, "")
        }

        data.append(entry)

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("data.json created with images added!")