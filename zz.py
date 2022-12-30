import pandas as pd 

a = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
c = pd.DataFrame({'a':[7,8,9], 'b':[0,0,0]})
print(a)
print(c)
a = a.merge(c, how='outer')
print(a)

