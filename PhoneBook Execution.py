from PhoneBookClass import Entry
from PhoneBookClass import PhoneBook

Phonebook = PhoneBook()

print("Welcome")



while True:
    print("What would you like to do whith your contact list?")
    print("Enter 1 to add a contact, 2 to delete one, 3 to look up a contact, 4 to update an existing contact or 5 to see your contact list")
    user_operation = input()
    if user_operation == "1":
        print("Enter a name for the contact")
        name = input()
        print("Enter a phone number for the contact")
        phonenumber = input()
        Phonebook.insert(name, phonenumber)
        Phonebook.sort
    elif user_operation == "2":
        print("Enter the name of the contact you would like to delete")
        name = input()
        Phonebook.delete(name)
    elif user_operation == "3":
        print("Enter 1 to search by name or 2 to search by number")
        searchbymethod = input()
        if searchbymethod == "1":
            print("Enter the name of the contact you are searching for")
            name = input()
            print("The phone number belonging to inputed name is")
            print(Phonebook.searchbyname(name))
        elif searchbymethod == "2":
            print("Enter phone number of the contact you are searching for")
            phonenumber = input()
            print("The owner of this phone number is")
            print(Phonebook.searchbynumber(phonenumber))
        else:
            print("invalid input you are now being returned to the main menu")
    elif user_operation == "4":
        print("Enter 1 to update a contacts name or 2 to update a contacts number")
        itemtobeupdated = input()
        if itemtobeupdated == "1":
            print("Please enter the current name tied to the contact you want to update")
            oldname = input()
            print("Please enter the new name for the contact")            
            newname = input()
            Phonebook.updatename(oldname, newname)
        elif itemtobeupdated == "2":
            print("Please enter the current number tied to the contact you want to update")
            oldname = input()
            print("Please enter the new number for the contact")            
            newnumber = input()
            Phonebook.updatephonenumber(oldnumber, newnumber)
        else:
            print("invalid input you are now being returned to the main menu")
    elif user_operation == "5":
        Phonebook.print()
    else:
        print("invalid input")