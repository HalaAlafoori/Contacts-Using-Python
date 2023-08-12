import json

# import call method from subprocess module
from subprocess import call
import os
from rich.console import Console
from rich.table import Table

class Contact:
    def __init__(self, name, email, *phone_numbers):
        self.name = name
       
        self.email = email
        self.phone_numbers = phone_numbers #a tuple 
        #print(type(self.phone_numbers))
        
    def return_list(self):
        
        phone_numbers_string=''
        for phone in self.phone_numbers[0] :
            phone_numbers_string= phone_numbers_string+f'{phone}\n'
        return [self.name, self.email, phone_numbers_string]
    
    def return_dict(self):
      
        return {'name': self.name, 'email': self.email, 'phone_numbers': self.phone_numbers}
   

   
def return_objs(contact_dict):
     
     return  Contact(contact_dict['name'], contact_dict['email'], contact_dict['phone_numbers'])
            

#creating the list of objects 
all_contacts=[] #empty at first

def clear_screen():
    os.system('cls')
    
       
def save_changes():
   all_contacts_list=[]
   for contact in all_contacts:
       all_contacts_list.append(contact.return_dict())
       
   filename = 'contacts_info.json'
   with open(filename, 'w') as f:
       json.dump( all_contacts_list, f)      
       
def load_data():
   global all_contacts 
   filename = 'contacts_info.json'
   with open(filename) as f:#send the loaded input to the converter function and then assign it to the global var
       json_list=json.load(f)
       print(json_list)
       for contact_dict in json_list:
           # pass
           all_contacts.append(return_objs(contact_dict))
       
       
       

def add():
   
    clear_screen()
    name=input("Enter name: \n")
    email=input("Enter email: \n")
    phone_numbers=[]
    
    while True:
        phone_number=input("Enter phone number: \n")
        phone_numbers.append(phone_number)
        answer=input("Is there another phone number? (Y/N) \n")
        if answer == 'N' or answer=='n':
            break
        
    all_contacts.append(Contact(name, email, phone_numbers))
    
    
    save_changes()
    
def edit():
   clear_screen()
   table = Table(title="Search Result")
   seacrh_by=int(input(
"To search by name enter 1 \n\
To search by email enter 2\n\
"))
   value=input("Enter value: \n")
   rows=find(seacrh_by, value)
   format_rows=foramt_rows(rows)

   print_table(table, format_rows)
   
   while True:
       edit_by=int(input(
    "To edit name enter 1 \n\
    To edit email enter 2 \n\
    To edit phone numbers enter 3 \n" ))
    
      
       if edit_by ==1:
           value=input("Enter new name: ")
           rows[0].name=value
           
           
       elif edit_by ==2:
           value=input("Enter new email: ")
           rows[0].email=value
          
       else: #error
           
           # rows[0].phone_numbers.clear() #delete old number
           new_numbers=[]
           while True:
                value=input("Enter new phone number: ")
                
                new_numbers.append(value)
                #print(new_numbers)
                answer=input("Is there another phone number? (Y/N) \n")
                if answer == 'N' or answer=='n':
                    break
           rows[0].phone_numbers=tuple(new_numbers)
           #sprint(rows[0].phone_numbers)
                
       answer=input("Do you want to edit another value?") 
       if answer == 'N' or answer=='n':
           break
   save_changes()
           
       
       
   
   
 
 

def print_table(table, rows):
    clear_screen()
    columns = ["Name", "Email", "Phone Numbers"]
    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)
    
    
    
def show():
    clear_screen()
    

    table = Table(title="My Contacts")
    rows =[]
    for contact in all_contacts:
        rows.append(contact.return_list())
   
    print_table(table, rows)
    input('press enter key to go back')

    
def find(seacrh_by, value):
   clear_screen()
   rows=[]
   if seacrh_by == 1:   
       for contact in all_contacts:
           if value in contact.name :
               
               rows.append(contact)
   else:      
       for contact in all_contacts:
           if value in contact.email :
               
               rows.append(contact)
  
               
   return rows
   
def foramt_rows(rows):
   format_rows=[]
   for row in rows:
       format_rows.append(row.return_list())
   return format_rows
        
def search(): 
   clear_screen()
  
   table = Table(title="Search Result")
  
   seacrh_by=int(input(
"To search by name enter 1 \n\
To search by email enter 2\n\
"))
   value=input("Enter value: \n")
   rows=find(seacrh_by, value)
   format_rows=foramt_rows(rows)

   print_table(table, format_rows)
   input('press enter key to go back')

def Diff(all_contacts, deleted_contacts):
    new_all_contacts = [contact for contact in all_contacts if contact not in deleted_contacts ]
    return  new_all_contacts
   
def delete():
   clear_screen()
   table = Table(title="Search Result")
  
   seacrh_by=int(input(
"To delete by name enter 1 \n\
To delete by email enter 2\n\
"))
   value=input("Enter value: \n")
   rows=find(seacrh_by, value)
   format_rows=foramt_rows(rows)
  
   print_table(table, format_rows)
   confirm=input("Do you want to delete this/ these contacts? (Y/N)/n")
   if confirm == 'N' or confirm=='n':
       pass
   elif confirm == 'Y' or confirm=='y':#delete
       global all_contacts
       all_contacts=Diff(all_contacts, rows) 
   save_changes()
   

# main

load_data()
run=True

while run:
   
    clear_screen()
    choice=input(
"To add a new contact enter 1 \n\
To edit a contact enter 2\n\
To delete a contact enter 3\n\
To show all contacts enter 4\n\
To search enter 5\n\
To exit enter 6\n\
")
                 
    choice_function={'1':add, '2':edit, '3':delete, '4':show, '5':search}
    choice_function[choice]()
