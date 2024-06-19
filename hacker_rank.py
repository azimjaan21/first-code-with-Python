#leap year
n_year = int(input("Write any year: "))

if n_year % 400 == 0 :
    print (n_year, ' is Leap Year !') 
elif n_year % 100 == 0 :
    print (n_year, ' is not Leap Year !')
elif n_year % 4 == 0 :
    print(n_year, ' is Leap Year')