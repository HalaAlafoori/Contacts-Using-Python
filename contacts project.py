class Contact:
    def __init__(self, name, email, *phone_numbers):
        self.name = name
       
        self.email = email
        self.phone_numbers = phone_numbers #a list 




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
    
def show():
    print("edit")
    
def search():
    print("search")
    




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
