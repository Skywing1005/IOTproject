
import bluetooth
import time

print "In/Out Board"

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
    
    
    
    result = bluetooth.lookup_name('04:b1:67:f5:71:78', timeout=2)
    if (result != None):
        print "Aditya: in"
    else:
        print "Aditya: out"

   result = bluetooth.lookup_name('64:a2:f9:80:6f:3c', timeout=5)
    if (result != None):
        print "Shubham: in"
    else:
        print "Shubham: out"
   result = bluetooth.lookup_name('94:n2:29:87:4f:9c', timeout=5)
    if (result != None):
        print "Satej: in"
    else:
        print "Satej: out"  
        

    time.sleep(30)


