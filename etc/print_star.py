# Print a star shape using star symbols

lines = int(input("Enter number of lines: "))
for i in range(lines):
    if i == 0:
        print(' ' * (lines - i - 1) + '*')
    elif i == lines - 1:
        print('*' * (2 * i + 1))
    else:
        print(' ' * (lines - i - 1) + '*' + ' ' * (2 * i - 1) + '*')
