lst = [5, 10, 15, 20, 25]
x = 0

def sum(lst):
    for num in lst:
        x+=num
    
    return x

print(sum(lst))

# from functools import reduce

# lst = [5, 10, 15, 20, 25]
# print(reduce(lambda x, y: x + y , lst))
