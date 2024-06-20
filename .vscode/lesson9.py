# sum of even numbers by 'n'

n = int(input('n = '))
sum = 0
for i in range(1, n):
    if i%2==0 : 
        sum += i 
print('Total = ', sum)