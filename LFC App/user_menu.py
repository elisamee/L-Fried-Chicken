from tabulate import tabulate
from owner_menu import listMenu,listPackage,listOfPackage,validPositiveIntInput,displayTable,listAllMenu,byCategory

# defined list to store cart data
cart = []
listNameCart = []
listCatCart = []

# function to check whether the cart empty or not
def checkcart():
    while len(cart) == 0:
        print('\n*You have no item in your cart!*')

# USER MAIN MENU
def menuUser():
    while True:
        choice = validPositiveIntInput('''            
Menu List :\n===========
1. Food and Drink Menu
2. Package Menu
3. Cart
4. Payment
5. Exit menu
Choose menu number : ''')
        # 1. FOOD AND DRINK MENU
        if choice == 1:
            menuUser1()
        # 2. PACKAGE MENU
        elif choice == 2:
            menuUser2()
        # 3. CART
        elif choice == 3:
            if len(cart) == 0:
                print('\n*You have no item in your cart!*')
            else :
                displayCart()
                break
        # 4. PAYMENT
        elif choice == 4:
            if len(cart) == 0:
                print('\n*You have no waiting payment!*')
            else :
                payment()
        # 5. EXIT MENU
        elif choice == 5:
            exitMenu()
            break
        else : print('\n*Invalid input!*')

# 1. FOOD AND DRINK MENU
def menuUser1():
    while True:
        action = validPositiveIntInput('\nFood and drink menu :\n=====================\n1. Show All Food & Drink Menu\n2. Display menu by category\n3. Add item to cart\n4. Back to previous menu\nChoose action : ')
        # MENU 1.1 SHOW ALL MENU
        if action == 1:
            listAllMenu(listMenu)
        # MENU 1.2 DISPLAY MENU BY CATEGORY
        elif action == 2:
            byCategory()
        # MENU 1.3 ADD ITEM TO CART
        elif action == 3:
            addItem()
        # MENU 1.4 BACK TO PREVIOUS MENU
        elif action == 4:
            break
        else:
            print('\n*Invalid input!*')

# MENU 1.1 ADD ITEM TO CART
def addItem():
    while True:
        # check if the user input is valid or invalid
        try :
            buyFood = int(input('\nAdd item to cart\n~~~~~~~~~~~~~~~~\nChoose item number you want to buy: '))
            if not 0 < buyFood <= len(listMenu):
                raise ValueError
        except ValueError: 
            print('\n*Invalid input!*')
            continue
        indexFood = buyFood-1
        buyName = listMenu[indexFood]["Name"]
        # check if the user input is valid or invalid
        try:
            foodQty = int(input("Enter quantity to buy: "))
            if not foodQty > 0:
                raise ValueError
            if foodQty > listMenu[indexFood]["Stock"]:
                raise KeyError
        # condition when the stock is not enough
        except KeyError :
            print(f'\n*Stock is not enough, {listMenu[indexFood]["Name"]} stock remaining is {listMenu[indexFood]["Stock"]}*')
            return addItem()
        except ValueError:
            print('\n*Invalid Input!*')
            break
        # condition where the stock is enough
        listMenu[indexFood]["Stock"] -= foodQty
        # condition when cart is empty
        if len(cart) == 0:
            cart.append([buyName,foodQty,listMenu[indexFood]["Price"]])
            listNameCart.append(buyName)
            listCatCart.append(listMenu[indexFood]["Cat"])
            print('\n*Item is added to cart*')
            break
        # condition when cart not empty
        else:
            if buyName in listNameCart:
                idx = listNameCart.index(buyName)
                cart[idx][1] += foodQty
            else : 
                cart.append([buyName,foodQty,listMenu[indexFood]["Price"]])
                listNameCart.append(buyName)
                listCatCart.append(listMenu[indexFood]["Cat"])
        print('\n*Item is added to cart*')
        break

# 2. PACKAGE MENU
def menuUser2():
    while True:
        listOfPackage(listPackage)
        action = validPositiveIntInput('\nPackage menu :\n==============\n1. Add package to cart\n2. Back to previous menu\nChoose action : ')
        # MENU 2.1 ADD PACKAGE TO CART
        if action == 1:
            addPackage()
        # MENU 2.2 BACK TO PREVIOUS MENU        
        elif action == 2:
            break 
        else :
            print('\n*Invalid input!*')

# MENU 2.1 ADD PACKAGE TO CART
def addPackage():
    while True:
        # check validity of package number to buy
        buyPackage = validPositiveIntInput('\nAdd package to cart\n~~~~~~~~~~~~~~~~~~~\nChoose package number you want to buy: ')
        indexPackage = buyPackage-1
        if buyPackage <= len(listPackage):
            packName = listPackage[indexPackage]["Name"]
            packQty = validPositiveIntInput('Enter quantity to buy: ') 
            # condition when we add item that already in cart
            if packName in listNameCart:
                idx = listNameCart.index(packName)
                for i in range(len(listMenu)):
                    # look for menu in listMenu that included in the package
                    for j in range(0,len(listPackage[indexPackage]["Item"]),2): # step by 2 to get only menu name in Package Item
                        # condition to get the qty for each item in package
                        if listMenu[i]["Name"] == listPackage[indexPackage]["Item"][j]:
                            qtyItem = listPackage[indexPackage]["Item"][j+1]
                            # condition to check whether the stock for each item is available or not
                            if listMenu[i]["Stock"] < packQty * qtyItem:
                                print('\n*Stock is not enough!*')
                                return
                            else :        
                                listMenu[i]["Stock"] -= packQty*qtyItem
                    continue
                cart[idx][1] += packQty
                print('\n*Item is added to cart*')
                break
            # condition when we add new item to cart
            else : 
                for i in range(len(listMenu)):
                    for j in range(0,len(listPackage[indexPackage]["Item"]),2): # step by 2 to get only menu name in Package Item
                        if listMenu[i]["Name"] == listPackage[indexPackage]["Item"][j]:
                            qtyItem = listPackage[indexPackage]["Item"][j+1]
                            # condition to check whether the stock available or not
                            if listMenu[i]["Stock"] < packQty*qtyItem:
                                print('\n*Stock is not enough!*')
                                return
                            else :        
                                listMenu[i]["Stock"] -= packQty*qtyItem
                    continue
                cart.append([packName,packQty,listPackage[indexPackage]["Price"]])
                listNameCart.append(packName)
                listCatCart.append(listPackage[indexPackage]["Cat"])
                print('\n*Item is added to cart*')
                break

# 3. CART DISPLAY and CART MENU
def displayCart():
    while True:
        # print cart table
        print('\n...........\nCart List\n...........')
        headerCart = ['Item','Qty','Price']
        displayTable(cart,headerCart)
        action = validPositiveIntInput('\nCart menu :\n===========\n1. Continue shopping\n2. Delete item in cart\n3. Continue to payment\nChoose action : ')
        # MENU 3.1 CONTINUE SHOPPING
        if action == 1:
            return menuUser()
        # MENU 3.2 DELETE ITEM IN CART
        elif action == 2:
            checkcart()
            delItem()
        # MENU 3.3 CONTINUE TO PAYMENT
        elif action == 3:
            checkcart()
            payment()
            return menuUser()
        else : 
            print('\n*Invalid input!\n*')

# MENU 3.2 DELETE ITEM IN CART
def delItem():
    while True:
        itemDel = (input('\nDelete item in cart\n~~~~~~~~~~~~~~~~~~~\nEnter item name to delete : ').title())
        # condition to make sure that itemDel is exist in cart
        if itemDel in listNameCart:
            idxDel = listNameCart.index(itemDel)
            qty = cart[idxDel][1]
            # condition for package menu to add back the stock after package in cart deleted
            if listCatCart[idxDel] == 'Pack':
                for i in range(len(listPackage)):
                    if itemDel == listPackage[i]["Name"]:
                        idxPackDel = i
                for i in range(len(listMenu)):
                    for j in range(len(listPackage[idxPackDel]["Item"])):
                        if listMenu[i]["Name"] == listPackage[idxPackDel]["Item"][j]:
                            qtyItem = listPackage[idxPackDel]["Item"][j+1]
                            listMenu[i]["Stock"] += qty*qtyItem               
                del cart[idxDel]
                del listNameCart[idxDel]
                del listCatCart[idxDel]
                print('\n*Item deleted!*')
                break
            # condition to add back the stock after item in cart deleted
            else :
                for i in range(len(listMenu)):
                    if itemDel == listMenu[i]["Name"]:
                        idxItem = i
                listMenu[idxItem]["Stock"] += qty
                del cart[idxDel]
                del listNameCart[idxDel]
                del listCatCart[idxDel]
                print('\n*Item deleted!*')
                break            
        else : 
            print('\n*Invalid input!*')
            break

# MENU 3.3 CONTINUE TO PAYMENT
def payment():
    print('\n..............\nPayment List:\n..............')
    headers=('Name','Qty','Price','Total')
    total = []
    # variable for total shopping amount
    sumPrice = 0
    for i in range(len(cart)):
        tot = [cart[i][0],cart[i][1],cart[i][2],cart[i][1]*cart[i][2]]
        total.append(tot)
        sumPrice += cart[i][1]*cart[i][2]
    displayTable(total,headers)
    print(f'\n*Shopping total price = {sumPrice}*\n')
    while True:
        money = validPositiveIntInput('Enter the amount of money: ')
        change = abs(money-sumPrice)
        if money > sumPrice:
            print(f'\n*Thank you for shopping !*\n*Your change is {change}*')
            break
        elif money < sumPrice:
            print(f'\n*Your money short by {change}*\n')
        elif money == sumPrice:
            print('\n*Thank you for shopping!*')
            break
    cart.clear()
    listNameCart.clear()
    listCatCart.clear()

# 5. EXIT MENU
def exitMenu():
    while True:
        if len(cart) != 0:
            try :
                userOpt = input('You have items in your cart, are you sure to exit? (Yes/No) ')
            except :
                print('\n*Invalid input!*')
                continue
            if userOpt.lower() == 'yes':
                print('\n*You are logging out!*')
                cart.clear()
                listNameCart.clear()
                break
            elif userOpt.lower() == 'no':
                return menuUser()
            else :
                print('\n*Invalid input!*')
        else :
            print('\n*You are logging out!*')
            break