'''
Created on 2017/12/17

@author: kshig
'''

a, b = 0, 1
while b < 1000:
    print(b, end=' ')
    a, b = b, a + b