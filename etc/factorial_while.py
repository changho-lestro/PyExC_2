input_val = input("Show Factorial values: ")

x = 1
while x <= int(input_val):
    if x == 1:
        prev_x = 1
    else:
        prev_x = prev_x * x
    x += 1

print(f"Factorial of {x-1} is {prev_x}.")

