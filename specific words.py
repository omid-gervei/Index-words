# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:18:22 2024

@author: omidg
"""
qq = []
ind = []
indices = []
text = input()
q = text.split(' ')
for i in range(len(q)):
    if q[i][-1] == '.':
        q[i] = q[i][:-1] #elimination of '.'
        indices.append(i) #storing the position of words with '.'cuz we don want to keep the next word is index word
print(q)        
print(indices)

indices = [i+1 for i in indices]
#print(indices)

for i in range(1,len(q)-1):
    if q[i].istitle()==True:
        if i in indices:
            continue
        else:
            ind.append(i)
            qq.append(q[i])
ind = [i+1 for i in ind]            
#print(qq)
#print(ind)
if len(ind) == 0:
    print('None')
else:
    for i in range(len(ind)):
        print(str(ind[i])+':'+qq[i])
