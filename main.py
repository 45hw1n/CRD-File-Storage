import threading 
from threading import Thread, Lock
_db_lock = Lock()
import time

data={} #'data' is the dictionary in which we store data

#Create operation 
def create(key,value,time_out=0):
    if key in data:
        print(f"ERROR: this {key} key already exists") #ERROR message 1 if key exist
    else:
        if(key.isalpha()):
            if len(data)<(1024*1020*1024) and value<=(16*1024*1024): #file size less than 1GB and Json object value less than 16KB 
                if time_out==0:
                    l=[value,time_out]
                else:
                    l=[value,time.time()+time_out,time_out]
                if len(key)<=32: #input key capped at 32chars
                    data[key]=l
                print(f"Key {key} successfully created")
            else: 
                print("ERROR: Memory limit exceeded")#ERROR message 2 if memory limit exceed
        else:
            print("ERROR: Invalid key")#ERROR message 3 if invalid key

#Read operation
def read(key):
    if key not in data:
        print("ERROR: Key does not exist in database") #ERROR message 4 if key doesn't exist
    else:
        a=data[key]
        if a[1]!=0:
            if time.time()<a[1]: #comparing the present time with expiry time
                string =str(key)+":"+str(a[0]) + ":" + str(a[2]) #Return value in JSON 
                print(string)
            else:
                print("ERROR: time-to-live of",key,"has expired") #ERROR message 5 if key expired
        else:
            string=str(key)+":"+str(a[0])
            print(string)

#Delete operation
def delete(key):
    if key not in data:
        print("ERROR: Key does not exist in database") #ERROR message 6  if key doesn't exist
    else:
        a=data[key]
        if a[1]!=0:
            if time.time()<a[1]: #comparing the current time with expiry time
                del data[key]
                print("key is successfully deleted")
            else:
                print("Alert: Key ",key,"has been expired") #if key expired
                confirm = input(f"Are you sure, want to delete this key : {key} ? y or n : ")
                if(confirm=='y'):
                    del data[key]
                    print("Success: Key is successfully deleted")
        else:
            del data[key]
            print(f"key {key} is successfully deleted")