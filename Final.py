while True:
    choice = raw_input("Please select which calculator you would like to access (quadratic or exponential?) ")
    quadratic = ['quad', 'quadratic', 'Quadratic']
    exponential = ['exp', 'exponential', 'Exponential']
    if choice in quadratic:
        print "Welcome to the Quadratic Calculator!"

        A = float(input("Enter your A coefficient: "))
        B = float(input("Enter your B coefficient: "))
        C = float(input("Enter your C coefficient: "))

        print "Your equation seems to be %sx^2 + %sx + %s" % (A, B, C)

        if raw_input("Would you like to proceed to the calculation (y/n)? ") == 'y':
            determiner = (B * B) - 4 * A * C
            og = determiner
            if determiner < 0:
                print("This is not possible!")
            if determiner > 0 and A != 0:
                    thisthing = determiner / 2
                    answer = (thisthing + 2) / 2
                    for x in range(40):
                        new = og / answer
                        answer = (new + answer) / 2

                    first = (-B + answer) / (2 * A)
                    second = (-B - answer) / (2 * A)
                    print(first, second)
            elif A == 0:
                first = -(C / B)
                print(first)
            elif determiner == 0:
                first = (-B) / (2 * A)
                print(first)
        else:
            print("Pfft, well I didn't want to show you anyways.")






    elif choice in exponential:
        print """Welcome to the Exponential Calculator!"""
        name = raw_input("What's your name? ")
        basevar_1 = input("What is the base number? ")
        exponentvar_2 = input("What is the exponent? ")


        exponentvar_2 -= 1



        if isinstance(exponentvar_2, float):
            exponentvar_2 += 1
            floated = 1 / exponentvar_2
            if int(floated) == 2:
                thisthing = basevar_1 / 2.
                answer = (thisthing + 2) / 2
                for x in range(40):
                    new = basevar_1 / answer
                    answer = (new + answer) / 2




        calculate = basevar_1
        if isinstance(exponentvar_2, int):
            if exponentvar_2 == 0:
                answer = basevar_1
            elif exponentvar_2 == -1:
                answer = 1
            elif exponentvar_2 <= -2:
                exponentvar_2 += 2
                newexp = -exponentvar_2
                if newexp == 0:
                    answer = 1 / float(basevar_1)
                for x in range(newexp):
                    calculate *= float(basevar_1)
                    answer = 1 / calculate
            else:
                for x in range(exponentvar_2):
                    calculate *= basevar_1
                    answer = calculate


        print answer




        print """Congratulation! You have successfully trialed Jason's Exponential Calculator. You have earnt %s thank(s) from me!
        Thank you for your patronage, %s!""" % (answer, name)

    else:
        print "Unknown Command"





