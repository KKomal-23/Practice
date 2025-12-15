from emp_abstraction import File_Operation
from emp_data import generate_emps
from emp_excel_file import load_work_book, FILE_PATH
from emp_classes import Employee
from datetime import datetime
import os

class excel_file_operation(File_Operation):
    def __init__(self):
        self.file_path = FILE_PATH

    def generate(self, num):
        return generate_emps(num)
    
    def write_headers(self):
        workbook, sheet = load_work_book()
        sheet.cell(row=1, column=1).value = "name"
        sheet.cell(row=1, column=2).value = "surname"
        sheet.cell(row=1, column=3).value = "dob"
        sheet.cell(row=1, column=4).value = "age"
        sheet.cell(row=1, column=5).value = "email"
        sheet.cell(row=1, column=6).value = "address"
        sheet.cell(row=1, column=7).value = "salary"
        
        workbook.save(self.file_path)
    
    def insert_records(self):
        workbook, sheet = load_work_book()
        emps = self.generate(20)
        for k, record in enumerate(emps, start=2):
            sheet.cell(row=k, column=1).value = record.name
            sheet.cell(row=k, column=2).value = record.surname[1]
            sheet.cell(row=k, column=3).value = record.dob
            sheet.cell(row=k, column=4).value = record.age
            sheet.cell(row=k, column=5).value = record.email
            sheet.cell(row=k, column=6).value = record.address
            sheet.cell(row=k, column=7).value = record.salary
            
        workbook.save(self.file_path)


    def read_records(self):
        _, sheet = load_work_book()
        emp_list = [
            Employee(
            name = sheet.cell(row=i, column=1).value,
            dob = sheet.cell(row=i, column=3).value,
            
            email = sheet.cell(row=i, column=5).value,
            address = sheet.cell(row=i, column=6).value,
            salary = sheet.cell(row=i, column=7).value
            )
            for i in range(2, sheet.max_row + 1)
        ]
        return emp_list
    
    def filter_data(self):
        emps = self.read_records()
        salary_filter = [emp for emp in emps if emp.salary>40000]
        filter_age =[emp for emp in emps if emp.age > 50]
        return{"salary_filter": salary_filter,
               "filter_age": filter_age}




