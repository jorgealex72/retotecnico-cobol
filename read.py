with open('input.txt', 'r') as file:
    # Omitir el encabezados
    next (file)

    #variables
    bfinal = 0
    tmayor = 0
    tccredito = 0
    tcdebito = 0
    nrow = 0

    # Lee linea a linea hasta el final del archivo
    for line in file:
        # Divide en columnas
        columns = line.strip().split(',')

        nrow += 1
        if float(columns[2]) > tmayor:
                # tmayor almacena la transaccion con mayor valor
                tmayor = float(columns[2])
                signo = "+" if columns[1] == "Credito" else "-"
                result = 'Transaccion de mayor monto: ID ' + str(nrow)  + ' monto :' + signo + str(tmayor)

        # suma linea a linea de acuerdo al tipo de transacción
        if columns[1] == "Debito":
                tcdebito += 1
                bfinal -= float(columns[2])
        if columns[1] == "Credito":
                tccredito += 1
                bfinal += float(columns[2])

    #Reporte final
    print('Reporte de Transacciones')
    print('------------------------')
    print('Balance Final :' , str(bfinal)  )
    print(result)
    print('Conteo de Transacciones: Credito=', tccredito, ' Debito=', tcdebito)
