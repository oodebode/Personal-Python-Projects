def sumMultiples_3_5(n):
        sum = 0
        for number in range(n):
                if number % 3 == 0 or number % 5 == 0:
                        sum += number
        
        return sum

print(sumMultiples_3_5(20))
