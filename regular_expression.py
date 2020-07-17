import re

# string = 'shubham@example.com, shubham@abc.com, shubham@shubham, shubham.com'
# pattern = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'

# result = re.findall(pattern, string) 
# print(result)

result = re.fullmatch("Hello", "Hello World")
print(result)