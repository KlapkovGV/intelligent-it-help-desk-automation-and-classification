import re
import pandas as pd
from src.config import ERROR_PATTERN, REQUEST_PATTERN

def classify_by_regex(text):
    if pd.isna(text):
        return 'Ambiguous'
    text = str(text).lower()
    if re.search(ERROR_PATTERN, text):
        return 'Error'
    elif re.search(REQUEST_PATTERN, text):
        return 'Request'
    else:
        return 'Ambiguous'
