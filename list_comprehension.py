# lst = [1, 2, 3, 4, 5]
# sq_lst = []

# for num in lst:
#     if num > 3 and num%5 == 0:
#         sq_lst.append(num ** 2)

# print(sq_lst)

lst = [1, 2, 3, 4, 5]
sq_lst = [num ** 2 for num in lst if num > 3 and num%5 == 0]

print(sq_lst)