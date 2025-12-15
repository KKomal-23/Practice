import openpyxl
import os


FILE_PATH = r"C:\Users\HP\OneDrive\Desktop\Koumal Assaignments\Assaignment_3\employees.xlsx"

#print(os.path.exists(FILE_PATH))
#print(os.path.getsize(FILE_PATH))
def load_work_book():
    # If file does not exist or is empty, create a new one
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        wb = openpyxl.Workbook()
        ws = wb.active
        wb.save(FILE_PATH)
        return wb, ws
    else:
        wb = openpyxl.load_workbook(FILE_PATH)
        ws = wb.active
        return wb, ws
