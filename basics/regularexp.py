import re

s = "A man, a plan, a canal: Panama"
x = re.findall('[a-zA-Z0-9]', s)
delimiter = ""
x = delimiter.join(x)
#print(x)

lists = list(s)
#print(lists)

for index,chars in enumerate(lists):
    print(index,chars)

z = '......a.....'
k = "".join(reversed(z))

obj = enumerate(lists)

#print(z==k,z,k)