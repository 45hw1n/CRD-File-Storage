import main as x 
from threading import Thread, Lock
_db_lock = Lock()

inp = input("Press r to read, c to create d to delete and q to quit : ")

while(inp!='q'):
    #Read
    if(inp=='r'):
        key_name = str(input("Enter Key Name : "))
        t1= Thread(target=(x.read),args=[key_name]) # Returns Key, Value & Timeout (Key:Value:Timeout)
        t1.start()
        t1.join()
    #Create
    elif(inp=='c'):
        key_name = input("Enter Key Name : ")
        value = int(input("Enter Value : "))
        time_out= int(input("Enter Expiry Time: ")) # If 0 it has infinite timeout
        t2= Thread(target=(x.create),args=(key_name,value, time_out))
        t2.start()
        t2.join()
    #Delete
    elif(inp=='d'):
        key_name = input("Enter Key Name : ") 
        t3= Thread(target=(x.delete),args=[key_name])
        t3.start()
        t3.join()
    else:
        print("Enter a valid input")

    inp = input("Press R to read, C to create D to delete and Q to quit : ")

print("Program quitted successfully")