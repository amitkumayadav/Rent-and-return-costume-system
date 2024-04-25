#creating a program of rent function
#importing time modules
import datetime
listCostume_1 =[]

#creating a function which are add another function and import in main function
def mainfileRent():    
    loop=True
    while loop==True: #using while loop
        printStock() #call function 

        dictionary = dictionaryCostume()
        costumeID = validationCostume(dictionary)
        Amount = quantityCostume(dictionary,costumeID)
        abc = writeCostume(dictionary,costumeID,Amount)


        Rate =dictionary[costumeID][2].replace("$","")
        Total=int(float(Rate)*Amount)
        listCostume_1.append([dictionary[costumeID][0],dictionary[costumeID][1],dictionary[costumeID][2],Amount,Total])
        userAsk=input("Do you want to rent another costume? Press Y to confirm, or any key to cancel.")
        if userAsk == "y": # using if and else statment
            loop=True
        else:
            information= userInformation()
            moblieNumber = userNumber()
            billRent(information,moblieNumber,dictionaryCostume,listCostume_1)
            loop=False

#creating function  to display the costume in table form
def printStock():
    print("================================================================================")
    print("ID\t  Custome Name\t    Custome Brand\t    Price\t    Quantity")
    print("================================================================================")
    # open text file 
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

#creatinfg function to ask costume ID by user and check costume ID is available or not through the user
def validationCostume(costumeDictionary):
    print(costumeDictionary)
    print("\n")
    loop=True
    while loop == True: # using while loop
        #using try and except
        try:
            validID = int(input("Enter the provide  ID of the costume you want:"))
            loop = False
            print("\n")
        except:
            print("Please select as your option")
    while validID <= 0 or validID > len(costumeDictionary): # using while loop
        #using try and except
        try: 
            print("\n")
            print("Enter provide a valid Costume ID yopu want:")
            print("\n")
            validID = int(input("Enter the provide  ID of the costume you want:"))
            print("\n")
        except:
            print("Please select as your option")
    #show message while costume ID is check
    if (int(costumeDictionary[validID][3])) == 0: # using if and else statment
        print("================================================================================")
        print("                      Your desired costume is unavailable.                      ")
        print("================================================================================")
        print("\n")
    else :    
        print("================================================================================")
        print("                       Your desired costume is available.                       ")
        print("================================================================================")
        print("\n")
    return validID 

#creating function to ask the costume quantity by user
def quantityCostume(costumeDictionary,validID):
    loop_2 = True
    while loop_2==True: #using while loop
        #using try and except
        try:
            userQyantity=int(input("Enter the quantity of costume you want to return:"))
            loop_2=False
            #print("\n")
        except:
            print("Please select as your option")

    quantitySelectCostume=costumeDictionary[validID][3] # call quantity from text file
    #using while loop
    while userQyantity <=0 or userQyantity> int(quantitySelectCostume):
        print ("Dear User, Quantity you looking for is not available in our shop. Please recheck")
        print("\n")
        userQyantity=int(input("Enter the quantity of costume you want:"))
    print("\n")
    return  userQyantity

#creating a function to reduce quantity through the user 
def writeCostume(costumeDictionary,validID,userQyantity):
    costumeDictionary[validID][3] = int(costumeDictionary[validID][3])-int(userQyantity) #reduce quantity by user in text file

    #write the text file
    file = open("stock_costume.txt","w")
    for values in costumeDictionary.values(): #using for loop
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
        file.write("\n")
    file.close()

#creating a function ask user name
def userInformation():
    print("================================================================================")
    print("           Bill Generation would require  to enter your information.            ")
    print("================================================================================")
    
    loop=False
    while loop==False: #using while loop
        #using try and except
        try:
            name=input("Enter  your full name:")
            print("\n")
            loop=True
        except:
            print("Please provide a valid input")
    
    return name

#creating a function ask user phone number
def userNumber():
    loop_4 = False
    while loop_4 == False: #using while loop
        #using try and except
        try:
            phonenumber = input("Enter your Phone Number:")
            loop_4 = True
        except:
            print("Please provide a correct phone number")
        print("================================================================================")
        print("\n")
    return phonenumber

#creating a function tp print a bill by user of rent
def billRent(name,phonenumber, dictionary,listCostume):
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
    file=open(name +"_RentCostume"+"["+timeFile+"]"+".txt","w")
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
    file.write("Name:"+name) #call name from user
    file.write("\n")
    file.write("Phone Number:"+phonenumber) #call number from user
    file.write("\n")
    file.write("Date:" +dateDisplay +" "+ "Time:" +timeDisplay)
    file.write("\n")
    file.write("================================================================================")
    file.write("\n")
    file.write("Costume Name\t   Costume Brand\t Costume Quantity\t Costume price")
    file.write("\n")
    file.write("================================================================================")
    file.write("\n")
    file.write("\n")
    totalPriceCostume = 0
    for values in listCostume_1:
        file.write(str(values[0])+"        "+str(values[1])+"            "+str(values[3])+"          "+str(values[2]))
        file.write("\n")
        totalPriceCostume = totalPriceCostume + values[-1]
    file.write("\n")
    file.write("================================================================================")
    file.write("\n")
    file.write("Total price of Costume:" +"$"+ str(totalPriceCostume))
    file.write("\n")
    file.write("================================================================================")
    file.write("\n")
    file.close()
    #open text file
    file=open(name +"_RentCostume"+"["+timeFile+"]"+".txt","r")
    #print text file
    print(file.read())



