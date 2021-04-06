import csv
with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    months = []
    sale = []
    for row in spreadsheet:
        months = row['month']
        sale = row['sales']

        print(months,sale)