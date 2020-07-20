from functools import wraps
import pandas as pd
import matplotlib.pyplot as plt

def prepost(*arg, **kwargs):
    def inner(function):
        @wraps(function)
        def wrapper(*a, **k):
            if 'url' in kwargs.keys():
                df = pd.read_csv(kwargs["url"])
                retval = function(*a, **k)
                df.hist()
                plt.show()
                print('done')
                return retval
        return wrapper
    return inner
      
    
@prepost(url='http://winterolympicsmedals.com/medals.csv')
def _f_protected():
    l1 = [ x for x in range(16)]
    list_1 = list(filter(lambda x : x > 5 ,l1))
    print(list_1)
    return list_1

_f_protected()


