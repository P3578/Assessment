import logging
from datetime import datetime
def deco(func):
    def wrap(*args):
        print ((str(datetime.now())))
        func(*args)
        print ("data saved into app.log")
    return wrap

@ deco
def item(name,title,content):
    logging.basicConfig(filename='app.log', level=logging.DEBUG, filemode='a')
    logging.info(str(datetime.now()))
    logging.info(f"\nEnter Python E-Note Generator Name :{name}" + "\n")
    logging.info(f"Enter Pyton E-Note Title : {title}" + "\n")
    logging.info(f"Enter E-Note Content : {content} "+ "\n")
    logging.info("-----------------------------------------------------------------------\n")
        
    