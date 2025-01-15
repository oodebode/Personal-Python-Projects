import random

def determineSex():

  male = 0
  female = 0

  for i in range(100):
    
    mother = random.randint(1,1)
    father = random.randint(0,1)
    
    if mother == 1 and father == 1:
      female += 1
    if (mother == 1 and father == 0):
      male += 1
 
  return male, female
      
def main():
  
  male, female = determineSex()
  
  print(f"Males: {male}, Female: {female}")

main()
