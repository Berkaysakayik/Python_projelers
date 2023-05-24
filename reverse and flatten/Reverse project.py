L1=[]

def revers(y):
    for o in reversed(y):
        L1.append(o)

    return L1



input1= [[1, 2], [3, 4], [5, 6, 7]]
input2= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(revers(input1))
print(revers(input2))