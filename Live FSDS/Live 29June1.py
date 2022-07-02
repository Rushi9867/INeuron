import logging as lg 
lg.basicConfig(filename='test2.log',level=lg.DEBUG,format='%(name)s %(levelname)s %(asctime)s %(message)s')
lg.info("This is my log with timestamp")
def divide(a,b):
    try:
        lg.info("The number entered by user is %s and %s",a,b)
        div = a/b 
        lg.info("We have completed a division operation")
        lg.info("Result of code is %s",div)
        return div
    except Exception as e:
        lg.exception((e))

print((divide(3,8)))