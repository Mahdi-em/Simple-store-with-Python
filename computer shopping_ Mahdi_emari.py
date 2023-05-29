import sys 
shopping_cart = dict()
data = {
    210:    {'name': 'Intel Core i7','Product Type':'Processors/CPUs', 'price':29700, 'desc':
             '12700K Alder Lake 3.6GHz Twelve-Core LGA 1700 Boxed Processor ', 'inventory': 5},
    
    211:    {'name': 'Intel Core i5','Product Type':'Processors/CPUs', 'price': 11500, 'desc':
             '10400F Desktop Processor 6 Cores up to 4.3 GHz Without Processor Graphics LGA1200', 'inventory': 3},
    
    212:    {'name': 'AMD Ryzen™ 9','Product Type':'Processors/CPUs', 'price': 32900,'desc':
             '5900X 12-core, 24-Thread Unlocked Desktop Processor', 'inventory': 2},
    
    213:    {'name': 'AMD Ryzen™ 7','Product Type':'Processors/CPUs', 'price': 34700 , 'desc':
             ' 7700X Raphael AM5 4.5GHz 8-Core Boxed Processor ', 'inventory': 5},
    
    214:    {'name': 'Lenovo ThinkPadE15','Product Type':'Laptops/Notebooks', 'price':89300, 'desc':
             'Gen 4 15.6" Laptop Computer - Gray', 'inventory': 2, 'color':'Gray'},

    215:    {'name': 'HP EliteBook','Product Type':'Laptops/Notebooks', 'price': 64900, 'desc':
             'Intel Core i5 12th Gen 1235U 1.3GHz Processor and 16GB DDR4-3200 RAM  ', 'inventory': 3, 'color':'Silver'},
    
    216:    {'name': 'ASUS ZenBookPro14','Product Type':'Laptops/Notebooks', 'price': 229900 , 'desc':
             'Intel Core i9 12th Gen 12900H 1.8GHz Processor,RTX 3050 Ti 4GB GDDR6 ', 'inventory': 2, 'color':'black'},
    
    217:    {'name':'Dell Inspiron16Plus','Product Type':'Laptops/Notebooks', 'price': 139900, 'desc':
             'Intel Core i7 12th Gen 12700H 1.7GHz Processor,16GB DDR5-4800 RAM', 'inventory': 2, 'color':'Dark Green'},
    
    217:    {'name':'ASUS VG32AQL1A31.5','Product Type':'Computer Monitors', 'price': 34900, 'desc':
             '2K QHD (2560 x 1440) 170Hz Gaming Monitor', 'inventory': 4},

    217:    {'name':'LG 32UN650','Product Type':'Computer Monitors', 'price': 42900, 'desc':
             'W.AUS 32" 4K UHD (3840 x 2160) 60Hz LED Monitor', 'inventory': 4},

    217:    {'name':'Samsung Odyssey Neo','Product Type':'Computer Monitors', 'price': 139900, 'desc':
             ' G8 G85NB 32" 4K Ultra HD (3840 x 2160) 240Hz Curved Screen Monitor', 'inventory': 2},
    
}

def login():
    attempt = 0
    while True:
        useradmin_inp=input("Are you an admin or a user?: ")
        if useradmin_inp=='user':
            user_inp=input("Enter your username  : ")
            pass_inp=input("Enter your password  : ")
            if user_inp=="mahdi" and pass_inp=="1234":
                welcome_message(user_inp)
                main_user()
            else:
                print("Invalid password. Please enter valid password")
                attempt += 1
                if attempt > 3:
                    print("Please refer to the source codes")
        elif useradmin_inp=='admin':
            user_inp=input("Enter your username  : ")
            pass_inp=input("Enter your password  : ")
            if user_inp=="mahdiem" and pass_inp=="4321" :
                welcome_message_ad(user_inp)
                main_admin()
                
            else:
                print("Invalid password. Please enter valid password")
        else:
            print("Invalid user type. Enter valid user type")

def welcome_message(user_inp):
    print(f''' ***Welcome {user_inp} to Computer Equipment Online Store/n***
select the number for the action that you  would like to do
1-view shoping list
2-add items to shoping list
3-remove item form shoping list
4-show shopping cart
5-show_factore(checkout)
6-clear shoping list
7-help
8-logout(Log in to the login page)
9-exit

''')
def welcome_message_ad(user_inp):
    print(f''' ***Welcome admin: {user_inp} *** /n
select the number for the action that you  would like to do
1-Income and Loss
2-logout(Log in to the login page)
3-exit''')


    
def show_menu():
    for code in data:
            print(f'code: {code} , name: {data[code]["name"]} , Product Type:{data[code]["Product Type"]} ,  price: {data[code]["price"]},inventory:{data[code]["inventory"]}')
def show_help():
    print('''In order for the program to work properly, you can reach your desired operation
by choosing one of the numbers listed in the list below.
        1-view shoping list
        2-add items to shoping list
        3-remove item form shoping list
        4-show shopping cart
        5-show_factore(checkout)
        6-clear shoping list
        7-help
        8-logout(Log in to the login page)
        9-exit''')
    
def show_factore(shopping_cart):
    print("**Sales Invoice**")
    for item_code in shopping_cart:
        print(f'CodeItem:{item_code} || Name:  {data[item_code]["name"]} || Number of products :{shopping_cart[item_code]} || price:{data[item_code]["price"]}')
        
            
    amount = 0
    for item_code in shopping_cart:
        revenue = data[item_code]['price'] * shopping_cart[item_code]
        amount = revenue + amount
    print ("Total price of products ",amount)
    
def Profit_loss():
    total1=0
    total2=0
    for code in data:
#sood =Profit = Selling Price – Cost Price.
        total1+=((data[code]["inventory"]*data[code]["price"])-(data[code]["inventory"]*data[code]["price"]-1000 ))
#zyan =Loss = Cost Price - Selling Price
        total2+=(((data[code]["inventory"]*data[code]["price"]-1000-data[code]["inventory"]*data[code]["price"]) ))
    print(f"Product profit :{total1}\n amount lost : {total2}")
    
    
def addItem():
    try:
        added1=input("enter the itemcode and quality  : ")
        if len(added1.split()) != 2:
                print('wrog input')
        else:
            added2=added1.split()
            item=int(added2[0])
            quality=int(added2[1])
        if quality <= data[item]['inventory']:
            shopping_cart.setdefault(item, 0)
            shopping_cart[item] += quality
            data[item]['inventory'] -= quality
            print(f" Product with code '{item}' was added to your cart")
            print(f" The quality is {quality}")
            print(f"Your shopping cart ==>  {shopping_cart}")
        else:
            print("Not available in stock")
    except Exception as e:
            print('somethiong else happend!', e)
        
            
def removeItem():
        removed1=input("Enter the Itemcode : ")
        if len(removed1.split()) != 1:
                print('wrog input')
        else:
            removed2=removed1.split()
            item=int(removed2[0])
            shopping_cart.pop(item)
            print(f"'{removed1}' has been remove to your cart.")
            print(f"Shopping cart after deleting the item {shopping_cart}")


def clearshooping_cart():
    shopping_cart.clear()
    print(f"All products in your cart have been removed {shopping_cart}")
    
    
def showshopping_cart():
    if len(shopping_cart) == 0:
        print("The cart is empty")
    else:
        for item_code in shopping_cart: 
            print(f'CodeItem:{item_code} || Name:  {data[item_code]["name"]} ||Number of products :{shopping_cart[item_code]} ||price:{data[item_code]["price"]}')
def logout():
    print("You have successfully logged out")
    login()
               
def main_admin():
    while True:
        try:
            number=int(input("'Make your selection???' "))
            if number==1:
                Profit_loss()
            elif number==2:
                logout()
            elif number==3:
                print("Good bye")
                sys.exit()
        
            else:
                print('command not found')
                
        except Exception as e:
            print('somethiong else happend!', e)
        
             
def main_user():
    attempt = 0
    while True:
        try:
            number = input('Make your selection???')
            if number != None:
                if number== '1':
                    show_menu()
                elif number == '2':
                     addItem()
                elif number == '3':
                     removeItem()
                elif number=='4':
                     showshopping_cart()
                elif number=='5':
                     show_factore(shopping_cart)
                elif number=='6':
                    clearshooping_cart()     
                elif number=='7':
                    show_help()
                elif number=='8':
                    logout()
                elif number=='9':
                    print("Thank you for visiting our store")
                    sys.exit()
                else:
                    print('command not found')
                    attempt += 1
                    if attempt > 3:
                        print('You were wrong more than three times')
                        show_help()
            else:
                ("Please select the desired number ")
        except Exception as e:
            print('somethiong else happend!', e)
                        
                                                    
login()
