piedra = '''
                       888      
                       888      
                       888      
888d888 .d88b.  .d8888b888  888 
888P"  d88""88bd88P"   888 .88P 
888    888  888888     888888K  
888    Y88..88PY88b.   888 "88b 
888     "Y88P"  "Y8888P888  888 
'''
papel = '''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88    
'''
tijera= '''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
                                   
'''
import random 
imagenes = [piedra, papel, tijera]

opcion = int(input('que opcion escogerias?? 1 "piedra", 2 "papel" o 3 "tijera"\n'))
if opcion >= 3 or opcion < 0:
    print("Opción inválida.")
  
else: 
  print(imagenes[opcion])
  
  opcion2= random.randint(0, 2)
  print(f'turno de la computadora:{opcion2}')
  print(imagenes[opcion2])
  
  if opcion == 0 and opcion2 == 2:
      print("¡Tú ganaste!")
  elif opcion2 == 0 and opcion == 2:
      print("¡Tú perdiste!")
  elif opcion2 > opcion:
      print("¡Tú pierdes!")
  elif opcion > opcion2:
       print("¡Tú ganaste!")
  elif opcion == opcion2:
      print("¡Empates!")
  