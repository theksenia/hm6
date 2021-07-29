import random
l= []
for i in range(5):
    l.append(random.randint(0,105))
print(l)
def listsum(l):
    s = 0
    for i in l:
       s = s + i
    return s

print(listsum(l))