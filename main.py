__author__ = 'george'
#from existence01 import Existence01
from existence02 import Existence02

if __name__ == '__main__':
    #ex = Existence01()
    ex = Existence02()

    for i in range(0, 7):
        stepTrace = ex.step()
        print "%d: %s" % (i, stepTrace)
