# Juego del ahorcado
	Proyecto grupal para desarrollar un ahorcado funcional en Python

## Descripción
	El juego consiste en adivinar el título de una película ingresando una letra por turno.
	El jugador dispone de un máximo de 6 intentos incorrectos.
	El programa muestra las letras descubiertas, los intentos restantes y el resultado final de la partida.
	El programa solo permite un tipo de entrada, este siendo una sola letra. Da error al recibir más de una letra o un caracter no válido.
## Archivos del proyecto
	main.py: ejecuta el juego y permite interactuar con el usuario.
	game.py: contiene las reglas, los intentos y las condiciones de victoria o derrota.
	utils.py: selecciona aleatoriamente uno de los nombres de wordlist.txt.
	wordlist.txt: contiene los nombres de películas que se usarán en el programa.
## Ejecución
	Para iniciar el juego, ejecutar desde la terminal:
	python3 main.py
	Termina al ganar o perder.
