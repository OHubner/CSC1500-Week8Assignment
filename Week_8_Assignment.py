
#1
firstName = "oliver"
#2
lastName = "HUBNER"
#3
print("Hello,", firstName.upper(), lastName.lower())
#4
print("\n\n")
#5
firstLast = "Oliver Hubner"
#6
print(firstLast[7:13])
#7
firstLast = firstLast.replace("Hubner", "Hubner, Wayne State University Student")
print(firstLast)
#8
print("\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\"")
#9
decimal1, decimal2 = 9.5, 1.2
#10
addDec = decimal1 + decimal2
subDec = decimal1 - decimal2
multDec = decimal1 * decimal2
divDec = decimal1 / decimal2
#11
print(str(decimal1) + " plus " + str(decimal2) + " equals " + str(addDec))
print("{} minus {} equals {}".format(decimal1, decimal2, subDec))
print("%s multiplied by %s equals %s" % (decimal1, decimal2, multDec))
#Below line does work, just says its a syntax error for some reason
print(f'{decimal1} divided by {decimal2} equals {divDec}')
#12
sq_root = round(multDec ** (1/2), 2)
print("The square root of %s equals %s" % (multDec, sq_root))
#13
month = "October"
day = 28
#14
print("\n\t\tToday is day {} of the month of {}".format(day, month))

