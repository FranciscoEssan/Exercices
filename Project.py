agenda = {}

#This function adds a new contact to the agenda
def addContact():
    name = input("Contact's name: ")   
    #Check if the contact exist before adding the information
    # If the contact exists the program shows the current information 
    if name in agenda:
        print(f"This contact already exist and the phone number is: {agenda[name]}")
    #If the contact does not exist the program save the new information
    else:
        number = input("Phone number: ")
        agenda[name]=number 

#This function updates the contact information
def modifyContact():
    name = input("Contact to update: ")
    #Check if the contact exist
    if name in agenda:
        #Asks for confirmation before updating the information
        option = input("Do you want to update the information? (Y/N) ")
        #If user confirms the update the program updates the information
        if option.lower() == "y":
            number = input("New phone number:")
            agenda[name]=number
            print("Information updated...")
    #If the contact does not exist shows a message
    else:
        print(f"The contact {name} does not exist")


#This funtion is to look for a contact
def searchContact():
    #Contact to search 
    contact = input("Contact's name: ")    
    #Check if the contact exists and shows the contact's information
    if contact in agenda:
        print(f"{contact}'s phone number is {agenda[contact]}")
    #if the contact does not exist shows a message
    else:
        print(f"The contact {contact} does not exist")


#This funtion is to delete a contact
def deleteContact():
    #Contact to delete
    name = input("Contact to delete: ")   
    #Check if the contact exists
    if name in agenda:
        #Asks for confirmation before deleting the contact
        option = input(f"Do you want to delete {name} from your agenda? (Y/N)")
        if option.lower() == "y":
            del agenda[name]
            print("Contact deleted...")
    ##if the contact does not exist shows a message
    else:
        print(f"The contact {name} does not exist")

#This funtion is to show all the agenda
def showAgenda():
    print("*************** Contacts list ***************")
    #Loop to show the information in a friendly way
    for name, number  in agenda.items():
        print(f"{name} -> {number}")
    #Shows a message if the agenda is empty
    if len(agenda) == 0:
        print(f"The agenda is empty!")


#Function to show a menu and choose an option
def menu():  
    
    #Loop to show and choose bettwen the options available  
    while True:
        #Show the options available
        print("\n1. Add \n2. Update \n3. Search \n4. Delete \n5. Show contacts \n6. Exit")
        #Read the option selected for the user and calls the correct function
        option = int(input("\nChoose an option: "))
        #Adds a contact
        if option == 1:
            addContact()
        #Updates a contact information
        elif option == 2:
            modifyContact()
        #Search a contact
        elif option == 3:
            searchContact()
        #Delete a contact
        elif option == 4:
            deleteContact()
        #Shows the agenda information
        elif option == 5:
            showAgenda()
        #Break the loop to exit
        elif option == 6:
            break
        #Shows a message if the user selects an incorrect option
        else:
            print("\nWrong option, try again. ")

menu()
