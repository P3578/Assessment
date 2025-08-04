import module2 as file
print ("\t\t\tWelcome to Python E - Note")
print ("\n")
flag = True
while flag:
    print ("\t\t\tPress 1 for generate Note")
    print ("\t\t\tpress 2 for view Note")
    print ("\t\t\tpress 4 for exit")
    choice =  int(input("\nEnter your choice : "))

    match choice:
        case 1:
            name = (input("Enter Python E-Note Generator Name : "))
            title = (input("Enter Pyton E-Note Title : "))
            content = (input("Enter E-Note Content : "))
            file.item(name,title,content)
            print ("\n")
        case 2:
            with open("app.log","r") as file:
                data = file.read()
                print (data)
            print ("\n")
        case 4:
            flag == False
            break
