definitions = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def hexconverter(decimal):
    if decimal.isalpha():
        upperdeci = decimal.upper()
    else:
        upperdeci = decimal
    search = definitions.index(upperdeci)
    return search

while True:
    hexanswer = raw_input("Print Hexadecimal? ")

    start_state = 0
    list_hexanswer = list(hexanswer)
    for number in list_hexanswer:
        real_value = hexconverter(number)
        multiplier = 16 ** (len(hexanswer) - list_hexanswer.index(number) - 1)
        adder = real_value * multiplier
        start_state += adder
        list_hexanswer.insert(list_hexanswer.index(number), 'X')
        idk = list_hexanswer.index(number)
        del list_hexanswer[idk]

    print start_state
