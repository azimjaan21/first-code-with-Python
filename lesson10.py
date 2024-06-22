#loop

a = input('Please, write any number -> ')

while a :
    if a.isdigit():
       print('Good job!')
       break
    else: print('Please, any number!')
    a = input('Please, write any number -> ')