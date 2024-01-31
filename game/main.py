import random


def opcion():
   opciones = ('piedra', 'papel', 'tijera')
   usu = input('piedra, papel o tijera => ')
   usu = usu.lower()

   if not usu in opciones:
    print('esa opcion no es valida')
    # continue
    return None, None

   pc = random.choice(opciones)

   print('usuario =>', usu)
   print('Computadora =>', pc)
   return usu, pc

def eleccion(usu, pc, usuario, computadora):
  if usu == pc:
    print('Empate!')
  elif usu == 'piedra':
    if pc == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      usuario += 1
    else:
      print('Papel gana a piedra')
      print('computer gano!')
      computadora += 1
  elif usu == 'papel':
    if pc == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      usuario += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computadora += 1
  elif usu== 'tijera':
    if pc == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      usuario += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computadora += 1
  return usuario,computadora

def comienzo():
  computadora = 0
  usuario = 0  
  ronda = 1
  while True:
    print('*' * 10)
    print('ROUND', ronda)
    print('*' * 10)

    print('computadora', computadora)
    print('usuario', usuario)
    ronda += 1

    usu,pc = opcion()
    usuario,computadora = eleccion(usu,pc,usuario,computadora)

    if computadora == 2:
      print('El ganador es la computadora')
      break

    if usuario == 2:
      print('El ganador es el usuario')
      break

comienzo()