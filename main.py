print("Hello World")

z = 42.5 # définir une variable
print(z) # afficher la variable
print(int(z)) # afficher la variable sans décimale

x = 5
y = 5

if (x==y):
    print("True") # Vérifier si condition remplie (même valeur)

arr=[1,2,3,4,5]
for i in arr:
    print (i) # Imprimer la liste de façon verticale

print(arr) # Imprimer la liste de façon horizontale

for i in arr:
    print(i,end=' ') # Imprimer en horizontale sans les parenthèses

print(arr[3]) # Afficher la 4ème valeur (commence à 0)

print(arr[::-1]) # Afficher la liste à l'envers (5, 4, 3, ...)

test1 = [1,2,3]
test2 = [1,2,3]
print(test1 is test2) # test1 n'est pas test2 même si les valeurs sont les mêmes
print(test1==test2) # en revanche les valeurs sont les mêmes

test1=test2
print(test1 is test2) # Ici, test1 et test2 ne font qu'un