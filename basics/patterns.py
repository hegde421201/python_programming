'''



largest = None

for i in [113,5,53,56,2,89,-1]:
    if largest is None or largest < i:
        largest = i
    print("Largest loop: ",largest)
print("Largest ",largest)

fruit = 'watermelon'

length = len(fruit)
print(length)

print(fruit[-2])
print(fruit[1])
print(fruit[0:5])
print(fruit[:])
print('melon' in fruit)

print(fruit.find('a'))

'''
from typing import List

a = [0] * 26
print(a)