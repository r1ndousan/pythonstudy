import os
from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d')
os.mkdir(current_date)

with open(f"{current_date}/example.txt", "w") as file:
    pass

os.mkdir(f"{current_date}/subdirectory")
os.rename(f"{current_date}/example.txt", f"{current_date}/subdirectory/example.txt")