inf = open('paper.txt','r')

for line in inf:
  print(line)

inf.close()

inf = open('paper.txt','r')

for line in inf:
  words = line.split()
  for word in words:
    print(word)
