def PSZ():
    global ch
    if ch in {"("}:
        if ch in {"("}:
            read()
        else:
            raise Exception()
        KSZ()
        if ch in {")"}:
            read()
        else: 
            raise Exception()
        KON5()
    elif ch in {"["}:
        if ch in {"["}:
            read()
        else:
            raise Exception()
        KSZ()
        if ch in {"]"}:
            read()
        else:
            raise Exception()
        KON4()
    elif ch in latin:
        letter()
        KON1()
    else:
        raise Exception()



def KSZ():
    global ch
    if ch in {"("}:
        if ch in {"("}:
            read()
        else:
            raise Exception()
        KSZ()
        if ch in {")"}:
            read()
        else: 
            raise Exception()
        sign()
        SZ1()
    elif ch in {"["}:
        if ch in {"["}:
            read()
        else:
            raise Exception()
        KSZ()
        if ch in {"]"}:
            read()
        else:
            raise Exception()
        sign()
        SZ2()
    elif ch in latin:
        letter()
        sign()
        PSZ()
    else:
        raise Exception()



def SZ1():
    global ch
    if ch in {"("}:
        if ch in {"("}:
            read()
        else:
            raise Exception()
        KSZ()
        if ch in {")"}:
            read()
        else: 
            raise Exception()
        KON2()
    elif ch in {"["}:
        if ch in {"["}:
            read()
        else:
            raise Exception()
        KSZ()
        if ch in {"]"}:
            read()
        else:
            raise Exception()
        KON4()
    elif ch in latin:
        letter()
        KON1()
    else:
        raise Exception()



def SZ3():
    global ch
    if ch in {"["}:
        if ch in {"["}:
            read()
        else:
            raise Exception()
        KSZ()
        if ch in {"]"}:
            read()
        else:
            raise Exception()
        KON4()
    elif ch in latin:
        letter()
        KON1()
    else:
        raise Exception()



def SZ2():
    global ch
    if ch in {"("}:
        if ch in {"("}:
            read()
        else:
            raise Exception()
        KSZ()
        if ch in {")"}:
            read()
        else: 
            raise Exception()
        KON5()
    elif ch in {"["}:
        if ch in {"["}:
            read()
        else:
            raise Exception()
        KSZ()
        if ch in {"]"}:
            read()
        else:
            raise Exception()
        KON3()
    elif ch in latin:
        letter()
        KON1()
    else:
        raise Exception()



def SZ4():
    global ch
    if ch in {"("}:
        if ch in {"("}:
            read()
        else:
            raise Exception()
        KSZ()
        if ch in {")"}:
            read()
        else:
            raise Exception()
        KON5()
    elif ch in latin:
        letter()
        KON1()
    else:
        raise Exception()
    
    
   
def KON1():
    global ch
    if ch in {"*","+","-","/"}:
        sign()
        PSZ()
    
    
   
def KON2():
    global ch
    if ch in {"*","+","-","/"}:
        sign()
        SZ3()
    
    
   
def KON3():
    global ch
    if ch in {"*","+","-","/"}:
        sign()
        SZ4()
    
    
   
def KON4():
    global ch
    if ch in {"*","+","-","/"}:
        sign()
        SZ2()
    
    
   
def KON5():
    global ch
    if ch in {"*","+","-","/"}:
        sign()
        SZ1()



def letter():
    global ch
    if ch in latin:
         read()
    else:
        raise Exception()



def read():
    global ch
    global string
    global current
    current += 1
    ch = string[current]



def sign():
    global ch
    if ch in {"*","+","-","/"}:
         read()



latin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rule = """
===========================================================================
Правила
===========================================================================
Правильная скобочная запись арифметических выражений с двумя видами скобок. 
Подряд могут идти не более двух скобок одного вида. 
Не должно быть “лишних” скобок, и одна буква не может браться в скобки. 
==========================================================================="""
print(rule)



while True:
    print("Введите выражение:")
    string = f"{input()}#"
    current = 0
    ch = string[current]
    
    try:
        PSZ()
        print("Эта запись ПРАВИЛЬНАЯ!")
    except BaseException:
        print("Эта запись НЕПРАВИЛЬНАЯ!")

    print("Попробовать снова?")
    print("Ведите \"Y\" или \"N\": \n        ^")
    if input() == "N":
        exit()
