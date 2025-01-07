record = [[0, 0] for i in range(8)]


# list comprehension - {} makes a set
# alis-ing
def indexOf(sub):
  subs = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']
  for i in range(len(subs)):
    if subs[i] == sub:
      return i
  return -1


# record[indexOf('HHH')][0]+=1


def prediction(last3):
  if indexOf(last3) == -1:  #sub DNE
    from random import choice
    return choice(['H', 'T'])
  if record[indexOf(last3)][0] > record[indexOf(last3)][1]:
    return 'H'
  if record[indexOf(last3)][0] < record[indexOf(last3)][1]:
    return 'T'
  else:
    from random import choice
    return choice(['H', 'T'])

  # look up last substring in list and check preference
  # return preference or rand


def mindReader():
  inp = ''
  winsComp = 0
  winsUser = 0

  while (winsComp < 25 and winsUser < 25):
    # guess
    last3 = inp[-3:]
    pred = prediction(last3)

    print('Computer has made a prediction')

    # user input

    letter = input('H or T?')
    
    while True:
      if letter == 'H' or letter == 'T':
        inp += letter
        break
      else:
        print('Invalid input')
        letter = input('H or T?')
      
     

    # update results

    if pred == letter:
      print('Computer Wins')
      winsComp += 1
      print('Wins User = ', winsUser)
      print('Wins Computer = ', winsComp)
      print(' ')

    else:
      print('You Win')
      winsUser += 1
      print('Wins User = ', winsUser)
      print('Wins Computer = ', winsComp)
      print(' ')

  last3 = inp[-4:-1]
  last1 = inp[-1:]

  if len(inp) >= 3:
    if last1 == 'H':
      record[indexOf(last3)][0] += 1
    else:
      record[indexOf(last3)][1] += 1

  print('Wins User = ', winsUser)
  print('Wins Computer = ', winsComp)


# 1. let user know the computer has made a prediction
# 2. get user input, H or T (update inp)
# 3. inform them who won (store prediction, use to determine winner)
# 4. update wins

mindReader()
