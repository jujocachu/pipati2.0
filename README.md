Universidad Internacional del Ecuador

Materia: Lógica de Programación

Profesora: Paula Vizcaíno

Estudiante: Juan José Carrasco Chuchuca
                                                   
                                                   
                                                   JUEGO : PIEDRA, PAPEL o TIJERA




**1. Definición de la función jugar()**

   Agrupa todo el código del juego en un solo bloque reutilizable. 

**2. Creación del diccionario reglas**

   El juego necesita saber qué opción vence a cuál. Para eso, se usa una estructura llamada diccionario, que funciona como una lista de reglas.
o	Por ejemplo, dentro de la entrada 'piedra', se indica que vence a 'tijera', pero pierde contra 'papel'.

**3. Mensajes iniciales**
    
  Imprime en pantalla el nombre del juego y cuáles son las opciones permitidas. Así, ambos jugadores saben cómo escribir sus elecciones.

**4. Inicio del bucle infinito (while True)**

  Crea un ciclo que se repite una y otra vez para que el juego continúe rondas hasta que el jugador 1 escriba “salir”.

**5. Entrada del Jugador 1**

  Se le pide al primer jugador que escriba su jugada. Si escribe “salir”, se rompe el ciclo y se finaliza el juego.

**6. Entrada del Jugador 2**

  Si el jugador 1 no ha salido, se le solicita al segundo jugador su elección.

**7. Validación de entradas**

  Se verifica si ambas jugadas están dentro del diccionario de reglas o si alguien se equivoca y escribe otra palabra, se imprime un mensaje de error y se reinicia la ronda.

**8. Mostrar elecciones**

   Se imprime lo que eligió cada jugador para visualizar claramente el duelo de esa ronda.

**9. Verificación de empate**

  Si ambos jugadores eligieron lo mismo, se declara empate.

**10. Determinación del ganador con get**

    Aquí es donde entra el método get:

    -	get se usa para buscar el resultado en el diccionario.

    -	Se accede a la jugada del jugador 1 (por ejemplo, 'piedra') y se busca si vence a la jugada del jugador 2 (por ejemplo, 'tijera').

    -	Si existe esa combinación, get devuelve quién gana; si no existe se da por hecho que gana el jugador 2.

    -	Esto se hace que busque dentro de las reglas de la jugada del Jugador 1 quién gana. Si no lo encuentras, asume que gana el Jugador 2.

**11. Mostrar resultado**

  Se imprime en pantalla si ganó el Jugador 1, el Jugador 2, o si fue un empate, según las comparaciones anteriores.

**12. Llamada a la función jugar() al final**

  Esta línea ejecuta la función y pone en marcha el juego cuando se corre el script
