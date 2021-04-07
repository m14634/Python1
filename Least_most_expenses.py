import csv

def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def run():
    data = read_data()
    sales = {}

    for row in data:
        expenditure = row['sales']
        month = row['month']
        sales[expenditure]=month
        print(sales)

        least_expenditure = min(sales)
        most_expenditure = max(sales)

    print('{} had the most sales:{}'.format(sales[most_expenditure],max(sales)))
    print('{} had the least sales:{}'.format(sales[least_expenditure], min(sales)))

run()

