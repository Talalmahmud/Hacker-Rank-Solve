# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def prime_check(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True
            
    
    
n = int(input())

for i in range(n):
    value = int(input())

    if value >= 2 and prime_check(value):
        print ('Prime')
    else:
        print ('Not prime')
    
