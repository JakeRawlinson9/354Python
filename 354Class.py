StNumber = 15010432
ArNumbers = [1, 5, 0, 1, 0, 4, 3, 2]
primes = []
print("0. The student number is: {}".format(StNumber))

for num in ArNumbers:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)

numPrimes = len(primes)
print ("1. The number of prime numbers in this student number is: {}".format(numPrimes))

import random
for x in range(1):
  rand = random.randint(25,51)

print ("2. The random number is: {}".format(rand))

import math
numStrings = math.floor(rand/numPrimes)
intStrings = int(numStrings)
print ("3. The number of strings to be generated is: {}".format(intStrings))

import string
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

strings =[]
for i in range (intStrings):
    if ((i+1) % 2 != 0):
        strings.append(randomString(5))
    else:
        strings.append(randomString(7))

print ("4. List of Strings:")
print ("********************")

x = 1
for word in strings:
    print(str(x)+". "+word)
    x +=1

print ("********************")

def numLetters(word):
    vowels=0
    for i in word:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
    