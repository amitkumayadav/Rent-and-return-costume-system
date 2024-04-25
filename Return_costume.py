#creating a program of return function
#importing time modules
import datetime
listCostume_2 = []

#creating a function which are add another function and import in main function
def mainfileReturn():
    loop =True
    while loop==True:#using while loop
        printStock() #call the function
        dictionary = dictionaryCostume()
        costumeID = validationCostume_1(dictionary)
        Amount=Requantity(dictionary,costumeID)
        abc = writeCostume_1(dictionary,costumeID,Amount)
        listCostume_2.append([dictionary[costumeID][0],dictionary[costumeID][1],dictionary[costumeID][2],Amount])
        ask_user=input("Do you want to rent another costume? Press Y to confirm, or any key to cancel.")
        if ask_user=="y":#using if and else statment
            loop=True
        else:
            detail= userInformation()
            moblieNumber = userNumber()
            charge = fine()
            bill(detail,moblieNumber,charge,dictionaryCostume,listCostume_2)
            loop=False

#creating function  to display the costume in table form
def printStock():
    print("================================================================================")
    print("ID\t  Custome Name\t    Custome Brand\t    Price\t    Quantity")
    print("================================================================================")
    file = open("stock_costume.txt","r")
    a = 1
    #using for loop to display costume
    for line in file:
        print(a,"\t"+line.replace(",","       "))
        a = a + 1
    print("================================================================================")
    print("\n")
    file.close()

#creating function  to display dictionary of available costume
def dictionaryCostume():
    file = open("stock_costume.txt","r")
    #creating empty dictionary
    costumeDictionary = {}
    costumeID = 1
    for line in file:
        line = line.replace("\n","")
        costumeDictionary.update({costumeID: line.split(",")})
        costumeID = costumeID + 1
    file.close()
    return costumeDictionary

#creatinfg function to ask costume ID by user 
def validationCostume_1(costumeDictionary):
    print(costumeDictionary)
    print("\n")
    loop_1=True
    while loop_1==True: #using while loop
        #using try and except
        try:
            validID = int(input("Enter the provide  ID of the Costume you want to return:"))
            loop_1=False
        
            print("\n")
        except:
            print("Please select as your option")
    while validID <= 0 or validID > len(costumeDictionary): #using  while loop
            print("\n")
            print("Enter provide a valid Costume ID")
            print("\n")
            validID = int(input("Enter provide the ID of the costume you want to return:"))
            print("\n")
    return validID

#creating function to ask the costume quantity by user
def Requantity(costumeDictionary,validID):
    loop_2 = True
    while loop_2==True: #using while loop
        #using try and except
        try:
            userQyantity=int(input("Enter the quantity of costume you want to return:"))
            loop_2=False
            print("\n")
        except:
            print("Please select as your option")

    quantitySelectCostume=costumeDictionary[validID][3]
    while userQyantity <=0: #using while loop
        print (" Invalid ")
        print("\n")
        userQyantity=int(input("Enter the quantity of costume you want to return:"))
    print("\n")
    # print(costumeDictionary)
    return  userQyantity

#creating a function to increase quantity through the user 
def writeCostume_1(costumeDictionary,validID,userQyantity):
    #increase quantity by user in text file
    costumeDictionary[validID][3] = int(costumeDictionary[validID][3])+int(userQyantity)
    #write the text file
    file = open("stock_costume.txt","w")
    for values in costumeDictionary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
        file.write("\n")
    file.close()

#creating a function to pay fine while it become more day  to return the costume 
def fine():
    loop_3=True
    while loop_3==True: #using while loop
        #using try and except function
        try:
            days=int(input("Enter the number of days you rented the costumes:"))
            print("\n")
            loop_3=False
        except:
            print("Invalid Input")
    return days

#creating a function ask user name
def userInformation():
    print("================================================================================")
    print("           Bill Generation would require  to enter your information.            ")
    print("================================================================================")
    loop_4=False
    while loop_4==False:#using while loop
        #using try and except function
        try:
            name=input("Enter  your full name:")
            print("\n")
            loop_4=True
        except:
            print("Invalid Input")
    return name

#creating a function ask user phone number
def userNumber():
    loop_5 = False
    #using while loop
    while loop_5 == False:
        #using try and except function
        try:
            phonenumber = input("Enter your Phone Number:")
            loop_5 = True
        except:
            print("Please provide a correct phone number")
        print("================================================================================")
        print("\n")
    return phonenumber

#creating a function tp print a bill by user of return
def bill(name,phonenumber,days,dictionary,listCostume2):
    #set date and time through import datetime
    date = str(datetime.date.today())
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    micro = str(datetime.datetime.now().microsecond)
    dateDisplay = date
    timeDisplay = hour + ":" + minute + ":" +second
    timeFile = hour+minute+second+micro
    #write a bill of rent of costume in text file
    file=open(name +"_ReturnCostume"+"["+timeFile+"]"+".txt","w")
    print("\n")
    file.write("================================================================================")
    file.write("\n")
    file.write("                        Bill of the Costume Rental Shop                         \n")
    file.write("================================================================================")
    file.write("\n")
    file.write("                    kamalpokhari,kathmandu   phone No: 123-456-7890             ")
    file.write("\n")
    file.write("================================================================================")
    file.write("\n")
    file.write("Name of costumer:"+name)
    file.write("\n")
    file.write("Phone Num,ber of costume:"+phonenumber)
    file.write("\n")
    file.write("Date:" +dateDisplay +"  "+ "Time:" +timeDisplay)
    file.write("\n")
    file.write("================================================================================")
    file.write("\n")
    file.write("Costume Name\t   Costume Brand\t    Costume Quantity\t   Costume price")
    file.write("\n")
    file.write("================================================================================")
    file.write("\n")
    file.write("\n")
    for values in listCostume_2:
        file.write(str(values[0])+"        "+str(values[1])+"            "+str(values[3])+"          "+str(values[2]))
        file.write("\n")
    file.write("================================================================================")
    file.write("\n")
    if days > 5:
        payFine = str((days-5)*10)
        file.write("Total Fine:"+"$"+ payFine)
    else:
        file.write("Dear user, No fine will be paid. Thank you for returning.")
        file.write("\n")
    file.write("\n")  
    file.write("================================================================================")
    file.write("\n")
    file.close()
    #open text file
    file=open(name +"_ReturnCostume"+"["+timeFile+"]"+".txt","r")
    #print text file
    print(file.read())
