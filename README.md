 # Objetivo:
Desarrolla una aplicación de línea de comandos (CLI) que procese un archivo CSV con transacciones bancarias y genere un reporte que incluya:

Balance Final:
Suma de los montos de las transacciones de tipo "Crédito" menos la suma de los montos de las transacciones de tipo "Débito".
Transacción de Mayor Monto:
Identificar el ID y el monto de la transacción con el valor más alto.
Conteo de Transacciones:
Número total de transacciones para cada tipo ("Crédito" y "Débito").

# Instrucciones de Ejecucion 
python 3.10.4
arhivos:  read.py ==> ejecutable
          input.txt ==> archivo con el registro de transacciones
           en el siguiente formato:
           id,tipo,monto
           1,Credito,100.00
           2,Debito,50.00
           

# Enfoque y Solución:
Se abre el archivo de texto y se lee linea a linea, en cada linea se suma y calcula en variables los valores necesarios para el reporte final

# Documentación y Calidad del Código:
El código fuente se encuentra documentado y se indica paso a paso la secuencia de ordenes a ejecutar
