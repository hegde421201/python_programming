'''
print("hello world!!")
print(4)
print(type("Hello world"))
print(type(4))
print(type(4.6))

'''

x = 44
print(x + 55)


def hegde():
    print("Welcome Hegde")

hegde()


#inp = input("What is your name?\n")
#print("Your name "+inp)

print(type(True))

x = 6
y = 6

if x < y:
    print(" x less than y")
elif x > y:
    print("x greater than y")
else:
    print("x and y are equal")

n = 7

while n > 0:
    print(n)
    n = n - 1

while True:
    line = input('> ')
    if line == 'done':
        break
    if line[0] == '#':
        continue
    print(line)

people = ['Putin','Bush','Gorbachev']
for president in people:
    print(president," Happy",7)

count = 0
for i in [24,6,7,45,89]:
    count = count + 2*i
print('Count: ',count)

