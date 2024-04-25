#creating a program to run a costume rental shop system
#importing other modules
import Rent_costume
import Return_costume

#creating a function to display welcome message
def messagePrint():
    print("================================================================================")
    print("                    Welcome to the Costume Rental Shop System                   ")
    print("================================================================================")
    print("\n")
messagePrint()

# creating a function to display options
def selectOption():
    print("choose your option")
    print("Press 1 to rent a costume")
    print("Press 2 to return a costume")
    print("Press 3 to exit")
    print("\n")
    #use the while loop when the number is not in integer form.
    loop_1 = False
    while loop_1 == False:
        #using try except concept
        try:
            value = int(input("Enter your option you want:"))
            print("\n")
            return value
            loop_1 = True
            inuptOfUser()
        except:
            print("\n")
            print("Please select as your option")
            print("\n")


#creatinf function to run main program that contains different other functions            
def inuptOfUser():

    loop_2 = True
    while loop_2 == True:
        #connecting other function through select option
        userinput = selectOption()
        if userinput == 1:
            print("Let's rent a costume you want")
            print("\n")
            #importing the rental function 
            Rent_costume.mainfileRent()
            
            
        elif userinput == 2:
            print("Let's return a custome you want")
            print("\n") 
            #importing the return function 
            Return_costume.mainfileReturn()
            

        elif userinput == 3:
            print("Thank you for using this system")
            print("\n")
            loop_2 = False
            
        else:
            print("your option is invalid.Please select as your available option")
            print("\n")                       
inuptOfUser()
