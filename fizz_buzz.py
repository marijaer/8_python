guess = int(input("Enter a number between 1 and 100: "))

for x in range (1,guess+1):

    if x % 3 == 0 and x % 5 == 0: #ako ovaj uvjet stavim pod elif onda loop ne prepoznaje taj uvjet. Zašto? (pitam jer sam inicijalno stavila if X%3 == 0 print(Fizz), elif x%5 == 0 print(buzz) elif x%3==0 and x%5==0 print(fizzbuzz) else print(x)
        print("fizzbuzz")

    elif x % 5 == 0:
        print("buzz")

    elif x % 3 == 0:
        print("fizz")

    else:
        print(x)