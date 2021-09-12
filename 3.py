i=0
def func(*args):
    for x in args:
        global i
        i+=1
        print(i,x)
    return 0
print(func(1000,50,80,55, "cdl,"))