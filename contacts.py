# Edmarck Sosa, Due by 9/10/24, a Python program that performs as a Tuffy Titan Contact List which contains a list of contacts that can be modified or deleted.

def print_list(contacts):
    """Prints the list of names. Args: contact_list (_type_): _description_."""
    print(f"{'Index':8}{'First Name':22}{'Last Name':22}")
    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')

def add_contact(contacts, first_name, last_name):
    """Adds contact to the list of names.  Args: add_contact (contacts): _description_."""
    # first_name = firstName
    # last_name = lastName
    # lastName = last_name
    # firstName = first_name
    #cfirstName = input("Enter first name: ")
    # lastName = input("Enter last name: ")
    #contacts.append([[firstName], [lastName]])
    contacts.append([first_name, last_name])
    return contacts
    
def modify_contact(contacts, first_name, last_name, index):
    """Modifies the contact list. Args: modify_contact(contact_list) _description_."""
    # userIndex = input("List index number you want to modify: ")
    if str(index).isdigit():
        index = int(index)
        if index >= 0 and index < len(contacts):
            # first_name = input("Enter first name: ")
            # last_name = input("Enter last name: ")
            contacts[index] = [first_name, last_name]
            return True
    #     else: 
    #         print("Invalid index number.")
    # else:
    #     print("Invalid index number.")
    return False
        
def delete_contact(contacts, index):
    """Delete contacts in contacts. Args: delete_contacts (contacts): _description_"""
    
    # index = input("List index number to delete: ")
    if str(index).isdigit():
        index = int(index)
        if index >=0 and index < len(contacts):
            contacts.pop(index)
            
            return True
    # else:
    #     #print("Invalid index number.")
    #     return contacts
    return False
def sort_contacts(contacts, column):
    # column = input()
    if str(column).isdigit():
        column = int(column)
        # alphabetize = sorted(contacts, key = lambda x: x[1], reverse=False)
        if column == 0:
            contacts.sort(key = lambda x: x[0])
            #contacts.sort(key=lambda x: x[1])
            #return alphabetize
        else:
            # last_reverse = sorted(contacts, key = lambda x: x[1])
            # contacts.sort(key=lambda x: x[1])
            contacts.sort(key = lambda x: x[1])

            #return
        
        #sorted(contacts, key = lambda contacts: contacts[1] )
    
    # return contacts

# def multiple(n):
#     return lambda x: X + n
# multiple_2 = multiple(2) prints 20
# multiple_3 = multiple(3) prints 30

# def practice(self):
#     students = [["james", 34], ["adam", 21], ["Kyle", 18]]
#     sorted_students = sorted(students, key = lambda x: x[1])
#     students.sort(key=lambda x: x[1])
#     print(sorted_students)    
