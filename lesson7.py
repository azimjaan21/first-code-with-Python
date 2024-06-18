# EURO 2024

portugal = ['Diego Costa 22','Pepe 3','Bruno Fernandes`8','Cristiano Ronaldo 7']
print(portugal)
 #Selecting Capitan, .....
capitan = portugal.pop(3)
goalkeeper = portugal.pop(0)
defender = portugal.pop(1)

#Adding new players
second_striker = 'Bernardo Silva'
#Substution
portugal.insert(2,second_striker)

#
print("Capitan of team -> " + capitan)
print("Goalkeeper of team -> " + goalkeeper)

print("Substution: \nB.Fernandes 8`(-)\nB.Silva(+) 10")
print(portugal)