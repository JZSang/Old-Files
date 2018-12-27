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





