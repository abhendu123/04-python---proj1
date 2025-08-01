
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pandas as pd
from datetime import datetime
from a001log.logger import log
from a002stage.import_excel import extract_from_excel




def extract():
    excel_file_path = 'C:/Users/abhendu.chowdhury/test.xlsx'      # <--- your excel file here
    return extract_from_excel(excel_file_path)


log("ETL Job Started")

log("Extract phase Started")
excel_df = extract()

if excel_df is not None:
    log("Extract phase Ended")
else:
    log("Extract phase Failed", is_error=True)  # This line will have a cross ('✗') instead of a checkmark

log("-------------------------", is_error=False, include_checkmark=False)  # This log line doesn't include the checkmark