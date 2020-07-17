# lst = [37, 38, 42, 40, 39, 45]
# ft_lst = []

# def greater(lst):
#     for item in lst:
#         if item > 39:
#             ft_lst.append(item)
#         else:
#             pass
    
#     return ft_lst

# print(greater(lst))

lst = [37, 38, 42, 40, 39, 45]
print(list(filter(lambda num: num > 39, lst)))