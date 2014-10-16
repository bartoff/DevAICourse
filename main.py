__author__ = 'george'
from existence01 import Existence01

if __name__ == '__main__':
    ex = Existence01()

    for i in range(0, 11):
        stepTrace = ex.step()
        print "%d: %s" % (i, stepTrace)
