def check(func):
    def inner(a, b):
        if b == 0:
            return "Can't divide by 0"
        elif b > a:
            return b/a
            
        return func(a, b)
    return inner

@check
def div(a, b):
    return a/b

print(div(10, 0))