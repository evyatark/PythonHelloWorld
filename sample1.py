import math 
import datetime
import os

SECONDS = 30


def getMyEnvVar():
    """
    This demonstrates how I retrieve some value from an Environment Variable.
    In Gitpod dashboard I defined that env var and supplied a value.
    The value is hidden from anyone using the code of this application.
    """
    val = os.environ.get('MY_SECRET_VAR')
    return int(val)


def doLengthyOperation1():
    value = getMyEnvVar()
    print(f'Hello World, started ...')
    my_range = range(SECONDS * value)
    for n in my_range:
        #print(n)
        x = n* math.sin(math.pi / (6))
        #if n%2000000==0:
        #    print(round(x, 4)) 
    print(f'Hello World, ... completed')


if __name__ == '__main__':
    startedAt = datetime.datetime.now()
    print('started at', startedAt)
    doLengthyOperation1()
    print('completed at', datetime.datetime.now())
    
