#adding in user input to give a description of what you want
items = input("Welcome to Ralphs, what would you like today: ")
print("I would like " + items)


#addition of "while true" keeps the loop continuous
while True:
    # the use of "float" allows our inputs to multiply
    quantity = float(input("quantity: "))
    price = float(input("price: "))

    total = price*quantity
    print("total: " + str(total))

#using if and else statement allows the user to enter the final part of the receipt
    if quantity == 0.0:
        print("Overall Total ")
        st = input("Would you like to add sales tax?: ")
        y = st
#give the sales tax a value to multiply to final total
        sales_tax = 9.5
        if st == y:
            print("Final Total: " + str(total*sales_tax))
        else:
            print("Final Total: " + str(total))
        break






#added overall variable to add the current total to the overall total








#if statement allows us to end the loop
