print """Here, I'll give you an actual action to take."""
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






