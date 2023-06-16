def CheckExpression(ch):
    def operator():
        if index < len(ch) and ch[index] not in "+-*/":
            return "error"

    def letter():
        if index < len(ch) and ch[index] not in "abcdefghijklmnopqrstuvwxyz":
            return "error"

    def PSZ():
        nonlocal index, expression
        if index < len(ch) and ch[index] in "([":
            expression = SZ1()
            if expression:
                return expression
            index += 1
            expression = operator()
            if expression:
                return expression
            index += 1
            expression = SZ2()
            if expression:
                return expression
        elif index < len(ch) and ch[index] in "abcdefghijklmnopqrstuvwxyz":
            expression = letter()
            if expression:
                return expression
            index += 1
            expression = operator()
            if expression:
                return expression
            index += 1
            expression = KSZ()
            if expression:
                return expression
        else:
            return "error"

    def KSZ():
        nonlocal index, expression
        if index < len(ch) and ch[index] in "([":
            expression = SZ1()
            if expression:
                return expression
            index += 1
            expression = KON2()
            if expression:
                return expression
        elif index < len(ch) and ch[index] in "abcdefghijklmnopqrstuvwxyz":
            expression = letter()
            if expression:
                return expression
            index += 1
            expression = KON1()
            if expression:
                return expression
        else:
            return "error"

    def SZ1():
        nonlocal index, expression
        if index < len(ch) and ch[index] == '(':
            index += 1
            expression = PSZ()
            if expression:
                return expression
            if index == len(ch) or ch[index] != ')':
                return "error"
        elif index < len(ch) and ch[index] == '[':
            index += 1
            expression = PSZ()
            if expression:
                return expression
            if index == len(ch) or ch[index] != ']':
                return "error"
        else:
            return "error"

    def SZ2():
        nonlocal index, expression
        if index < len(ch) and ch[index] in "([":
            expression = SZ1()
            if expression:
                return expression
            index += 1
            expression = KON3()
            if expression:
                return expression
        elif index < len(ch) and ch[index] in "abcdefghijklmnopqrstuvwxyz":
            expression = letter()
            if expression:
                return expression
            index += 1
            expression = KON1()
            if expression:
                return expression
        else:
            return "error"

    def KON1():
        nonlocal index, expression
        if index < len(ch) and ch[index] in "+-*/":
            expression = operator()
            if expression:
                return expression
            index += 1
            expression = KSZ()
            if expression:
                return expression

    def KON2():
        nonlocal index, expression
        if index < len(ch) and ch[index] in "+-*/":
            expression = operator()
            if expression:
                return expression
            index += 1
            expression = SZ2()
            if expression:
                return expression

    def KON3():
        nonlocal index, expression
        if index < len(ch) and ch[index] in "+-*/":
            expression = operator()
            if expression:
                return expression
            index += 1
            expression = letter()
            if expression:
                return expression
            index += 1
            expression = KON1()
            if expression:
                return expression

    expression = ''
    index = 0
    expression = KSZ()
    if expression or len(ch) != index:
        return "The entered expression does NOT satisfy the grammar!"
    else:
        return "The entered expression satisfies the grammar!"


while True:
    expression = input("Enter your expression (or 'exit' to quit): ")
    if expression == 'exit':
        break
    result = CheckExpression(expression)
    print(result)
