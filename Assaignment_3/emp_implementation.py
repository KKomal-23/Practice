from emp_operation import excel_file_operation

if __name__ == "__main__":
    obj = excel_file_operation()
    obj.write_headers()
    obj.insert_records()
    #print(obj.read_records())
    #filters = obj.filter_data()
    #print(f"Filtered by salary > 40000: {[str(emp) for emp in filters["salary_filter"]]}")
    #print(f"Filtered by age > 50: {[str(emp) for emp in filters["filter_age"]]}")
    