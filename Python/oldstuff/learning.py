import random
import os
import time
import random
print("Hello world")



bob = str(random.randint(1,100))

print(bob)
print(type(bob))
bob2 = bob
for i in range(1,100):
    bob2 = bob2 + " " + str(random.randint(1,100))

print(bob2)

print("\n\n")

bob3 = bob2
for i in range(1,200):
    bob3 = bob3 + " " + str(random.randint(1,1000))

print(bob3)

print("\n\n")

bob4 = bob3
for i in range(1,400):
    bob4 = bob4 + " " + str(random.randint(1,10000))

print(bob4)

print("\n\n")

bob5 = bob4
for i in range(1,600):
    bob4 = bob4 + " " + str(random.randint(1,100000))

print(bob5)

time.sleep(random.randint(1,10))

os.system('cls' if os.name == 'nt' else 'clear')





