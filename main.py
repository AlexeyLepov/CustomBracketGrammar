def custom_bracket_form(expr):
    stack = []
    last_char = ''
    for i, ch in enumerate(expr):
        if ch in {'(', '['}:
            if last_char == ch:
                print(f"Error: Two or more consecutive '{ch}' at position {i}")
                return False # Two or more parentheses of the same kind in a row
            stack.append(ch)
        elif ch in {')', ']'}:
            if not stack:
                print(f"Error: Extra '{ch}' at position {i}")
                return False # Extra closing parenthesis
            if (ch == ')' and stack[-1] != '(') or (ch == ']' and stack[-1] != '['):
                print(f"Error: Mismatched '{stack[-1]}' and '{ch}' at position {i}")
                return False # Mismatched closing parenthesis
            stack.pop()
        elif last_char.isalpha() and ch.isalpha():
            print(f"Error: One letter cannot be bracketed at position {i}")
            return False # One letter cannot be bracketed
        last_char = ch
    if stack:
        print(f"Error: Extra '{stack[-1]}' at position {len(expr)}")
        return False # Extra opening parenthesis
    return True

while True:
    # expression = "(a+b)/([a-b*c]([a-b]*(a+b)*(a*a+b*b)))"
    expression = input("Please enter your expression (press 'q' to quit): ")
    if expression == 'q':
        break
    if custom_bracket_form(expression):
        print("The expression is valid.")
