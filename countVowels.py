def countVowels(str):
    vowels = ['a','e','i','o','u']
    vowelCount = 0
    for character in str:
        for vowel in vowels:
            if character == vowel:
                vowelCount += 1
    return vowelCount
        
print(countVowels('Python'))
