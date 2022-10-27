import re
import sys

import main

arrayRoadTypes = ['CARRERA', 'CRA', 'KRA', 'KR', 'CR', 'CALLE', 'CLL', 'CL', 'CT', 'CARRETERA', 'CQ', 'CIRCULAR', 'CIR', 'CV', 'CIRCUNVALAR', 'CRV', 'CC', 'CUENTASCORRIDAS', 'AU', 'AUT', 'AUTOPISTA', 'AV', 'AVENIDA', 'AC', 'AVENIDACALLE', 'AVENIDACLL', 'AVENIDAC', 'AVENIDACL', 'AVCALLE', 'AVCALLE', 'AVCLL', 'AVCL', 'AK', 'AVENIDACARRERA', 'AVENIDACRA', 'AVENIDAKRA', 'AVENIDAKR', 'AVENIDACR', 'AVENIDAK', 'AVCARRERA', 'AVCRA', 'AVKRA', 'AKR', 'AVCR', 'AVK', 'BL', 'BULEVAR', 'DG', 'DIAGONAL', 'DIAG', 'PJ', 'PASAJE', 'PS', 'PASEO', 'PT', 'PEATONAL', 'TV', 'TRANSVERSAL', 'TRANS', 'TR', 'TC', 'TRONCAL', 'VT', 'VARIANTE', 'VI', 'VIA', 'VÍA']
arrayNumeralV = ['NRO.', 'NO.', '#', 'N°', 'N.°', 'NUMERO', 'NUMERAL', 'NÚMERO']
bis = 'BIS'
ADDRESS = ''


def whatComponentIsNext(address):
    main.arrayNumeralV = sorted(main.arrayNumeralV, key=len, reverse=True)
    posBis1 = address.find(bis)
    posNumb = -1
    for i in main.arrayNumeralV:
        if address.find(i) != -1:
            posNumb = address.find(i)
            break
    if posBis1 != -1 and posNumb != -1 and posBis1 < posNumb:
        return address[posBis1:len(address)]
    elif posBis1 != -1 and posNumb != -1 and posBis1 > posNumb:
        return address[posNumb:len(address)]
    elif posBis1 == -1 and posNumb != -1:
        return address[posNumb:len(address)]
    elif posBis1 != -1 and posNumb == -1:
        return address[posBis1:len(address)]
    else:
        return sys.exit(1)


def q10(address, pos):
    address2 = address[pos+1: (len(address))] if address[pos+1] == " " else address[pos: (len(address))]
    address2 = address2[1:len(address)] if address2[0] == ' ' else address2[0:len(address)]
    posNextComponent = whatComponentIsNext(address2)
    print(posNextComponent)


def validateTypeOfRoad(address):
    main.ADDRESS = address
    main.arrayRoadTypes = sorted(main.arrayRoadTypes, key=len, reverse=True)
    pattern = r'\s+'
    addressPiv = re.sub(pattern, '', address)
    direc = ""
    for i in main.arrayRoadTypes:
        if address.startswith(i) or addressPiv.startswith(i):
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
    with open(fileName, encoding="utf8") as file_object:
        while True:
            line = file_object.readline().strip().upper()
            "line = re.sub(pattern, '', line)"
            arrayAddresses.append(line)
            if not line:
                break
    arrayAddresses.pop()
    traverseString(arrayAddresses)


if __name__ == '__main__':
    run()
