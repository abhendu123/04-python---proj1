import pandas as pd
from datetime import datetime
from a001log.logger import log




def extract_from_excel(file_to_process):
    try:
        dataframe = pd.read_excel(file_to_process)
        return dataframe
    except FileNotFoundError:
        log(f"Error: The file '{file_to_process}' was not found.", is_error=True)
        return None

def extract():
    excel_file_path = 'C:/test.xlsx'      # <--- your excel file here
    return extract_from_excel(excel_file_path)