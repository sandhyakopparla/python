import re,logging
logging.basicConfig(filename='error2.log',level=logging.ERROR)
def validation_of_books(book_title,author,price,distributor_name,publisher):
    val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",book_title)   
    val2=re.match("([a-z]+)([a-z]+)([a-z]+)$",author)
    val3=re.match("[0-9]{0,7}$",price)
    val4=re.match("([a-z]+)([a-z]+)([a-z]+)$",distributor_name)
    val5=re.match("([a-z]+)([a-z]+)([a-z]+)$",publisher)
    try:
        if val1 and val2 and val3 and val4 and val5:
            return True
        else:
            return False
    except:
        logging.error("Invalid validation kindly check it")
    else:
        logging.info("done!")