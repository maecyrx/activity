

user_number= int(input("how many number would you like"))
listnumbers= []

for x in range(user_number):
    message = input ("number?:")
    user_number.append(message)

    print(user_number)

for user_number in listnumbers:
    if user_number > "0":
        print(listnumbers + "positive")
    elif user_number < "0":
        print(listnumbers + "negative")
    else:
        print("error")