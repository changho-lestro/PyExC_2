# # Lab 04
# # Ahmed Kadar
# # 7/17/2025
# # Functions & Classes

import sys
sys.path.append("./Lec07_test")
from mycount import countnullfields

csv_path = r'C:\E\PyExC\Lec07_test\05datafile.csv'
empty_count = countnullfields(csv_path)
print(f'Number of empty header fields: {empty_count}')