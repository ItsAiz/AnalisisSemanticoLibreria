import re
import sys

import main

arrayRoadTypes = ['CARRERA', 'CRA', 'KRA', 'KR', 'CR', 'CALLE', 'CLL', 'CL', 'CT', 'CARRETERA', 'CQ', 'CIRCULAR', 'CIR',
                  'CV', 'CIRCUNVALAR', 'CRV', 'CC', 'CUENTAS CORRIDAS', 'AU', 'AUT', 'AUTOPISTA', 'AV', 'AVENIDA', 'AC',
                  'AVENIDA CALLE', 'AVENIDA CLL', 'AVENIDA C', 'AVENIDA CL', 'AK', 'AVENIDA CARRERA', 'AVENIDA CRA',
                  'AVENIDA KRA', 'AVENIDA KR', 'AVENIDA CR', 'AVENIDA K', 'BL', 'BULEVAR', 'DG', 'DIAGONAL', 'DIAG',
                  'PJ', 'PASAJE', 'PS', 'PASEO', 'PT', 'PEATONAL', 'TV', 'TRANSVERSAL', 'TRANS', 'TR', 'TC', 'TRONCAL',
                  'VT', 'VARIANTE', 'VI', 'VIA']
arrayNumeralV = ['Nro.', 'No.', '#', 'N°', 'N.°', 'n°', 'n.°', 'Numero', 'numero', 'Numeral','numeral']


def q10(address, pos):
    address2 = address[pos: (len(address) - 1)]
    patternAZ = re.compile("^[A-Z]+$")
    pattern09 = re.compile("^\d+$")
    patternECAZ09 = re.compile("^[A-Za-z#'°.\d\-]+$")
    count = 0
    "for i in main.arrayNumeralV:"
    "if i in address2:"


def validateTypeOfRoad(address):
    main.arrayRoadTypes = sorted(main.arrayRoadTypes, key=len, reverse=True)
    direc = ""
    for i in main.arrayRoadTypes:
        if address.startswith(i):
            direc += i
            break
    if len(direc) > 1:
        q10(address, len(direc))
    else:
        sys.exit(1)


def traverseString(arrayAddresses):
    for i in arrayAddresses:
        validateTypeOfRoad(i)


def run():
    pattern = r'\s+'
    fileName = 'DIRECCIONES.txt'
    arrayAddresses = []
    for i in main.arrayRoadTypes:
        val = re.sub(pattern, '', i)
        main.arrayRoadTypes.remove(i)
        main.arrayRoadTypes.append(val)
    with open(fileName, encoding="utf8") as file_object:
        while True:
            line = file_object.readline().strip().upper()
            line = re.sub(pattern, '', line)
            arrayAddresses.append(line)
            if not line:
                break
    arrayAddresses.pop()
    traverseString(arrayAddresses)


if __name__ == '__main__':
    run()
