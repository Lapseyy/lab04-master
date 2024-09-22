# Edmarck Sosa, Due by 9/10/24, a Python program that performs as a Tuffy Titan Contact List which contains a list of contacts that can be modified or deleted.

# def print_list(contacts):
#     """Prints the list of names. Args: contact_list (_type_): _description_."""
#     print(f"{'Index':8}{'First Name':22}{'Last Name':22}")
#     for i in range(len(contacts)):
#         print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
# since the readme did not say to add the print list on contacts.py it will be in main

def add_contact(contact, first_name, last_name, id = None):
    """Adds contact to the list of names.  Args: add_contact (contacts): _description_."""
    contact = {}
    if id in contact:
        print("error")
    contact[id] = [first_name, last_name]
    return {id: contact[id]}
    
def modify_contact(contact, first_name, last_name, id = None):
    """Modifies the contact list. Args: modify_contact(contact_list) _description_."""
    contact = {}
    if id not in contact:
        print("error")
    contact[id] = [first_name, last_name]
    return {id: contact[id]}
        
def delete_contact(contact, index):
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

def find_contact(contacts, find):
    name = {}
    