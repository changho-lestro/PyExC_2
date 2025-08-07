# # Lab 04
# # Ahmed Kadar
# # 7/17/2025
# # Functions & Classes

import csv

def countnullfields(csvfile):
    with open(csvfile, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader, [])
        return sum(1 for h in headers if not h.strip())