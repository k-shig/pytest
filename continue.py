'''
Created on 2017/12/17

@author: kshig
'''
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
    #else:
        #print("Found a number", num)
        continue
    print("Found a number", num)