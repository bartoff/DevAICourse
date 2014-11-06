__author__ = 'george'
#from existence01 import Existence01
#from existence02 import Existence02
#from existence03 import Existence03
from existence031 import Existence031

if __name__ == '__main__':
    #ex = Existence03()
    ex = Existence031()

    for i in range(0, 7):
        stepTrace = ex.step()
        print (i, stepTrace)#wasn't working
