print('welcome to Dhiraj Mart')

item = {'oppo phone': 13999, 'bot earphone': 199, 'vivo mobile': 11456, 'realme phone': 16500, 'vivo 5G': 21000, 'king earphone': 70, 'mi mobile': 9999, 'headphone': 599, 'charger': 300, 'iphone': 100500, 'vivo y53': 7499,}
cart = 0

print("Please chosoe product and Enter ------- ")
for keys, value in item.items():
    print('>',keys)
print("--> Enter product name to add cart\n--> Enter 'cart' to cheakout")
n = 0
while n<100:
    
    userinput = input('Enter product name --> ')
    print("**********************************************************")
    print("")
    userinputs = userinput.lower()
    if userinput == 'oppo phone':
        price = item.get(userinput)
        cart = price+cart
    elif userinput == 'bot earphone':
        price = item.get(userinput)
        cart = price+cart
    elif userinput == 'vivo mobile':
        price = item.get(userinput)
        cart = price+cart
    elif userinput == 'realme phone':
        price = item.get(userinput)
        cart = price+cart
    elif userinput == 'vivo 5G':
        price = item.get(userinput)
        cart = price+cart
    elif userinput == 'king earphone':
        price = item.get(userinput)
        cart = price+cart
    elif userinput == 'mi mobile':
        price = item.get(userinput)
        cart = price+cart
    elif userinput == 'headphone':
        price = item.get(userinput)
        cart = price+cart
    elif userinput == 'charger':
        price = item.get(userinput)
        cart = price+cart
    elif userinput == 'iphone':
        price = item.get(userinput)
        cart = price+cart
    elif userinput == 'vivo y53':
        price = item.get(userinput)
        cart = price+cart
    elif userinput == 'cart':
        print('Your total amount is --> ',cart)
        print("********Thanks for shoping Dhiraj Mart********")
    else:
        print("********Thanks for vist Dhiraj Mart********")
        exit()