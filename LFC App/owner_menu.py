from tabulate import tabulate

listMenu = [{'Cat':'Food','Name':'Chicken','Price':15000,'Stock':50},
            {'Cat':'Food','Name':'Rice','Price':8000,'Stock':50},
            {'Cat':'Food','Name':'Fries','Price':10000,'Stock':50},
            {'Cat':'Food','Name':'Burger','Price':20000,'Stock':50},
            {'Cat':'Drink','Name':'Cola','Price':9000,'Stock':50},
            {'Cat':'Drink','Name':'Sprite','Price':9000,'Stock':50},
            {'Cat':'Drink','Name':'Water','Price':7000,'Stock':50}]

listPackage = [{'Cat':'Pack','Name':'Double Chicken','Note':'Chicken 2 pcs, Rice 1 pcs, Cola 1 pcs',
                'Item':['Chicken',2,'Rice',1,'Cola',1],'Price':42000},
                {'Cat':'Pack','Name':'Chicken Fries','Note':'Chicken 1 pcs, Fries 1 pcs, Cola 1 pcs',
                'Item':['Chicken',1,'Fries',1,'Cola',1],'Price':38000}]

user = {'user':'pass',
        'owner':'pass'}   

# function for sorting purpose when adding new menu
def sortMenu(item):
    return item['Cat']

# function to make sure input is integer and > 0 
def validPositiveIntInput(choice):
    while True:
        try:
            num = int(input(choice))
            if num>0:
                return num
            else:
                print('\n*Invalid input!*\n')
        except ValueError:
            print('\n*Invalid input!*\n')

# function to make sure input is alphabet only
def validAlphaInput(choice):
    while True:
        try:
            inp = (input(choice).title())
            stat = inp.isalpha()
            if stat == True:
                return inp
            else:
                print('\n*Invalid input!*\n')
        except ValueError:
            print('\n*Invalid input!*\n')

# function to make sure input is string
def validStringInput(choice):
    while True:
        try:
            inp = str(input(choice))
            return inp
        except ValueError:
            print('\n*Invalid input!*\n')

# DISPLAY FUNCTION
def displayTable(table,headers):
    print(tabulate(table, headers=headers, showindex='never', tablefmt='grid'))

# DISPLAY ALL FOODS AND DRINKS DATA
def listAllMenu(listMenu):
    print('\n.........................\nList of Foods and Drinks\n.........................')
    # define new variabel for table headers we want
    headers = [ 'No', 'Category', 'Name', 'Price', 'Stock']
    # define new variabel to store data we want to use for List of Foods and Drinks
    tableFood = [[i + 1, menu['Cat'], menu['Name'], menu['Price'], menu['Stock']] for i, menu in enumerate(listMenu)]
    displayTable(tableFood,headers)

# DISPLAY MENU BY CATEGORY
def byCategory():
    inp = validAlphaInput('Enter category you want : ')
    print('\n.........................\nList of Foods and Drinks\n.........................')
    # define new variabel for table headers we want
    headers = ['No','Category','Name','Price']
    # define new variabel to store data we want to use for List of Foods and Drinks
    tableFood = [[i + 1,menu["Cat"],menu["Name"],menu["Price"],menu["Stock"]] for i, menu in enumerate(listMenu) if inp == menu["Cat"]]
    displayTable(tableFood,headers)

# DISPLAY PACKAGE DATA
def listOfPackage(listPackage):
    print('\n................\nList of Packages\n................')
    # define new variabel for table headers we want
    headers = ['Package','Cat','Name','Items','Price']
    # define new variabel to store data we want to use for List of Packages
    tablePack = [[i+1,menu["Cat"],menu["Name"],menu["Note"],menu["Price"]] for i, menu in enumerate(listPackage)]
    displayTable(tablePack,headers)

# OWNER MAIN MENU
def menuOwner():
    while True:
        action = validPositiveIntInput('\nMenu List :\n===========\n1. Menu setting\n2. Package setting\n3. Exit menu\nChoose action : ')
        # 1. MENU SETTING
        if action == 1:
            menuOwner1()
        # 2. PACKAGE SETTING
        elif action == 2:
            menuOwner2()
        elif action == 3:
        # 3. EXIT MENU
            print('\n*You are logging out!*')
            break
        else :
            print('\n*Invalid Input!*')

# 1. MENU SETTING
def menuOwner1():
    while True:
        action = validPositiveIntInput('\nMenu Setting :\n===============\n1. Display All Food & Drink Menu\n2. Display menu by category\n3. Add new menu\n4. Update menu\n5. Delete menu\n6. Back to previous menu\nChoose action : ')
        # MENU 1.1 DISPLAY ALL MENU
        if action == 1:
            listAllMenu(listMenu)
        # MENU 1.2 DISPLAY MENU BY CATEGORY
        elif action == 2:
            byCategory()
        # MENU 1.3 ADD NEW MENU
        elif action == 3:
            addNewMenu()
        # MENU 1.4 UPDATE MENU
        elif action == 4:
            updateMenu()
        # MENU 1.5 DELETE MENU
        elif action == 5:
            deleteMenu()
        # MENU 1.6 BACK TO PREVIOUS MENU
        elif action == 6:
            break
        else :
            print('\n*Invalid input!*')

## MENU 1.1 FUNCTION TO ADD NEW MENU
def addNewMenu():
    while True:
        try :
            # new menu category and name must be alphabet only
            catNew = validAlphaInput('\nAdd New Menu\n~~~~~~~~~~~~~\nEnter menu category (alphabet only): ')
            nameNew = validAlphaInput('Enter menu name (alphabet only): ')
            # check if the new name is already exit in menu
            if any(nameNew in menu["Name"] for menu in listMenu):
                print('\n*Name already exists!*\n')
                break
            # new menu price and stock must be integer and positive
            priceNew = validPositiveIntInput('Enter menu price: ')
            stockNew = validPositiveIntInput('Enter menu stock: ')
        except :
            print('\n*Invalid input!*')
            break
        # make a table for confirmation purpose 
        newMenu = {'Cat':catNew,'Name':nameNew,'Price':priceNew,'Stock':stockNew}
        addList = [[catNew,nameNew,priceNew,stockNew]]
        headerNew = ['Category','Name','Price','Stock']
        print('\nHere is the menu you want to add: ')
        displayTable(addList,headerNew)
        # confirm to add new menu
        while True:
            act2 = input('\nConfirm to add new menu (Yes/No): ').lower()
            if act2 == 'yes':
                listMenu.append(newMenu)
                listMenu.sort(reverse=True,key=sortMenu)
                print('\n*New menu added!*')
                break
            elif act2 == 'no':
                print('\n*Add process is cancelled!*')
                break
            else : print('\n*Invalid input!*')
        break

## MENU 1.2 FUNCTION TO UPDATE MENU    
def updateMenu():
    while True:
        # menu number must be integer and positive
        itemEdit = validPositiveIntInput('\nUpdate Menu\n~~~~~~~~~~~\nEnter menu number to update : ')
        if itemEdit <= (len(listMenu)):
            action = validPositiveIntInput('Select what you want to update:\n1. Update Name\n2. Update Category\n3. Update Price\n4. Update Stock\n5. Back to previous menu\nChoose action : ')
            # 1.2.1 UPDATE NAME
            if action == 1:
                # new name must be alphabet only
                nameEdit = validAlphaInput('\nUpdate Name\n~~~~~~~~~~~\nEnter update name (alphabet only): ')
                # check if the new name is already exist in menu
                if any(nameEdit in menu["Name"] for menu in listMenu):
                    print('\n*Name already exists!*\n')
                    break
                listMenu[itemEdit-1]["Name"] = nameEdit.title()
                print('\n*Menu updated!*')
                break
            # 1.2.2 UPDATE CATEGORY
            elif action == 2:
                # new category must be alphabet only    
                catEdit = validAlphaInput('\nUpdate Category\n~~~~~~~~~~~~~~~\nEnter update category (alphabet only): ')
                listMenu[itemEdit-1]["Cat"] = catEdit.title()
                listMenu.sort(reverse=True,key=sortMenu)
                print('\n*Menu updated!*')
                break
            # 1.2.3 UPDATE PRICE
            elif action == 3:
                # new price must be integer and positive
                priceEdit = validPositiveIntInput('\nUpdate Price\n~~~~~~~~~~~~~\nEnter update price : ')
                listMenu[itemEdit-1]["Price"] = priceEdit
                print('\n*Menu updated!*')
                break
            # 1.2.4 UPDATE STOCK
            elif action == 4:
                # new stock must be integer and positive
                stockEdit = validPositiveIntInput('\nUpdate Stock\n~~~~~~~~~~~~\nEnter update stock : ')
                listMenu[itemEdit-1]["Stock"] = stockEdit
                print('\n*Menu updated!*')
                break
            # 1.2.5 BACK TO PREVIOUS MENU
            elif action == 5:
                return
        else :
            print('\n*Invalid Input!*')

## MENU 1.3 FUNCTION TO DELETE MENU
def deleteMenu():
    while True:
        menuDel = validPositiveIntInput('\nDelete Menu\n~~~~~~~~~~~\nEnter menu number to delete : ')
        if menuDel in range(len(listMenu)+1):
            del listMenu[menuDel-1]
            print('\n*Menu deleted!*')
            break
        else :
            print('\n*Invalid input!*')

# 2. PACKAGE SETTING
def menuOwner2():
    while True:
        # display list of package
        listOfPackage(listPackage)
        act6 = validPositiveIntInput('\nPackage Setting :\n=================\n1. Add new package\n2. Update package name\n3. Update package price\n4. Delete package\n5. Back to previous menu\nChoose action : ')
        # MENU 2.1 ADD NEW PACKAGE
        if act6 == 1:
            addNewPack()
        # MENU 2.2 UPDATE PACKAGE NAME
        elif act6 == 2:
            updatePackName()
        # MENU 2.3 UPDATE PACKAGE PRICE
        elif act6 == 3:
            updatePackPrice()
        # MENU 2.4 DELETE PACKAGE MENU
        elif act6 == 4:
            delPack()
        # MENU 2.4 BACK TO PREVIOUS MENU
        elif act6 == 5:
            break
        else:
            print('Invalid Input!')

## MENU 2.1 ADD NEW PACKAGE
def addNewPack():
    listAllMenu(listMenu)
    newItem = []
    print('\nAdd New Package\n~~~~~~~~~~~~~~~~')
    while True:
        # user add items from food and drink list to new package
        packItem = validPositiveIntInput('Pick item number for new package : ')
        if packItem <= len(listMenu) :
            itemName = listMenu[packItem-1]["Name"]
            qtyItem = validPositiveIntInput('Enter items qty: ')
            # condition when user add new item to package
            if itemName not in newItem:
                act7 = input('Add other items? (Yes/No) ')
                if act7.lower() == 'yes':
                    newItem.append(itemName)
                    newItem.append(qtyItem)
                    continue
                elif act7.lower() == 'no':
                    newItem.append(itemName)
                    newItem.append(qtyItem)
                    break
                else :
                    print('\n*Invalid input!*\n')
                    continue
            # condition when user add existing item to package
            elif itemName in newItem:
                act7 = input('Add other items? (Yes/No) ')
                if act7.lower() == 'yes':
                    idx = newItem.index(itemName)
                    newItem[idx+1] += qtyItem
                    continue
                elif act7.lower() == 'no':
                    idx = newItem.index(itemName)
                    newItem[idx+1] += qtyItem
                    break
                else :
                    print('\n*Invalid input!\n*')
                    continue
        else :
            print('\n*Invalid input!*\n')
    # for loop to make note for new package
    for i in range(len(newItem)):
        if i == 0:
            newNote = str(newItem[i]) + ' '
        elif i == len(newItem)-1:
            newNote += str(newItem[i]) + ' pcs'
        elif i % 2 == 0:
            newNote += str(newItem[i]) + ' '
        elif i % 2 != 0:
            newNote += str(newItem[i]) + ' pcs, '
    print(f'\nNew package items : {newNote}')
    while True:
        # condition to make sure that new package name is consist of alphabet only
        newPackName = validStringInput('\nEnter new package name: ')
        # check if the new name is already exit in menu
        if any(newPackName in menu["Name"] for menu in listPackage):
            print('\n*Name already exists!*\n')
            break
        else :        
        # condition to make sure user input package price > 0 
            packPrice = validPositiveIntInput('Enter new package price : ')
            newPack = {'Cat':'Pack','Name':newPackName,'Note':newNote,'Item':newItem,'Price':packPrice}
            listPackage.append(newPack)
            print('\n*New package added*')
            break

## MENU 2.2 UPDATE PACKAGE NAME
def updatePackName():
    while True:
        editPack = validPositiveIntInput('\nUpdate Package Name\n~~~~~~~~~~~~~~~~~~~~\nEnter package number to update : ')
        if editPack <= (len(listPackage)):
            editName = validStringInput('Enter update package name : ')
            # check if the new name is already exist in menu
            if any(editName in menu["Name"] for menu in listPackage):
                print('\n*Name already exists!*\n')
                break
            listPackage[editPack-1]["Name"] = editName.title()
            print('\n*Package menu updated!*')
            break
        else :
            print('\n*Invalid input!*')

## MENU 2.3 UPDATE PACKAGE PRICE
def updatePackPrice():
    while True:
        editPack = validPositiveIntInput('\nUpdate Package Price\n~~~~~~~~~~~~~~~~~~~~~\nEnter package number to edit : ')
        if editPack <= (len(listPackage)):
            editPrice = validPositiveIntInput('Enter update package price : ')
            listPackage[editPack-1]["Price"] = editPrice
            print('\n*Package menu updated!*')
            break
        else :
            print('\n*Invalid input!*')

## MENU 2.4 DELETE PACKAGE MENU
def delPack():
    while True:
        packDel = validPositiveIntInput('\nDelete Package\n~~~~~~~~~~~~~~~\nEnter package number to delete : ')
        if packDel <= (len(listPackage)+1):
            del listPackage[packDel-1]
            print('\n*Package deleted!*')
            break
        else :
            print('\n*Invalid input!*')
            break