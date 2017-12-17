'''
Created on 2017/12/17

@author: kshig
'''
words = ["cat", "dog", "panda"]
for w in words:
    print(w, len(w))
    
for w in words[:]:
    if len(w) > 4:
        words.insert(0, w)

print(words)        