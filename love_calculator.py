print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n1= name1.lower()
n2 = name2.lower()

cuenta=0
cuenta2=0

cuenta += n1.count('t') + n2.count('t')
cuenta += n1.count('r') + n2.count('r')
cuenta += n1.count('u') + n2.count('u')
cuenta += n1.count('e') + n2.count('e')

cuenta2 += n1.count('l') + n2.count('l')
cuenta2 += n1.count('o') + n2.count('o')
cuenta2 += n1.count('v') + n2.count('v')
cuenta2 += n1.count('e') + n2.count('e')

total = int(str(cuenta) + str(cuenta2))

if total <10 or total >90:
    
    print(f'Your score is {total}, you go together like coke and mentos.')
elif 40<= total <=50:
    print(f'Your score is {total}, you are alright together.')
else:
    print(f'Your score is {total}.')
