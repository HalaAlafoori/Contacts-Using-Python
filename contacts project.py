from os import system
from rich.console import Console
from rich.table import Table

class Contact:
    def __init__(self, name, email, *phone_numbers):
        self.name = name
       
        self.email = email
        self.phone_numbers = phone_numbers #a tuple 
        #print(type(self.phone_numbers))
        
    def return_list(self):
        #print(self.phone_numbers)
        phone_numbers_string=''
        for phone in self.phone_numbers[0] :
            phone_numbers_string= phone_numbers_string+f'{phone}\n'
        return [self.name, self.email, phone_numbers_string]

#creating the list of objects 
all_contacts=[] #empty at first



def add():
     
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
    
    
    print(all_contacts[0].name)
    
def edit():
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
           
       
       
   
   
 
 

def print_table(table, rows):
    columns = ["Name", "Email", "Phone Numbers"]
    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)
    
    
    
def show():
    

    table = Table(title="My Contacts")
    rows =[]
    for contact in all_contacts:
        rows.append(contact.return_list())
   
    print_table(table, rows)

    
def find(seacrh_by, value):
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
  
   table = Table(title="Search Result")
  
   seacrh_by=int(input(
"To search by name enter 1 \n\
To search by email enter 2\n\
"))
   value=input("Enter value: \n")
   rows=find(seacrh_by, value)
   format_rows=foramt_rows(rows)

   print_table(table, format_rows)

def Diff(all_contacts, deleted_contacts):
    new_all_contacts = [contact for contact in all_contacts if contact not in deleted_contacts ]
    return  new_all_contacts
   
def delete():
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
   
       
       
   
# main

  
run=True

while run:
   
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
