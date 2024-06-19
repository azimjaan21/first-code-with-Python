#practice_6
#sum of numers for any NUMBER(e.g: 367-> 3+6+7 = 16)

number = int(input('Any 3 Digit Number (p.s: 237): '))

a = number//100
b = number%100
c = b//10
d = number%10
total = a + c + d
print("Sum of 3 digit for ",number,' -> ',total)

