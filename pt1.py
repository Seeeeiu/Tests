'''
Restaurant Menu Order System

'''
import datetime
import random
import string
import sys
import os


# define classes!
class Restaurant:
    # attributes
    def __init__(self, name,menu=[]): #
        self.name = name
        self.menu = menu

    def welcome(self):
        print("Welcome to " + self.name)


#Your initial display menu should give a list of restaurants available to order from.
class Menu:
    # attributes
    def __init__(self,menulist=[]):
        # menulist is a list including menuitem classes
        self.menulist = menulist
    def display(self):
        print("This is used to print the menu")

# include item information
class MenuItem:
    # attributes
    def __init__(self, num,name, category,price):
        self.num = num
        self.category = category
        self.name = name
        self.price = price

# create the unique ticket for each order
class Ticket:
    # attributes
    def __init__(self, ID, orderList=[]):
        self.ID = ID
        self.orderList = orderList

'''
Each order should get a unique random ID that consists of alphanumeric
characters, and the user should be able to save the order in a file with a filename that
has the oder_xxxxxx_resturantname_MM/dd/yyyy_HHMMSS.txt.
'''

# read in the restaurant file and create classes
def readData(iFileName):

    iFile = open(iFileName,'r')
    restaurantList=[] # record the restaurant
    menuList=[] # record the items in the menu
    cursor =0 # record the menuitem number(reload when finish reading a menu)
    num = 0 # record the restaurant number
    for line in iFile:
        if line == "\n":
            break
        if line == "END\n":
            # add the menu(first transforme to class) to the restaurant class(choose from the restaurantList)
            restaurantList[num].menu = Menu(menuList)
            num += 1 #start a new restaurant
            menuList = [] #start a new blank menuList
        elif line.find(",")== -1:
            # add a new restaurant
            restaurantList.append(Restaurant(line))
            # clear the menulist count number to get ready for next munu
            cursor = 0
        else:
            category, name, price, = line.split(",")
            #temporary store the strings
            p = MenuItem(cursor+1,name, category, price)
            menuList.append(p)
            cursor+=1

    iFile.close()
    return restaurantList

# customers choose different restaurant
def displayRestaurant():

    print('''
        *================================================================*
        *                                                                *
        *              Welcome to Miami Fantastic Restaurants !           *
        *                                                                *
        *================================================================*
        ''')
    iFileName = "restaurant.txt"
    restaurants = readData(iFileName)
    num = 1
    for i in restaurants:
        print(num,": ",i.name)
        num+=1
    choice = input("Please choose your restaurant(enter the number):")
    a = int(choice)

    return restaurants[a-1]

# display the menu of each restaurant
def displayMenu():
    r = displayRestaurant()
    print()
    print('''
        *================================================================*
                          Welcome to '''+r.name +'''
        *================================================================*
        ''')
    print("NewMeal (n)".rjust(30), "Quit and create tickets(q)".rjust(30))

    # print the menu
    menuCategory = ['Appetizers']
    print()
    print(("「" + "Appetizers" + "」").center(80))
    print("============".center(80))
    index =0
    for i in r.menu.menulist:
        menuCategory.append(i.category)
        index+=1
        # only print category once
        if menuCategory[index]!= menuCategory[index-1]:

            print(("「" + i.category + "」").center(80))
            print("============".center(80))
        print(str(i.num).ljust(15),end="" )
        print(i.name.ljust(50), end="")
        print(("$" + i.price).ljust(15))

    return r

# get input
def getInput():
    x = input("Please enter your meal [1~n]\n(if you want to delete items, enter[-1~-n]): ")
    return x

# deal with different input
def inputType(x):
    if x == 'n':
        flag = 'new'
    elif x == 'q':
        flag = 'quit'
    elif int(x)>=1 and int(x)<=15 :
        flag = 'add'
    elif int(x)>=-15 and int(x)<=-1 :
        flag = 'delete'
    else:
        flag = 'wrong'
    return flag





# generate random id for tickets
def GenId():
    chars=string.ascii_letters+string.digits
    id =  ''.join([random.choice(chars) for i in range(6)])
    return id

# print the ticket
def printTicket(r,list):
    print()
    print("="*120)
    print("Your current meal has",len(list),"item(s).")
    Price = 0
    for meal in list:
        for i in r.menu.menulist:
            if meal == str(i.num):
                price = i.price
                Price+=float(i.price)
                print(str(i.num).ljust(10), i.category.ljust(30), i.name.ljust(60), ("$" + i.price).ljust(15))
    tax = round(Price*0.065,2)
    tip = round(Price*0.2,2)
    total = round(Price+tax+tip,2)
    print("="*120)
    print("Subtotal = ".rjust(80),("$"+str(Price)).rjust(10))
    print("Tax = ".rjust(80),("$"+str(tax)).rjust(10))
    print("Tip = ".rjust(80),("$"+str(tip)).rjust(10))
    print("Total = ".rjust(80),("$"+str(total)).rjust(10))

# create the ticket and quit
def quit(r,orderlist):

    print("Thank you for your order!")
    print("Your ticket has been printed.")
    print("Hope to see you again!")
    '''
    Each order should get a unique random ID that consists of alphanumeric
    characters, and the user should be able to save the order in a file with a filename that
    has the order_xxxxxx_restaurantname_MM/dd/yyyy_HHMMSS.txt.
    '''
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    GenId
    fileName = "order_"+GenId()+"_"+r.name.rstrip("\n")+"_"+str(month)+"/"+str(day)+"/"+str(year)+"_"+str(hour)+str(minute)+str(second)+".txt"


    dirname = os.path.dirname(fileName)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(fileName, 'w'):
        f = open(fileName, 'w')
        f.write("=" * 120 +"\n")
        f.write("Your ticket has "+str(len(orderlist))+ " item(s).\n")
        Price = 0
        for meal in orderlist:
            for i in r.menu.menulist:
                if meal == str(i.num):
                    price = i.price
                    Price += float(i.price)
                    f.write((str(i.num).ljust(10)+ i.category.ljust(30)+ i.name.ljust(60)+ ("$" + i.price).ljust(15))+"\n")
        tax = round(Price * 0.065, 2)
        tip = round(Price * 0.2, 2)
        total = round(Price + tax + tip, 2)
        f.write("=" * 120 +"\n")
        f.write("Subtotal = ".rjust(80)+("$" + str(Price)).rjust(10)+"\n")
        f.write("Tax = ".rjust(80)+("$" + str(tax)).rjust(10)+"\n")
        f.write("Tip = ".rjust(80)+("$" + str(tip)).rjust(10)+"\n")
        f.write("Total = ".rjust(80)+("$" + str(total)).rjust(10)+"\n")

    f.close()  # close the file


def main():

    r = displayMenu()
    input = getInput()

    orderList = []  # get order item key
    price = 0
    while inputType(input) == 'add' or inputType(input) == 'new' or inputType(input) == 'wrong' or inputType(
            input) == 'delete':
        if inputType(input) == 'new':
            print("Your previous meal has been cleaned, please order again. ")
            orderList = []
            input = getInput()
        if inputType(input) == 'wrong':
            print("Sorry, you entered the invalid number! Please enter again.")
            input = getInput()
        if inputType(input) == 'add':
            orderList.append(input)
        if inputType(input) == 'delete':
            input = input.strip('-')
            flag = False
            for i in orderList:
                if i == input:
                    orderList.pop(orderList.index(i))
                    flag = True
            if flag == False:
                print("Sorry,the item you delete is not in your meal, please check again!")

        printTicket(r,orderList)
        input = getInput()
    if inputType(input) == 'quit':
        quit(r,orderList)

main()