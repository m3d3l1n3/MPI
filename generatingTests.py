import random

def generatRandom(upper):
    l=[]
    for i in range(upper):
        l.append(random.randint(0,10000000))
    return l

def generateAscending(upper):
    l = []
    for i in range(upper):
        l.append(i)
    return l

def generateDescending(upper):
    l=[]
    for i in range(upper,1,-1):
        l.append(i)
    return l

