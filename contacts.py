# Edmarck Sosa, Due by 9/10/24, a Python program that performs as a Tuffy Titan Contact List which contains a list of contacts that can be modified or deleted.

# def print_list(contacts):
#     """Prints the list of names. Args: contact_list (_type_): _description_."""
#     print(f"{'Index':8}{'First Name':22}{'Last Name':22}")
#     for i in range(len(contacts)):
#         print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
# since the readme did not say to add the print list on contacts.py it will be in main

def add_contact(contact, first_name, last_name, id = None):
    """Adds contact to the list of names.  Args: add_contact (contacts): _description_."""
    # contact = {}
    if id in contact:
        return "error"
    contact[id] = [first_name, last_name]
    return {id: contact[id]}
    
def modify_contact(contact, first_name, last_name, id = None):
    """Modifies the contact list. Args: modify_contact(contact_list) _description_."""
    # contact = {}
    if id not in contact:
        return("error")
    contact[id] = [first_name, last_name]
    return {id: contact[id]}
        
def delete_contact(contact, id = None):
    """Delete contacts in contacts. Args: delete_contacts (contacts): _description_"""
    # contact = {}
    if id not in contact:
        print("error")
    delete = {id: contact.pop(id)}
    return delete

def sort_contacts(contact):
    """ Sort contacts in contacts. Args: delete_contacts (contacts): _description_"""
    sorted_contacts = dict(sorted(contact.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower())))
    return sorted_contacts

def find_contact(contact, find=None):
    """
    Finds contacts by phone number or name substring.
    """
    contact = {}
    
    if find.isdigit() and int(find) in contact:
        contact[int(find)] = contact[int(find)]
    
    for id, (first_name, last_name) in contact.items():
        if find.lower() in first_name.lower() or find.lower() in last_name.lower():
            contact[id] = [first_name, last_name]
    

    sorted_contacts = dict(sorted(contact.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower())))
    return sorted_contacts
