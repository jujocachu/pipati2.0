def jugar():
    # Diccionario que define qué le gana a qué
    reglas = {
        'piedra': {'tijera': 'Jugador 1 gana', 'papel': 'Jugador 2 gana'},
        'papel': {'piedra': 'Jugador 1 gana', 'tijera': 'Jugador 2 gana'},
        'tijera': {'papel': 'Jugador 1 gana', 'piedra': 'Jugador 2 gana'}
    }
    
    print("=== PIEDRA, PAPEL O TIJERA ===")
    print("Opciones válidas: piedra, papel, tijera\n")
    
    while True:
        j1 = input("Jugador 1 (o 'salir' para finalizar el juego): ").lower()
        if j1 == 'salir':
            print("¡Juego terminado!")
            break
            
        j2 = input("Jugador 2: ").lower()
        
        # Validación de entradas
        if j1 not in reglas or j2 not in reglas:
            print("¡Opción no válida! Intenta otra vez\n")
            continue
            
        print(f"\nJugador 1: {j1}  vs  Jugador 2: {j2}")
        
        if j1 == j2:
            print("¡Empate!\n")
        else:
            resultado = reglas[j1].get(j2, 'Jugador 2 gana')
            print(f"¡{resultado}!\n")

# Iniciar el juego
jugar()