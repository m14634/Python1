# Importing required modules.
import csv
import pandas as pd
import openpyxl
from openpyxl import Workbook
import numpy as np
import xlrd
from xlrd import open_workbook
import matplotlib.pyplot as plt
most_expenditure = 0
least_expenditure = 0


# The following code can be used to calculate the gross profits and monthly percentage changes for 2018.
# This data will be stored in the complete_spreadsheet.xlsx file along with the rest of the sales information.

# This part of the code reads the data from the .csv file and collects sales from each month into a list.
lis = input('Would you like to collect all of the sales from each month into a single list? y/n ')
if lis == 'y':
    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        months = []
        sale = []

        for row in spreadsheet:
            months = row['month']
            sale = row['sales']

            print(months, sale)

# Reading the file of interest (sales.csv).
df = pd.read_csv(r'/Users/vee/PycharmProjects/cfg-python/Group Project/sales.csv')

# Calculating % change and gross profit.
df['Percentage change (%)'] = round(df['sales'].pct_change()*100, 2)
df['Gross Profit (£)'] = df['sales'] - df['expenditure']

# Generating a new spreadsheet containing additional % change and gross profit information.
df.to_excel(r'/Users/vee/PycharmProjects/cfg-python/Group Project/complete_spreadsheet.xlsx', index=False)

spreadsheet = input('Would you like calculate the gross profit and monthly percentage changes for 2018? y/n ')
if spreadsheet == 'y':
    print('The data has been saved in complete_spreadsheet.xlsx.')
    print(df)

# If requested, the total sales for 2018 can be calculated.
sales_t = input('Would you like to calculate the total sales for 2018? y/n ')
if sales_t == 'y':
    # Calculating and rounding total sales to 2 decimal places.
    sum1 = df['sales'].sum()
    sum11 = round(sum1, 2)
    print('The total sum of sales is: £' + str(sum11))

# The code can calculate the mean, median, standard deviation and variance of sales.
m_me_var = input('Would you like to calculate the mean, median, standard deviation and variance? y/n ')
if m_me_var == 'y':
    # Calculating required values using pandas module.
    mean1 = df['sales'].mean()
    median1 = df['sales'].median()
    std1 = df['sales'].std()
    var1 = df['sales'].var()

    # Rounding the values to 2 decimal places.
    mean11 = round(mean1, 2)
    median11 = round(median1, 2)
    std11 = round(std1, 2)
    var11 = round(var1, 2)

    # Producing output values.
    print('The mean of sales is: £' + str(mean11))
    print('The median of sales is: £' + str(median11))
    print('The standard deviation of sales is: £' + str(std11))
    print('The variance of sales is: £' + str(var11))

# The code can display the months with most and least sales, along with the sales value.
m_l_ex = input('Would you like to see the months with the most and least sales? y/n ')
if m_l_ex == 'y':
    # Defining the function.
    def read_data():
        # Using dictionary.
        global row
        data = []
        with open('sales.csv', 'r') as sales_csv:
            sheet = csv.DictReader(sales_csv)
            for row in sheet:
                data.append(row)
        return data

    def run():
        global least_expenditure, most_expenditure, row
        data = read_data()
        sales = {}

        for row in data:
            expenditure = row['sales']
            month = row['month']
            sales[expenditure] = month

            least_expenditure = min(sales)
            most_expenditure = max(sales)

        print('The month of {} had the most sales: £{}'.format(sales[most_expenditure], max(sales)))
        print('The month of {} had the least sales: £{}'.format(sales[least_expenditure], min(sales)))
    run()

# The code can produce Financial Graphs for 2018, displaying sales and gross profit for each month.
# These graphs will be saved as Financial_graphs_2018.png.
m = input('Would you like to see the graphs for gross profit/sales per month? y/n ')
if m == 'y':
    # Defining x and y variables for the bar chart.
    x = df['month']
    y = df['sales']
    yy = df['Gross Profit (£)']
    colourlist = ['red', 'orange', 'yellow', 'green', 'c', 'blue', 'purple', 'yellow', 'green', 'c', 'blue', 'purple']

    plt.figure()
    plt.suptitle('Financial Graphs for 2018', fontsize=20)
    plt.subplot(2, 1, 1)
    plt.bar(x, y, color=colourlist)
    plt.title('Sales')
    plt.xlabel("Month")
    plt.ylabel("Sales (£)")

    plt.subplot(2, 1, 2)
    plt.bar(x, yy, color=colourlist)
    plt.title('Gross Profit')
    plt.xlabel("Month")
    plt.ylabel("Gross Profit (£)")
    plt.tight_layout()
    plt.show()
    # Plot saved.
    plt.savefig('/Users/vee/PycharmProjects/cfg-python/Group Project/Financial_graphs_2018.png')
