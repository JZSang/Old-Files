while True:
    name = raw_input("What is your name? ")
    print ("Thanks for entering the I N T E R S E C T I O N C A L C U L A T O R, %s!") % (name)
    print ("First, we need to enter your first equation.")
    print ("This is the format we are following: Ax + B")
    A = float(input("What is your A value? "))
    B = float(input("What is your B value? "))
    print("Your first equation is %sx + %s.") % (A, B)

    print ("Second, we need to enter your Second equation.")
    C = float(input("What is your A value? "))
    D = float(input("What is your B value? "))

    print("Your first equation is %sx + %s.") % (C, D)

    New_x = A - C
    New_b = D - B

    X_Value = New_b / New_x

    Y_Value = A * X_Value + B

    print("These values intersect at (%s, %s).") % (X_Value, Y_Value)