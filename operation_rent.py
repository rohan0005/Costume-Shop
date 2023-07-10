from datetime import *
from dictionary_conversion import *

#creating empty list to store stocks costume details after customer rent the costumes
item_costume=[]

#creating empty list to store brand names of costume
item_brand=[]

#creating empt list to store total price of different costumes
item_price=[]

#creating empty list to store total cosumes and quantity
costume_and_qty=[]



#Functions



def rent_costume_function():
            #asking user to input ID of costume        
            costume_dictionary_conversion()
            try:
                                
                option = int(input ("\nEnter the ID of costume:"))
                o=option
                selected_item=costume_dic[o]
                qty=selected_item[3]

            except:
                print("\n**********************************")
                print("  Please enter a valid input!!")
                print("**********************************\n")
                rent_costume_function()
            
            try:
                                
                if int(qty)>0 and option<=len(costume_dic):
                    print("\n\n++++++++++++++++++++++++")
                    print("  Costume available")
                    print("++++++++++++++++++++++++\n\n")
                    #asking user to input quantity of costume
                    quantity= int(input("Enter the quantity: "))
                    q=quantity
                    costume_and_qty.append(q)
                    quantity_validate(q,o)



                else:
                    #if user input invalid input error message will display
                    print("\n\n++++++++++++++++++++++++++++++++++++++++")
                    print("  Please provide a valid input")
                    print("++++++++++++++++++++++++++++++++++++++++\n\n")
                #returning local variables to use in other functions
                return o
                return q
            
            except:
                lp=False
                while lp==True:
                    print("\n\n++++++++++++++++++++++++++++++++++++++++")
                    print("  Please provide a valid input")
                    print("++++++++++++++++++++++++++++++++++++++++\n\n")
                    rent_costume_function()
                    lp==False
                 
                  
              
    

def quantity_validate(q,o):          
            #using local variables after returning
            quantity=q
            option=o

            selected_item=costume_dic[option]
            #if quantity is greater than what we have in stock an error message will displayed
            if int(selected_item[3])<quantity:
                print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Quantity provide is greater than what we have in stock")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                print(costume_dic)
                print("")
                rent_costume_function()

            elif int(quantity)<=0:
                print("Invalid quantity!!!!\n")
                rent_costume_function()
                
            else:
                '''
                if user select the quantity then the quantity will decrease from dictionary and
                txt file and it will displayes after updating
                '''
                lp=True
                while lp == True:
                    selected_costume = costume_dic[option]
                    update_qty= int(selected_costume[3])-quantity
                    selected_costume[3]=str(update_qty)
                    #calling stock_update function to update the quantity
                    stock_update()
                    #displaying dictionary after updating quantity
                    print(costume_dic)
                    print("")
                
                    #using append to store price in item_price list, removing "$"  sign and multiplying quantity
                    item_price.append(float(selected_costume[2].strip().strip("$"))*quantity)
                    #using append to store costume in item_costume list which user will select 
                    item_costume.append(selected_costume[0])
                    item_brand.append(selected_costume[1])
                    lp=False
                

         
                loop=True
                #if loop is True then user can rent other costume else name of costumer should be input
                while loop==True:

                        choice = input("Enter 'y' to rent another else enter any value: ")
                        if choice =="y":
                                rent_costume_function()
                        else:
                                condition = True
                                while condition == True:
                                    t_price=sum(item_price)
                                    condition = False
                                print("Total price is",t_price)
                                
                                amount_received=float(input("Enter the amount you will pay now:"))
                                if float(t_price)<float(amount_received):
                                    print("\nAmount you enter is greater that total amount\n")
                                    quantity_validate(q,o)                            

                                else:
                                    total_amount_due=float(t_price)-float(amount_received)
                                    print("Total amount to be paid:",total_amount_due)

                                        
                                    name=input("\nEnter your full name: ")
                                    n=name
                                    phone=input("\nEnter your contact number: ")
                                    p_num=phone
                                    print("")
                                    #calling rent_bill function aftr asking name from customer
                                    rent_bill(n,p_num,t_price,total_amount_due,amount_received)
                                    return n
                                    return p_num
                                    return t_price
                                    return total_amount_due
                                    return amount_received
                                    #loop value will be changed into false
                                    loop=False            



def rent_bill(n,p_num,t_price,total_amount_due,amount_received):
        #this function is used to generate bill and write it in a txt file

        #assigning variables
        name=n
        price=t_price
        p=str(price)
        c=item_costume
        cos=str(item_costume)
        brand=str(item_brand)
        phone=p_num
        total_due=str(total_amount_due)
        received=str(amount_received)
        dt=datetime.now()
        year=str(dt.year)
        month=str(dt.month)
        day=str(dt.day)
        hour=str(dt.hour)
        minute=str(dt.minute)
        second=str(dt.second)
        date_time=year+"/"+month+"/"+day+" "+hour+":"+minute+":"+second

        #Displaying return bill
        print("==============================================")
        print("\t\tBill Details\t\t")
        print("\n==============================================")
        print("**********************************************")
        print("Name of the customer: ",name)
        print("Contact number of customer:",phone)
        print("Date Time of borrow: ",date_time)
        print("Items in rent are:",cos)
        print("Brand of items are:",brand)
        print("Total price is: $",p)
        print("Total amount received: $",received)
        print("Total amount to be received: $",total_due,)
        print("**********************************************")
  
        #creating txt file using costumer name and storing details of customer and costumes details as bill details
        with open("Rent-"+name+"-"+phone+".txt","w") as f:
                f.write("Name of the customer: "+name+"\n")
                f.write("Contact number of customer:"+phone+"\n")
                f.write("Date Time of borrow: "+date_time+"\n")
                f.write("Total price is: $"+p+"\n")
                f.write("Total amount received: $"+received+"\n")
                f.write("Total amount to be received: $"+total_due)
                f.write("\nItems in rent are:\n")

                count=1
                for i in range(len(costume_and_qty)):
                    num=str(count)
                    it=str(item_costume[i])
                    itb=str(item_brand[i])
                    caq=str(costume_and_qty[i])
                    n=str(num)
                    i=str(it)
                    ib=str(itb)
                    cq=str(caq)
                    f.write(n+".  ")
                    f.write(i)
                    f.write("  :"+ib)
                    f.write("  Quantity"+"-  "+cq+"\n")
                    count=count+1
                
        f.close
        costume_and_qty.clear()
        item_price.clear()
        item_brand.clear()
        item_costume.clear()

#function to update quantity in dictionary
def stock_update():
        f=open("stock.txt","w")
        for value in costume_dic.values():
                string = ",".join(value)
                f.write(string)
                f.write("\n")
        f.close()
        
