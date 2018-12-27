# 0 - 15 -- 0 - F
decision2 = 'y'
definitions = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
print "It's the decimal to hex (or vice versa) converter."
while decision2 == 'y':
    decision = raw_input("""
Enter '1' for decimal to hexadecimal
or  
Enter '2' for hexadecimal to decimal

Enter your choice here: """)

    def decconverter(decimal):
        search = definitions[decimal]
        return search

    def hexconverter(decimal):
        if decimal.isalpha():
            upperdeci = decimal.upper()
        else:
            upperdeci = decimal
        search = definitions.index(upperdeci)
        return search

    if decision == '1':
        divided = input("Decimal number? ")

        list1 = []

        while divided != 0:
            hexadecimal_1 = divided % 16
            list1.insert(0, decconverter(hexadecimal_1))
            divided /= 16

        string = ''
        hexadecimal = string.join(list1)


        print "Your hexadecimal number is: " + hexadecimal

    if decision == '2':
        hexanswer = raw_input("Print Hexadecimal? ")

        s = 0
        list_hexanswer = list(hexanswer)
        for number in list_hexanswer:
            newvalue = hexconverter(number)
            value = 16 ** (len(hexanswer) - list_hexanswer.index(number) - 1)
            newnew = newvalue * value
            s += newnew
            list_hexanswer.insert(list_hexanswer.index(number), 'X')
            idk = list_hexanswer.index(number)
            del list_hexanswer[idk]

        print s

    decision2 = raw_input("""
Would you like to keep using the converter? y/n """)

    if decision2 == 'n':
        print "Application Terminated"
    else:
        while decision2.isalpha() and decision2 != 'y':
            print "Invalid Answer"
            decision2 = raw_input("""
Would you like to keep using the converter? y/n """)

