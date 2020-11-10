print("Welcome, I am here to help you convert kilometres to miles.")

while True:
    print("Please enter the value of kilometres for conversion. Enter just the number please. ")

    km = float(input("Kilometres: "))

    miles = km * 0.621371

    print("This is " + str(miles) + " miles")

    another_conversion = input("Do you want another conversion? Please answer with yes or no: ")

    if another_conversion.lower() != "yes" and another_conversion.lower()!= "y":
        print ("Ok, by now you know all conversions by heart.")
        break


        #s ovim zadatkom sam se baaaaš namucila.