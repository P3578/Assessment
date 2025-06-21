from datetime import datetime
def item(name,title,content):
    with open("my_file.txt","a") as file:
        file.write(str(datetime.now()))
        file.write(f"\nEnter Python E-Note Generator Name :{name}" + "\n")
        file.write(f"Enter Pyton E-Note Title : {title}" + "\n")
        file.write(f"Enter E-Note Content : {content} "+ "\n")
        file.write("-----------------------------------------------------------------------\n")
        
        print ("data saved into my_file.txt")