import csv

input_file = "input.csv"
output_file = "output.csv"

with open(input_file, newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    rows = list(reader)

seen = set()
unique_rows = []

for row in rows:
    row_tuple = tuple(row)
    if row_tuple not in seen:
        seen.add(row_tuple)
        unique_rows.append(row)

with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(unique_rows)
