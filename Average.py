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
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    avg = sum(sales) / len(sales)
    print('Average sales: {}'.format(avg))

run()