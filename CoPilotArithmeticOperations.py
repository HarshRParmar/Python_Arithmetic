# Simple arithmetic program
# Input: either a single line "a b op" or three separate lines:
#   3 4 add
#   or
#   3
#   4
#   add

import sys

def to_number(s):
    try:
        if '.' in s:
            return float(s)
        return int(s)
    except ValueError:
        return float(s)  # fallback, will raise if invalid

def format_result(x):
    # print integer-looking floats as ints
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

def main():
    data = []
    # Try to read tokens from a single line
    try:
        line = sys.stdin.readline()
        if not line:
            return
        parts = line.strip().split()
        if len(parts) >= 3:
            a_str, b_str, op = parts[0], parts[1], parts[2].lower()
        else:
            # read remaining inputs from subsequent lines
            a_str = parts[0] if parts else sys.stdin.readline().strip()
            b_str = sys.stdin.readline().strip()
            op = sys.stdin.readline().strip().lower()
    except Exception:
        print("Invalid input")
        return

    try:
        a = to_number(a_str)
        b = to_number(b_str)
    except Exception:
        print("Invalid numbers")
        return

    # Supported operations
    if op in ('add', '+', 'plus'):
        res = a + b
    elif op in ('sub', '-', 'minus'):
        res = a - b
    elif op in ('mul', '*', 'x', 'times'):
        res = a * b
    elif op in ('div', '/', 'divide'):
        if b == 0:
            print("Error: Division by zero")
            return
        res = a / b
    elif op in ('mod', '%', 'remainder'):
        try:
            res = a % b
        except Exception:
            print("Error: Invalid modulo operation")
            return
    elif op in ('pow', '^', '**'):
        res = a ** b
    else:
        print("Unsupported operation")
        return

    print(format_result(res))

if __name__ == "__main__":
    main()
