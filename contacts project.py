from rich.console import Console
from rich.table import Table

class Contact:
    def __init__(self, name, email, *phone_numbers):
        self.name = name
       
        self.email = email
        self.phone_numbers = phone_numbers #a list 
        
    def return_list(self):
        print(self.phone_numbers)
        phone_numbers_string=''
        for phone in self.phone_numbers[0] :
            phone_numbers_string= phone_numbers_string+f'{phone}\n'
        return [self.name, self.email, phone_numbers_string]




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
    print("edit")
    
def delete():
    print("edit")

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

    
     
    
def search(): 
  
   table = Table(title="Search Result")
   rows=[]
   seacrh_by=int(input(
"To search by name enter 1 \n\
To search by email enter 2\n\
"))
   value=input("Enter value: \n")
   if seacrh_by == 1:   
       for contact in all_contacts:
           if value in contact.name :
               
               rows.append(contact.return_list())
   else:      
       for contact in all_contacts:
           if value in contact.email :
               
               rows.append(contact.return_list())
   
   print_table(table, rows)
        
       
    
    




run=True
#creating the list of objects 
all_contacts=[] #empty at first
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
