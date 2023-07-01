print('''
                _
              (`  ).                   _
             (     ).              .:(`  )`.
)           _(       '`.          :(   .    )
        .=(`(      .   )     .--  `.  (    ) )
       ((    (..__.:'-'   .+(   )   ` _`  ) )
`.     `(       ) )       (   .  )     (   )  ._
  )      ` __.:'   )     (   (   ))     `-'.-(`  )
)  )  ( )       --'       `- __.'         :(      ))
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'

--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.

''')


print("Historia de amor.")
print("Encuentra a tu novio.")

eleccion1 = input('Vas caminando por la calle. En qué dirección vas? "derecha" or "izquierda"\n').lower()

if eleccion1 == "derecha":
  eleccion2 = input('Te diriges a la casa de él y ves que la puerta está abierta. ¿Qué decides hacer? "entrar" o "esperar"\n').lower()
  
  if eleccion2 == "esperar":
    print('Llegó la noche y nunca lo encontraste')
  else:
    eleccion3 = input('Decides entrar y lo encuentras con otra chica que no conoces. ¿Decides "enfrentarlo" o "irte"?\n').lower()
    
    if eleccion3 == "enfrentarlo":
      print('Descubres que es una prima de él y tú quedaste de entrometida')
    else:
      print("Fuiste a tu casa y le escribiste un mensaje preguntando, él te contesta rápido y te invita a conocer a su prima que vino del extranjero")
else:
  print("Fuiste a tu casa a ver televisión")
  
  
                    