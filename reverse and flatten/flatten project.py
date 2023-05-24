
def flatten(x):
    if len(x) == 0:
        return x
    if isinstance(x[0], list):
        return flatten(x[0]) + flatten(x[1:])
    return x[:1] + flatten(x[1:])


input1= [[1, 2], [3, 4], [5, 6, 7]]
input2= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flatten(input1))
print(flatten(input2))