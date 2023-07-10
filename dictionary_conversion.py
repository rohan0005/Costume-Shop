#creating a dictionary to store ID and costume details
costume_dic = {}
def costume_dictionary_conversion():
        print("-------------------------------------------------------------")
        print("ID \t Costume Name \t Costume Brand \t Price \t Quantity ")
        print("-------------------------------------------------------------")
        file =open("stock.txt","r")
        #read all the data from file
        costume_data = file.read()
        costume_data = costume_data.split("\n")
        count = 0

        #while loop is used to remove empty string in a list
        while("" in costume_data):
            costume_data.remove("")
        
        for i in range(len(costume_data)):
            count=count+1
            #displaying txt file with ID and spliting each
            costume_dic[count]=(costume_data[i].split(","))
        display()
        file.close()

#applying proper space        
def display():
    for key, value in costume_dic.items():
        print(key,end =("\t"))
        for i in value:
            print(i,end =("\t"))
        print("\n")
    print("-------------------------------------------------------------")



        
    
