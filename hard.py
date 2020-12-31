import main as x 
from time import sleep
from threading import *



class create(Thread):
    def run(self):
            x.create("abc",55,10)
            sleep(1)

class read(Thread):
    def run(self):
            x.read("abc")
            sleep(1)

class delete(Thread):
    def run(self):
            x.delete("abc")
            sleep(1)


t1= create() #creates abc
t2= create() #creates abc and returns error message
t3= read() #read abc
t4= delete() #delete abc
t5= read() #reads abc and returns error since its deleted 

t1.start() 
sleep(0.2)
t2.start()
sleep(0.1)
t3.start()
sleep(0.2)
t4.start()
sleep(0.2)
t5.start()
sleep(0.2)

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print("Bye")