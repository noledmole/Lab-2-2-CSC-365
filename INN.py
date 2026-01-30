## script to generate INSERT statements for the INN database
import csv

def clean_val(val):
    return val.strip().strip("'")

def sql_format(val, is_date=False):
    cleaned = clean_val(val)
    if is_date:
        return f"STR_TO_DATE('{cleaned}', '%d-%b-%y')"
    if cleaned.isdigit() or cleaned.replace('.', '').replace('-', '').isdigit():
        return cleaned
    else:
        escaped = cleaned.replace("'", "''")
        return f"'{escaped}'"

with open('INN/Rooms.csv', 'r', encoding='utf-8') as csvfile, \
    open('INN-build-ROOMS.sql', 'w') as sqlfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if row:
            values = ', '.join(sql_format(val) for val in row)
            sqlfile.write(f"INSERT INTO ROOMS VALUES ({values});\n")

with open('INN/Reservations.csv', 'r', encoding='utf-8') as csvfile, \
    open('INN-build-RESERVATIONS.sql', 'w') as sqlfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if row:
            formatted = [sql_format(val, is_date=(i in [2, 3])) for i, val in enumerate(row)]
            sqlfile.write(f"INSERT INTO RESERVATIONS VALUES ({', '.join(formatted)});\n")
