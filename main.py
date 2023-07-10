from operation_rent import *
from operation_return import *
#main menu
print("------------------------------------------------------------")
print("\t Welcome to costume rental application \t")
print("------------------------------------------------------------")
print("")
def displaymessage():
        try:
                
                while(True):
                        print("\n Select desirable option")
                        print("(1) || Press 1 to rent a costume.")
                        print("(2) || Press 2 to return a costume.")
                        print("(3) || Press 3 to exit \n")

                        #if user input any string value then the try except will handel the exception
                        try:                       
                                #asking the user whether he/she want to rent,return costume or exit the application 
                                option = int(input("Enter a option: "))

                        except:
                                print("\nInvalid option! please enter a valid option")
                                displaymessage()

                        #if user input 1 then this condition will run
                        if(option == 1):
                            print("\n+++++++++++++++++++++++++++")
                            print("    Let's rent a costome")
                            print("+++++++++++++++++++++++++++")
                            print("")
                            #calling rent_costume function
                            rent_costume_function()

                        #if user input 2 then this condition will run        
                        elif(option == 2):

                            print("+++++++++++++++++++++++++++")
                            print("\nLet's return a costome")
                            print("+++++++++++++++++++++++++++")
                            print("")
                            costume_return()

                        #if user input 3 then the 
                        elif (option == 3):
                            print("")
                            print(" Thank you for using our application")
                            print("")
                            break
                        
                        #if user input any other number except 1,2,3 then the else condition will execute 
                        else:
                            print("Invalid input. Please choose a valid value ")

        except:
                print("Invalid input. please input a valid value")

    


displaymessage()









            

   
