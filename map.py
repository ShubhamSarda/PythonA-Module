# lst = [5, 10, 20, 25, 50]
# sq_lst = []

# def square(lst):
#     for item in lst:
#         sq_lst.append(item**2)

#     return sq_lst

# print(square(lst))

lst = [5, 10, 20, 25, 50]
print(list(map(lambda num: num ** 2, lst)))