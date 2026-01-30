# script to populate MARATHON table
import csv

def clean_val(val):
    return val.strip().strip("'")

def sql_format(val):
    cleaned = clean_val(val)
    if cleaned.isdigit() or cleaned.replace('.', '').replace('-', '').isdigit():
        return cleaned
    else:
        escaped = cleaned.replace("'", "''")
        return f"'{escaped}'"

with open('MARATHON/marathon.csv', 'r', encoding='utf-8') as csvfile, \
    open('MARATHON-build-MARATHON.sql', 'w') as sqlfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if row:
            values = ', '.join(sql_format(val) for val in row)
            sqlfile.write(f"INSERT INTO MARATHON VALUES ({values});\n")
