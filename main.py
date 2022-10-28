import re
import sys

import main

arrayRoadTypes = ['CARRERA', 'CRA', 'KRA', 'KR', 'CR', 'CALLE', 'CLL', 'CL', 'CT', 'CARRETERA', 'CQ', 'CIRCULAR', 'CIR',
                  'CV', 'CIRCUNVALAR', 'CRV', 'CC', 'CUENTASCORRIDAS', 'AU', 'AUT', 'AUTOPISTA', 'AV', 'AVENIDA', 'AC',
                  'AVENIDACALLE', 'AVENIDACLL', 'AVENIDAC', 'AVENIDACL', 'AVCALLE', 'AVCALLE', 'AVCLL', 'AVCL', 'AK',
                  'AVENIDACARRERA', 'AVENIDACRA', 'AVENIDAKRA', 'AVENIDAKR', 'AVENIDACR', 'AVENIDAK', 'AVCARRERA',
                  'AVCRA', 'AVKRA', 'AKR', 'AVCR', 'AVK', 'BL', 'BULEVAR', 'DG', 'DIAGONAL', 'DIAG', 'PJ', 'PASAJE',
                  'PS', 'PASEO', 'PT', 'PEATONAL', 'TV', 'TRANSVERSAL', 'TRANS', 'TR', 'TC', 'TRONCAL', 'VT',
                  'VARIANTE', 'VI', 'VIA', 'VÍA']
arrayRoadTypesNoneTwoWords = ['CARRERA', 'CRA', 'KRA', 'KR', 'CR', 'CALLE', 'CLL', 'CL', 'CT', 'CARRETERA', 'CQ',
                              'CIRCULAR', 'CIR', 'CV', 'CIRCUNVALAR', 'CRV', 'AU', 'AUT', 'AUTOPISTA', 'AV', 'AVENIDA',
                              'BL', 'BULEVAR', 'DG', 'DIAGONAL', 'DIAG', 'PJ', 'PASAJE', 'PS', 'PASEO', 'PT',
                              'PEATONAL', 'TV', 'TRANSVERSAL', 'TRANS', 'TR', 'TC', 'TRONCAL', 'VT', 'VARIANTE', 'VI',
                              'VIA', 'VÍA']
arrayNumeralV = ['NRO.', 'NO.', '#', 'N°', 'N.°', 'NUMERO', 'NUMERAL', 'NÚMERO']
bis = 'BIS'
cardinalPoints = ['NORTE', 'SUR', 'ESTE', 'OESTE']
ADDRESS = ''
patternA = "(([A-Z]){1})$"
patternB = "(([A-Z]){1}(\s|\-){1}([A-Z]){1})$"
patternC = "(([A-Z]){1}(\s|\-){1}(\d)(\s|\-){1}([A-Z]){1})$"
outPut = ''
isA = False
isAA = False
isA1A = False
isNumber = False
isAlphanumeric = False


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
            if i != main.ADDRESS[0:(len(main.ADDRESS) - len(address)) - 1]:
                posTypeRoad = address.find(i)
                strTypeR = i
                break
            else:
                break

    if posBis1 != -1 and posNumb != -1 and posBis1 < posNumb:
        res = str(posBis1) + " " + str(len(bis) + posBis1) + " " + bis
        return res
    elif posBis1 != -1 and posNumb != -1 and posBis1 > posNumb:
        res = str(posNumb) + " " + str(len(strComp) + posNumb) + " " + strComp
        return res
    elif posBis1 == -1 and posNumb != -1:
        res = str(posNumb) + " " + str(len(strComp) + posNumb) + " " + strComp
        return res
    elif posBis1 != -1 and posNumb == -1:
        res = str(posBis1) + " " + str(len(bis) + posBis1) + " " + bis
        return res
    elif posBis1 == -1 and posNumb == -1 and posTypeRoad != -1:
        res = str(posTypeRoad) + " " + str(len(strTypeR) + posTypeRoad) + " " + strTypeR
        return res
    else:
        res = res + '-1'
        return res


def qAfterBistoNumOrTypeR(afterComponent):
    arrayAfterC = afterComponent.split()
    for i in arrayAfterC:
        if re.search(main.patternA, i):
            main.isA = True
            main.outPut = main.outPut + '0'
            break
        elif re.search(main.patternB, i):
            main.isAA = True
            main.outPut = main.outPut + '0'
            break
        elif re.search(main.patternC, i):
            main.isA1A = True
            main.outPut = main.outPut + '0'
            break
        elif re.search("(\\d)", i):
            main.outPut = main.outPut + '0'
            break
        else:
            main.outPut = main.outPut + '1'
            print(main.outPut)
            print("Cadena no valida")
            sys.exit(1)


def qBeforeBisNum(beforeComponent):
    if beforeComponent[len(beforeComponent)-1] == ' ':
        beforeComponent = beforeComponent[0:len(beforeComponent)-1]
    print(beforeComponent)
    if re.search(main.patternC, beforeComponent):
        val = str(re.search(main.patternC, beforeComponent).span()).replace("(", "")
        val = val.replace(")", "")
        val = val.replace(",", "")
        val = val.split()
        beforeComponent = beforeComponent[0: (int(val[0]))]
        main.isA1A = True
        if re.search("(\\d|\w)", beforeComponent):
            main.isAlphanumeric = True
        elif re.search("(\\d)", beforeComponent):
            main.isNumber = True
        else:
            main.outPut = main.outPut + '1'
            print(main.outPut)
            print("Cadena no valida")
            sys.exit(1)
    elif re.search(main.patternB, beforeComponent):
        val = str(re.search(main.patternB, beforeComponent).span()).replace("(", "")
        val = val.replace(")", "")
        val = val.replace(",", "")
        val = val.split()
        beforeComponent = beforeComponent[0: int(val[0])-1]
        main.isAA = True
        if re.search("(\\d|\w)", beforeComponent):
            main.isAlphanumeric = True
        elif re.search("(\\d)", beforeComponent):
            main.isNumber = True
        else:
            main.outPut = main.outPut + '1'
            print(main.outPut)
            print("Cadena no valida")
            sys.exit(1)
    elif re.search(main.patternA, beforeComponent):
        val = str(re.search(main.patternA, beforeComponent).span()).replace("(", "")
        val = val.replace(")", "")
        val = val.replace(",", "")
        val = val.split()
        back = beforeComponent[int(val[0])-1]
        if (48 <= ord(back) <= 57) or back == " ":
            main.isA = True
        else:
            if re.search("(\\d|\w)", beforeComponent):
                main.isAlphanumeric = True
            elif re.search("(\\d)", beforeComponent):
                main.isNumber = True
            else:
                main.outPut = main.outPut + '1'
                print(main.outPut)
                print("Cadena no valida")
                sys.exit(1)
    else:
        if re.search("(\\d|\w)", beforeComponent):
            main.isAlphanumeric = True
        elif re.search("(\\d)", beforeComponent):
            main.isNumber = True
        else:
            main.outPut = main.outPut + '1'
            print(main.outPut)
            print("Cadena no valida")
            sys.exit(1)


def qNumb(beforeComponent, afterComponent, address):
    print("qNumb")


def qbis(beforeComponent, afterComponent, address2):
    qBeforeBisNum(beforeComponent)
    if main.isAlphanumeric:
        main.outPut = main.outPut + "0"
        if main.isA or main.isAA or main.isA1A:
            main.outPut = main.outPut + "0"
            print("A", main.isA)
            print("AA", main.isAA)
            print("A1A", main.isA1A)
            print("Alpha", main.isAlphanumeric)
            print("num", main.isNumber)
            print("output", main.outPut)
            print("\n")
            main.isA = False
            main.isAA = False
            main.isA1A = False
            main.isNumber = False
            main.isAlphanumeric = False


def q10(address, pos):
    re.compile(main.patternA)
    re.compile(main.patternB)
    re.compile(main.patternC)
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
                afterComponent = address2[int(arrayLimits[1]) + 1:len(address2)]
            else:
                beforeComponent = address2[0: int(arrayLimits[0])]
                afterComponent = address2[int(arrayLimits[1]):len(address2)]
            componentValue = arrayLimits[2]
            if componentValue == bis:
                qbis(beforeComponent, afterComponent, address2)
            else:
                qNumb(beforeComponent, afterComponent, address2)
    except:
        main.outPut = main.outPut + '1'
        print("Cadena no valida")
        print(main.outPut)
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
        main.outPut = '0'
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
