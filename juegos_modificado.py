# • Agregar al programa juegos.py una función que guarde los datos del jugador y a qué juego jugó.
# • Definir y justificar la estructura de datos a utilizar.
# • Elegir y justificar el formato de archivo a utilizar.
# • Si pasan el menú a PySimpleGUI, suman doble.
# • Deben subir el código a git y dejar el enlace en una tarea que será creada en catedras.info.
# • Fecha límite: 11 de mayo.
# ------------------------------------------------------------------------------------------------
import hangman
import reversegam
import tictactoeModificado
import os
import json
import PySimpleGUI as sg

def main(args):
	
	def guardar_datos(key, value, data):
		
		nonlocal returning_player
		# Chequeo si se guarda usuario
		if key == 'username':
			# Busco si el usuario estaba registrado
			found = False
			i = 0
			while not found and i < len(data):
				if value == data[i][key]:
					found = True
					returning_player = i
					print('''
		Bienvenida/o de vuelta {}!'''.format(value))
				i += 1
			if not found:
				# Agrego nuevo usuario
				data.append(
				{key: value,
				'games_played': []})
				print('''
		Bienvenida/o {}!'''.format(value))
		# Chequeo si se guarda juegos jugados
		elif key == 'games_played':
			# Si es un nuevo usuario guardo al final de la lista
			if returning_player == -1:
				data[len(data) - 1][key].append(value)
			else:
				data[returning_player][key].append(value)

	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Se elije la estructura de archivo porque se busca la PERSISTENCIA de los    #
	# datos más allá de la ejecución del programa en memoria principal o RAM.     #
	# --------------------------------------------------------------------------- #
	# Se utiliza json por la mayor portabilidad y seguridad que otorga, además    #
	# que es compatible con la estructura  de lista de diccionarios que se usa.    #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	if os.path.exists('juegos_data.txt'):
		# Cargo el archivo en memoria
		archivo = open('juegos_data.txt', 'r')
		data = json.load(archivo)
		archivo.close()
	else:
		data = []
	archivo = open('juegos_data.txt', 'w')

	sigo_jugando = True
	while sigo_jugando:
		# Tema para PySympleGUI
		sg.theme('LightGrey')
		# Organización del menú
		layout = [  [sg.Text('Elegí con qué juego querés jugar:')],
					[sg.Button('Ahorcado')], 
					[sg.Button('Ta-Te-Ti')],
					[sg.Button('Otello')], 
					[sg.Button('-Salir-')]  ]
		# Creo la ventana
		window = sg.Window('Jueguitos', layout)
		# Capturo la interacción
		event, values = window.read()
		# Cierro la ventana
		window.close()
		# Si el usuario no cierra la ventana ni cliquea -Salir-
		if event not in (None, '-Salir-'):
			# Variable para informar si el usuario es existente
			returning_player = -1
			# Se guarda el nombre de usuario en una lista
			guardar_datos('username', input('Ingrese su nombre de usuario: '), data)
			# Se ejecuta el juego elegido
			if event == 'Ahorcado':
				hangman.main()
			elif event == 'Ta-Te-Ti':
				tictactoeModificado.main()
			elif event == 'Otello':
				reversegam.main()
			# Se guarda el juego que se ejecutó
			guardar_datos('games_played', event, data)
		# El usuario la ventana o cliquea Salir
		elif event in (None, '-Salir-'):
			sigo_jugando = False
	# Guardo en el archivo y lo cierro
	json.dump(data, archivo)
	archivo.close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
