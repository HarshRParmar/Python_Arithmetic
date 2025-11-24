def calculate(num1, num2, operation):
    """
    Performs arithmetic operations based on the operator provided.
    """
    # specific handling for division to avoid crashes
    if operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    
    # Standard operations
    elif operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return  num1 * num2
    elif operation == '%':
        return num1 % num2  # Modulus (Remainder)
    else:
        return "Error: Invalid operation selected."

def main():
    print("--- Simple Arithmetic Calculator ---")
    print("Available Operations: +, -, *, /, %")
    
    try:
        # Taking inputs
        # We use float() to ensure decimals work (e.g., 5.5)
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        op = input("Enter the operation (+, -, *, /, %): ")

        # Calling the function
        result = calculate(n1, n2, op)

        # Displaying result
        print("-" * 30)
        print(f"Result: {result}")
        print("-" * 30)

    except ValueError:
        print("Error: Please enter valid numeric values.")

# This ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
