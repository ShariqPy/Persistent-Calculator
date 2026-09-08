def add(a, b):
    return a + b 

def minus(a, b):
    return a - b   

def multiply(a, b):
    return a * b 

def divide(a, b):
    if b == 0: 
        return "Error: Dividing by zero!"
    return a / b 

history = [] 
current_total = None  # Holds the accumulated answer across operations

while True: 
    print("\n----------------------- Persistent Calculator -----------------------") 
    if current_total is not None:
        print(f"Current Value: {current_total}")
    else:
        print("Current Value: [Clear]")

    print("1. Add  2. Minus  3. Multiply  4. Divide  5. View History  6. Clear/Reset  7. Exit") 
    choice = input("Select an option (1-7): ").strip() 

    if choice == '7':
        print("Have a great day!") 
        break 

    if choice == '6':
        current_total = None
        print("Calculator reset!")
        continue

    if choice in ['1', '2', '3', '4']:
        try:
            # If we don't have a total yet, ask for the first number.
            # Otherwise, use current_total as num1!
            if current_total is None:
                num1 = float(input("Enter first number: ")) 
            else:
                num1 = current_total
                print(f"First number (using current total): {num1}")

            num2 = float(input("Enter next number: ")) 

            if choice == '1':
                result = add(num1, num2) 
                op = "+"  
            elif choice == '2':
                result = minus(num1, num2) 
                op = "-" 
            elif choice == '3':
                result = multiply(num1, num2)
                op = "*" 
            elif choice == '4':
                result = divide(num1, num2) 
                op = "/" 

            # Only update total if division didn't fail
            if isinstance(result, (int, float)):
                current_total = result
                entry = f"{num1} {op} {num2} = {result}" 
                print(f"Result: {result}") 
                history.append(entry) 
            else:
                print(result) # Prints error message

        except ValueError: 
            print("Oops! There seems to be an error on your side!")   

    elif choice == '5':
        print("\n ------ Calculation History ------") 
        if not history:
            print("No history recorded yet.")
        else:
            for idx, item in enumerate(history, 1):
                print(f"{idx}. {item}")