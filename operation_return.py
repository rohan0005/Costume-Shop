from dictionary_conversion import *
from operation_rent import *
from datetime import *
cos_name=[]
#adding rented items in a list!!!#
rented_costumes=[]

#creating empty list to store values
returning_costumes=[]
num_quantity=[]
date_time_list=[]
due_amount_list=[]
grand_total=[]

#Function
def costume_return():
        #This function will ask the user to input name and contact
        costume_dictionary_conversion()
        name = input("\nEnter your full name:")
        cus_name=name
        number = input("\nEnter your contact number:")
        c_number= number
        read_rent_file(cus_name,c_number)
        return cus_name
        return c_number

def read_rent_file(cus_name,c_number):
        #This function is used to read the rented file
        try:                
                with open("Rent-"+cus_name+"-"+c_number+".txt") as f:
                        line=f.readlines()
                        date_time_list.append(str(line[2].strip().strip("Date Time of borrow: ")))
                        due_amount_list.append(float(line[5].strip().strip("Total amount to be received: $")))
                        print("Items in rent are:")
                        print("------------------------------------------------")
                        for i in range(7,len(line)):
                                print(line[i])
                                rented_costumes.append(line[i].split("  "))
                        print("------------------------------------------------")
                        
                f.close
                print("")
                conform_return(cus_name,c_number)

        except:
                print("\nNo rent information found with this details.")


def conform_return(cus_name,c_number):
        #this function is used to display successful message
        print("Do you want to return those costumes?")
        conform=input("Enter any value to return: ")
        print("")
        print("******************************************")
        print("          Successfully returned.          ")
        print("   Thank you for returning the costume.   ")
        print("******************************************\n")
        return_costume_process(cus_name,c_number)
                


        

def return_costume_process(cus_name,c_number):    
        #loop will run till the length of list
        for i in range(len(rented_costumes)):
                for j in costume_dic:
                        cstm=costume_dic[j]
                        cos_name=rented_costumes[i]
                        if cos_name[1]==cstm[0]:
                                num_quantity.append(str(cos_name[4].strip().strip("\n")))
                                num_qty=int(num_quantity[i])
                                qty_rent=costume_dic[j]
                                up_qty_rtn= int(qty_rent[3])+num_qty
                                qty_rent[3]=str(up_qty_rtn)
                                stock_update_return()     
        print(costume_dic)
        print("")
        costume_dictionary_conversion()
        any_key=input("\nEnter any key to invoice return bill:")
        print("")
        return_bill(cus_name,c_number)


def stock_update_return():
        #to update quantity in dictionary
        f=open("stock.txt","w")
        for value in costume_dic.values():
                string = ",".join(value)
                f.write(string)
                f.write("\n")
        f.close()


def return_bill(cus_name,c_number):
            #function is used to generate return bill 

            #assigning variables
            name=cus_name
            phone=c_number
            due_amount=str(due_amount_list[0])
            grand_total.append(float((due_amount)))
            dt=datetime.now()
            year=str(dt.year)
            month=str(dt.month)
            day=str(dt.day)
            hour=str(dt.hour)
            minute=str(dt.minute)
            second=str(dt.second)
            date_time=year+"/"+month+"/"+day+" "+hour+":"+minute+":"+second
            rnt_date = str(date_time_list[0])
            rtn_date = str(date_time)

            # convert string to datetime
            d_rent= datetime.strptime(rnt_date, "%Y/%m/%d %H:%M:%S")
            d_return = datetime.strptime(rtn_date, "%Y/%m/%d %H:%M:%S")

            # difference between datetime in timedelta
            delta = d_return - d_rent
            late=int(delta.days)
            if int(late) > 5:
                    late_days_fine=int(late)-5
            else:
                    late_days_fine= 0

            fine=str(float(late_days_fine)*5)

            grand_total.append(float((fine)))

            total=str(sum(grand_total))


            for i in range(len(rented_costumes)):
                    costm_nm=rented_costumes[i]
                    rtn_cstm=True
                    #while rtn_cstm == True:
                    returning_costumes.append(str(costm_nm[1]))
                            #rtn_cstm=False

            rtn_costumes=str(returning_costumes)
            
            #Displaying return bill 
            print("========================================================")
            print("\t\tBill Details\t\t")
            print("========================================================")
            print("********************************************************")
            print("Name of the customer: "+name)
            print("Contact number of customer:"+phone)
            print("Date Time of return: "+date_time)
            print("Items that are returned :"+rtn_costumes)
            print("Total amount to be received: $"+due_amount)
            print("Total fine: $"+fine)
            print("Grand Total: $"+total)
            print("********************************************************")
            
           
            #creating txt file using costumer name and storing details of customer and costumes details as bill details
            with open("Return-"+name+"-"+phone+".txt","w") as f:
                f.write("Name of the customer: "+name+"\n")
                f.write("Contact number of customer:"+phone+"\n")
                f.write("Date Time of rent: "+rnt_date+"\n")
                f.write("Date Time of return: "+date_time+"\n")
                f.write("Items that are returned :"+rtn_costumes+"\n")
                f.write("Total fine: $"+fine+"\n")
                f.write("Total price is: $"+total+"\n")
            f.close
