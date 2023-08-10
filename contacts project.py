




def add():
    print("add")
    
def edit():
    print("edit")
    
def delete():
    print("edit")
    
def show():
    print("edit")
    
def search():
    print("search")
    




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
                 
    choice_function={'1':add, 2:edit, 3:delete, 4:show, 5:search}
    choice_function[choice]()
