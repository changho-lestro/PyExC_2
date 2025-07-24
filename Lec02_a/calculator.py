import operator

def calculator():
    print("Simple CLI Calculator")
    print("Enter 'exit' to quit.")

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    while True:
        try:
            user_input = input("Enter operation (e.g., 2 + 2): ").strip()
            if user_input.lower() == 'exit':
                print("Exiting calculator. Goodbye!")
                break

            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Please use the format: number operator number")
                continue

            num1, op, num2 = parts
            num1, num2 = float(num1), float(num2)

            if op in operations:
                result = operations[op](num1, num2)
                print(f"Result: {result}")
            else:
                print(f"Unsupported operator: {op}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()