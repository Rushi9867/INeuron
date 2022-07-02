import logging as lg 
lg.basicConfig(filename='test3.log',level=lg.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')
try:
    with open('rest1.txt','r'):
        lg.info("Successfully it has read the file")
except Exception as e:
    lg.critical("This is a situation for us")
    lg.error(e)