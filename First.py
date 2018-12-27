name = raw_input("What is your name? ")
row = raw_input("How many rows are seen? ")
column = raw_input("How many columns are seen? ")
total = int(row) * int(column)
print "Your name is %s" % (name)
print "Your total chair count is " + str(total)
print "What would you like to do next?"

action = raw_input("""Type in your next action
here: """)

print "You, %s, requested to " % (name) + action + """. You currently have not requested to do 
anything about your %s seats.""" % (total)


