# Edmarck Sosa, Due by 9/24/24, a Python program that performs as a Tuffy Titan Contact List which contains a list of contacts that can be modified or deleted.

import contacts

def menu():
    print("\n*** TUFFY TITAN CONTACT MAIN MENU ***")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by last name")
    print("7. Exit program")

 
def main():
    # contacts_list = [["Richard","Stallman"],["Bill","Gates"]]
    contacts_list = {}
    # contacts_list = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
    # c = {7145551111: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']}
    while True:
        menu()
        
        choice = input("Enter menu choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                for id, names in contacts_list.items():
                    print(f"Phone: {id}, First Name: {names[0]}, Last Name: {names[1]}")
                
            elif choice == 2:
                #contact_list = contacts.add_contact(contacts_list, first_name = input("insert first name: "), last_name = input("insert last name: "))
                id = input("Enter phone number (ID): ")
        
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                result = contacts.add_contact(contacts_list, first_name=first_name, last_name=last_name, id=int(id))
                # if result == "error":
                #     print("Error: Contact already exists.")
                if result == "error":
                    print("error")        
                else:
                    print(f"Contact added: {result}")
                        
            elif choice == 3:
                ccontact_list = contacts.modify_contact(contacts_list, index= input("Index to update: "), first_name= "", last_name= "")
            
            elif choice == 4:
                contact_list = contacts.delete_contact(contacts_list, index=input())
                
            elif choice == 5:
                contact_list = contacts.sort_contacts(contacts_list, column=input()) 
                
            
            elif choice == 6:
                contact_list = contacts.sort_contacts(contacts_list, column=input()) 
                
                
            elif choice == 7:
                break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
            