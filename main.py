import re
import sys

import main

arrayRoadTypes = ['CARRERA', 'CRA', 'KRA', 'KR', 'CR', 'CALLE', 'CLL', 'CL', 'CT', 'CARRETERA', 'CQ', 'CIRCULAR', 'CIR', 'CV', 'CIRCUNVALAR', 'CRV', 'CC', 'CUENTASCORRIDAS', 'AU', 'AUT', 'AUTOPISTA', 'AV', 'AVENIDA', 'AC', 'AVENIDACALLE', 'AVENIDACLL', 'AVENIDAC', 'AVENIDACL', 'AVCALLE', 'AVCALLE', 'AVCLL', 'AVCL', 'AK', 'AVENIDACARRERA', 'AVENIDACRA', 'AVENIDAKRA', 'AVENIDAKR', 'AVENIDACR', 'AVENIDAK', 'AVCARRERA', 'AVCRA', 'AVKRA', 'AKR', 'AVCR', 'AVK', 'BL', 'BULEVAR', 'DG', 'DIAGONAL', 'DIAG', 'PJ', 'PASAJE', 'PS', 'PASEO', 'PT', 'PEATONAL', 'TV', 'TRANSVERSAL', 'TRANS', 'TR', 'TC', 'TRONCAL', 'VT', 'VARIANTE', 'VI', 'VIA', 'VÍA']
arrayRoadTypesNoneTwoWords = ['CARRERA', 'CRA', 'KRA', 'KR', 'CR', 'CALLE', 'CLL', 'CL', 'CT', 'CARRETERA', 'CQ', 'CIRCULAR', 'CIR', 'CV', 'CIRCUNVALAR', 'CRV', 'AU', 'AUT', 'AUTOPISTA', 'AV', 'AVENIDA',  'BL', 'BULEVAR', 'DG', 'DIAGONAL', 'DIAG', 'PJ', 'PASAJE', 'PS', 'PASEO', 'PT', 'PEATONAL', 'TV', 'TRANSVERSAL', 'TRANS', 'TR', 'TC', 'TRONCAL', 'VT', 'VARIANTE', 'VI', 'VIA', 'VÍA']
arrayNumeralV = ['NRO.', 'NO.', '#', 'N°', 'N.°', 'NUMERO', 'NUMERAL', 'NÚMERO']
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
bis = 'BIS'
cardinalPoints = ['NORTE', 'SUR', 'ESTE', 'OESTE']
ADDRESS = ''


def whatComponentIsNext(address):
    main.arrayNumeralV = sorted(main.arrayNumeralV, key=len, reverse=True)
    main.arrayRoadTypesNoneTwoWords = sorted(main.arrayRoadTypesNoneTwoWords, key=len, reverse=True)
    posBis1 = address.find(bis)
    posNumb = -1
    posTypeRoad = -1
    strComp = ''
    strTypeR = ''
    res = ''
    for i in main.arrayNumeralV:
        if address.find(i) != -1:
            posNumb = address.find(i)
            strComp = i
            break
    for i in main.arrayRoadTypesNoneTwoWords:
        if address.find(i) != -1:
            if i != main.ADDRESS[0:(len(main.ADDRESS) - len(address))-1]:
                posTypeRoad = address.find(i)
                strTypeR = i
                break
            else:
                break

    if posBis1 != -1 and posNumb != -1 and posBis1 < posNumb:
        res = str(posBis1) + " " + str(len(bis)+posBis1)+" "+bis
        return res
    elif posBis1 != -1 and posNumb != -1 and posBis1 > posNumb:
        res = str(posNumb)+" "+str(len(strComp)+posNumb)+" "+strComp
        return res
    elif posBis1 == -1 and posNumb != -1:
        res = str(posNumb)+" "+str(len(strComp)+posNumb)+" "+strComp
        return res
    elif posBis1 != -1 and posNumb == -1:
        res = str(posBis1)+" "+str(len(bis)+posBis1)+" "+bis
        return res
    elif posBis1 == -1 and posNumb == -1 and posTypeRoad != -1:
        res = str(posTypeRoad)+" "+str(len(strTypeR)+posTypeRoad)+" "+strTypeR
        return res
    else:
        res = res+'-1'
        return res


def q30(beforeCompoment, afterComponent, address2):
    print("q30")
    patternN = "/^[0-9]+$/"
    patternA = "/([A-Z]){1}/"
    re.compile(patternA)
    arrayBeforeC = beforeCompoment.split()
    arrayAfterC = afterComponent.split()
    count = 0
    for i in arrayBeforeC:
        for j in i:
            print(re.search(j, patternA))
            if re.search(patternA,j) != 'None':
                count += 1

    print(count)


def q36(beforeCompoment, afterComponent, address2):
    print("q36")
    arrayBeforeC = beforeCompoment.split()
    arrayAfterC = afterComponent.split()



def q10(address, pos):
    try:
        address2 = address[pos + 1: (len(address))] if address[pos + 1] == " " else address[pos: (len(address))]
        address2 = address2[1:len(address)] if address2[0] == ' ' else address2[0:len(address)]
        posNextComponent = whatComponentIsNext(address2)
        if len(posNextComponent) == 2:
            less1 = int(posNextComponent)
            sys.exit(1)
        else:
            arrayLimits = posNextComponent.split()
            if arrayLimits[0] == arrayLimits[1]:
                beforeComponent = address2[0: int(arrayLimits[0])]
                afterComponent = address2[int(arrayLimits[1])+1:len(address2)]
            else:
                beforeComponent = address2[0: int(arrayLimits[0])]
                afterComponent = address2[int(arrayLimits[1]):len(address2)]
            componentValue = arrayLimits[2]
            if componentValue == bis:
                q30(beforeComponent, afterComponent, address2)
            else:
                q36(beforeComponent, afterComponent, address2)


    except:
        print("Cadena no valida")
        sys.exit(1)


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
