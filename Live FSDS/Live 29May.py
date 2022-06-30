import logging as lg 
lg.basicConfig(filename='test.log',level= lg.INFO)
lg.info("This is my very first code for logging")
lg.warning("this will try to load a warning message")
lg.error("This is a error message from system")
l = [1,2,3,4,5,6,7,8]
for i in l:
    if i == 2:
        lg.info(i)
        lg.warning("This is a warning for a user that they have found out 2 in list")

lg.shutdown()