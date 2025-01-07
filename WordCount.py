class WordCount:
  def __init__(self, word, count):
    self.word = word
    self.count = count

  def setCount(self):
    self.count = 0
    
  def increaseCount(self, count):
    self.count += count

  def getCount(self):
    return self.count 
    
  def getWord(self): 
    return self.word
    
  def __str__(self):
    return self.word + " " + str(self.count)

  def __repr__(self):
    return self.word + " " + str(self.count)

def main():
  myWord = WordCount("test",3)
  print(myWord)
  myWord.increaseCount(5)
  print(myWord)
  list = [WordCount("test",x) for x in range(1,10)]
  print(list)

main()

def sampleWordCount():
  inf = open('sampleText.txt','r')
  wordCountList = []
  
  for line in inf:
    words = set(line.split())
    for word in words:
      if(WordCount(word,0) not in wordCountList):
        wordCountList.append(WordCount(word,0)) 
  inf.close()
  print(wordCountList)
  return wordCountList
  
print(sampleWordCount())
      
