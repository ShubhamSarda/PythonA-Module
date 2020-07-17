def recursion(count):

    if count == 500:
        return 0
    else:
        print("Hello World", count)
        recursion(count + 1)

count = 0
recursion(count)