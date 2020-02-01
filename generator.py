#tjg!#

import time
start = time.time()
class Generator:

    divident = 2147483647
    x = 65
    y = 8921
    count = 0
    factorA = 16807
    factorB = 48271
    
    def genA():

        Generator.x = (Generator.x * Generator.factorA) % Generator.divident
        yield bin(Generator.x).replace('0b', "")[-16::]

    def genB():

        Generator.y = (Generator.y * Generator.factorB) % Generator.divident
        yield bin(Generator.y).replace('0b', "")[-16::]

    def Compare(A, B):
        if(A==B):
            Generator.count = Generator.count+1

for i in range(40000000):
    Generator.Compare(next(Generator.genA()) , next(Generator.genB()))

print("Count:", Generator.count)
end = time.time()
print("Time elapsed: ", int(end-start), " Seconds")

