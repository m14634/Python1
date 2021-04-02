import openpyxl

from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B2"] = "world!"

workbook.save(filename="hello_world.xlsx")

#have to go to File -- Settings -- Project -- Python Interpreter -- Click on plus button at bottom left of dialogue box -- 'Add' -- Search and Install 'Openpyxl'
# then in terminal type: 'pip install openpyxl' [dont know if necessary]
#above code creates an Excel workbook with 'hello world!' in corresponding cells and saves in same folder as python docs are saved

#potential idea to create our own excel file and then manipulate data as per requirements ??
#https://realpython.com/openpyxl-excel-spreadsheets-python/