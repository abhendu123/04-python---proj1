from datetime import datetime

def log(message, is_error=False, include_checkmark=True):
    timestamp_format = '%Y-%b-%d-%H:%M:%S'  # Year-Monthname-Day-Hour-Minute-Second
    current_time = datetime.now()
    timestamp = current_time.strftime(timestamp_format)
    
    if include_checkmark:
        symbol = '✓' if not is_error else '✗'
    else:
        symbol = ''
    
    log_message = f"[{timestamp}] {symbol} {message}\n"
    
    with open("logfile.txt", "a", encoding='utf-8') as f: # <--- your log file here
        f.write(log_message)