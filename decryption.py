from math import sqrt

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'

def onlyLower(str):
  lowerStr = ''

  for character in str:
    if character in lower:
      lowerStr += character
    if character in upper:
      lowerStr += character.lower()

  return lowerStr


print(onlyLower('Does This Work for Everyone'))
print(' ')


def encrypt(lowerStr, key):

  encryptedStr = ''

  for character in lowerStr:
    if character in lower:
      alphaIdx = lower.find(character)
      cypherIdx = (alphaIdx + key) % 26
      encryptedStr += lower[cypherIdx]
  return encryptedStr


print(encrypt('mystery', 5))
print(' ')

def letterFrequencies(str):
  frequencies = [0.0 for i in range(26)]
  characterMax = 0

  for character in str:
    characterMax += 1

    if character in lower:
      alphaIdx = lower.find(character)
      frequencies[alphaIdx] += 1

  for i in range(26):
    frequencies[i] = round((frequencies[i] / float(characterMax)), 4)

  return frequencies

print(letterFrequencies('happy'))
print(' ')

def textFileFrequencies():
  frequencies = [0.0 for i in range(26)]
  characterMax = 0

  with open('paper.txt', 'r') as file:
    str = file.read()
    str = onlyLower(str)

    for character in str:
      characterMax += 1

      if character in lower:
        alphaIdx = lower.find(character)
        frequencies[alphaIdx] += 1

    for i in range(26):
      frequencies[i] = round((frequencies[i] / float(characterMax)), 4)

    return frequencies


print(textFileFrequencies())
print(' ')

def error(message):
  freqMessage = letterFrequencies(message)
  freqEnglish = textFileFrequencies()

  error = 0.0

  for i in range(26):
    error += (freqMessage[i] - freqEnglish[i])**2

  return sqrt(error)

print(error('oglurerpaomdennemeldingenerpaengelsk'))
print(' ')

def decryption(message):
  possibleKey = [0.0 for i in range(26)]
  
  message = onlyLower(message)
  
  for key in range(26):
    cypher = encrypt(message, key)
    cypherError = error(cypher)

    possibleKey[key] = cypherError
    
  mostLikelyKey = possibleKey.index(min(possibleKey))

  return encrypt(message, mostLikelyKey)
