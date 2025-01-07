def reverseSlicing(str):
    reverseStr = ''
    for letter in str:
        reverseStr = letter + reverseStr
    return reverseStr

print(reverseSlicing('Hello'))
        
