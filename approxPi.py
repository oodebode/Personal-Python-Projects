from math import sqrt
from random import uniform

def piFrac(n):

  oddNums = [1 + (2 * i) if i % 2 == 0 else -1 * (1 + 2 * i) for i in range(n)]
  oddNumDiv = [1 / i for i in oddNums]
  pi = 4 * sum(oddNumDiv)
  
  return pi


def piDots(n):

  pointsIn = 0
  
  for i in range(n):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    
    pointDis = sqrt((x ** 2) + (y ** 2))
    
    if pointDis <= 1:
      pointsIn += 1
    
  pi =  4 * (pointsIn / n)
  return pi


n = 10 ** int(input('Enter a Power of 10 to Begin Calculations: '))
print('  ')

def approxPi(n):

  while True:
    choice = input('Random Chance, Algebraic Approximation, or Both? Select 1, 2 or 3: ')
    print(' ')
    if choice == '1':
      result = piDots(n)
      print(result)
      break
      
    elif choice == '2':
      result = piFrac(n)
      print(result)
      break
      
    elif choice == '3':
      resultOne = piDots(n)
      resultTwo = piFrac(n)

      print(resultOne)
      print(' ')
      print(resultTwo)
      break
      
    else:
        print('Invalid Input, Try Again')


approxPi(n)
