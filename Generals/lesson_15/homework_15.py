import csv
import logging
import numbers
import os
import json
import xml.etree.ElementTree as ET

logging.basicConfig(
    filename="json__perederiiev.log",
    level = logging.ERROR,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)


    # Завдання 1
seen_ids = set()
unique_rows = []

with open("ideas_for_test/r-m-c.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        contact_id = row[0]
        if contact_id not in seen_ids:
            seen_ids.add(contact_id)
            unique_rows.append(row)

with open("ideas_for_test/random-michaels.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        contact_id = row[0]
        if contact_id not in seen_ids:
            seen_ids.add(contact_id)
            unique_rows.append(row)

with open("result_perederiiev.csv", "w", encoding="utf-8", newline="") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(header)
    writer.writerows(unique_rows)

    # Завдання 2

files = os.listdir("ideas_for_test/work_with_json")

for filename in files:
    full_path = "ideas_for_test/work_with_json/" + filename
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Невалідний JSON: {filename} - {e}")

    # Завдання 3
def find_incoming(number):
    tree = ET.parse("ideas_for_test/work_with_xml/groups.xml")
    root = tree.getroot()

    for group in root:
        group_number = group.find("number").text
        if group_number == number:
            incoming_tag = group.find("timingExbytes/incoming")
            if incoming_tag is not None:
                return incoming_tag.text
            else:
                return None

result = find_incoming("2")
print(result)