import datetime

def print_header(title):
    print("\n" + "="*50)
    print(title)
    print("="*50)

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
