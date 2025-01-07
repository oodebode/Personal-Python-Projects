x = int(input('Enter X Value: '))
y = int(input('Enter Y Value: '))

def twoPosInt(x, y):

  # level 7 - evaluates for floats and strings
  if type(x) != int:
    print('ERROR: Enter Integer')
    while True:  
      try:
        x = int(input('Enter X'))
        break
      except ValueError:
        print('ERROR: Enter Integer')
  if type(y) != int:
    print('ERROR: Enter Integer')
    while True:  
      try:
        y = int(input('Enter Y'))
        break
      except ValueError:
        print('ERROR: Enter Integer')

    # level 6 - evaluates for zero
  if x <= 0 or y <= 0:
    print('ERROR: Enter Integer Greater Than 0')
    while x <= 0 or y <= 0:
      if x <= 0:
        x = int(input('Enter New X Integer:'))
      if y <= 0:
        y = int(input('Enter New Y Integer:'))

  # level 0
  sum = x + y
  diff = x - y if x > y else y - x
  prod = x * y
  quot = x / y if x > y else y / x

  print(sum)
  print(diff)
  print(prod)
  print(quot)

  # level 1
  min = x if x < y else y
  max = x if x > y else y
  rng = diff
  avg = sum / 2

  print(min)
  print(max)
  print(rng)
  print(avg)

  # level 2
  remainder = divmod(x, y) if x > y else divmod(y, x)
  print(remainder)

  # level 3
  while True:
    if input('Repeat Integer Operations? (1 for yes):') == '1':
      print(sum)
      print(diff)
      print(prod)
      print(quot)
      print(min)
      print(max)
      print(rng)
      print(avg)
      print(remainder)

    else:
      break

  # level 4
  for i in [x, y]:
    print('*' * i)
    print(' ' * i)  #just an assignment break

  # copy of Jessica's solution
  space = ' '
  print('*' * x)
  for j in range(0, y - 2):
    print('*' + space * (x - 2) + '*')

  print('*' * x)
  print(' ')

  # level 5
  for i in range(x):
    print('*' * y)


twoPosInt(x, y)
