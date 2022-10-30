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
arrayComplement = ['ADMINISTRACION', 'ADMINISTRACIÓN', 'AD', 'AGRUPACIÓN', 'AGRUPACION', 'AG', 'ALTILLO', 'AL', 'APARTAMENTO', 'AP', 'BARRIO', 'BR', 'BLOQUE', 'BQ', 'BODEGA', 'BG', 'CASA', 'CS', 'CÉLULA', 'CELULA', 'CU', 'CENTRO COMERCIAL', 'CE', 'CIUDADELA', 'CD', 'CONJUNTO RESIDENCIAL', 'CO', 'CONSULTORIO', 'CN', 'DEPOSITO', 'DP', 'DEPOSITO SÓTANO', 'D', 'DEPOSITO SOTANO','EDIFICIO', 'ED', 'ENTRADA', 'EN', 'ESQUINA', 'EQ', 'ESTACIÓN', 'ES', 'ESTACION', 'ETAPA', 'ET', 'EXTERIOR', 'EX', 'FINCA', 'FI', 'GARAJE', 'GA', 'GARAJE SÓTANO', 'GS', 'GARAJE SOTANO', 'INTERIOR', 'IN', 'KILÓMETRO', 'KM', 'KILOMETRO', 'LOCAL', 'LC', 'LOCAL MEZZANINE', 'LM' , 'LOTE', 'LT', 'MANZANA', 'MZ', 'MEZZANINE', 'MN','MÓDULO', 'MODULO', 'MD', 'OFICINA', 'OF', 'PARQUE', 'PQ', 'PARQUEADERO', 'PA', 'PENT-HOUSE', 'PN', 'PISO', 'PI', 'PLANTA', 'PL', 'PORTERIA', 'PR', 'PREDIO', 'PD', 'PUESTO', 'PU', 'ROUND POINT', 'RP', 'SECTOR', 'SC', 'SEMISÓTANO', 'SEMISOTANO', 'SS', 'SÓTANO', 'SO', 'SOTANO', 'SUITE', 'ST', 'SUPERMANZANA', 'SM', 'TERRAZA', 'TZ', 'TORRE', 'TO', 'UNIDAD', 'UN', 'UNIDAD RESIDENCIAL', 'UL', 'URBANIZACIÓN', 'URBANIZACION', 'UR', 'ZONA', 'ZN']
bis = 'BIS'
ADDRESS = ''
patternA = "(([A-Z]){1})$"
patternB = "(([A-Z]){1}(\s|\-){1}([A-Z]){1})$"
patternC = "(([A-Z]){1}(\s|\-){1}(\d)(\s|\-){1}([A-Z]){1})$"
patternCardinal = "(NORTE)|(SUR)|(ESTE)|(OESTE)"
patternDecimal = "^((\d*)(\s|-)(\d*))"
outPut = ''
conditionAfterNumber = False
isA = False
isAA = False
isA1A = False
isNumber = False
isAlphanumeric = False
isCardinal = False
isSpace = False
isAccepted = False
isComplement = False


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


def isCardinalValidate(address):
    re.compile(main.patternCardinal)
    main.isCardinal = True if re.search(main.patternCardinal, address) else False


def formatRefexRes(value):
    value = str((value.span())).replace("(", "")
    value = value.replace(")", "")
    value = value.replace(",", "")
    return value.split()


def qAfterBistoNumOrTypeR(afterComponent):
    isCardinalValidate(afterComponent)
    if afterComponent is None or len(afterComponent) == 0:
        main.isSpace = True
    else:
        if main.isCardinal:
            posCardinal = formatRefexRes(re.search(main.patternCardinal, afterComponent))
            afterComponent = afterComponent[0:int(posCardinal[0])]
        if afterComponent[0] == ' ' and len(afterComponent) > 1:
            afterComponent = afterComponent[1:len(afterComponent)]
        if afterComponent[len(afterComponent) - 1] == ' ':
            afterComponent = afterComponent[0:len(afterComponent) - 1]
        if re.search(main.patternA, afterComponent):
            val = formatRefexRes(re.search(main.patternA, afterComponent))
            back = afterComponent[int(val[0]) - 1]
            if (48 <= ord(back) <= 57) and len(afterComponent) < 1 or back == " " or back == "":
                main.isA = True
            else:
                if afterComponent[0] == ' ':
                    qAfterBistoNumOrTypeR(afterComponent)
                else:
                    main.isA = True
                    if re.search(main.patternB, afterComponent):
                        main.isAA = True
                        main.isA = False
                    if re.search(main.patternC, afterComponent):
                        main.isA1A = True
                        main.isA = False
                        main.isAA = False

        else:
            if afterComponent == "" or afterComponent == " ":
                main.isSpace = True


def qBeforeBisNum(beforeComponent):
    if beforeComponent[len(beforeComponent) - 1] == ' ':
        beforeComponent = beforeComponent[0:len(beforeComponent) - 1]
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
            print("Cadena no valida BeforeBis1")
            sys.exit(1)
    elif re.search(main.patternB, beforeComponent):
        val = str(re.search(main.patternB, beforeComponent).span()).replace("(", "")
        val = val.replace(")", "")
        val = val.replace(",", "")
        val = val.split()
        beforeComponent = beforeComponent[0: int(val[0]) - 1]
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
        back = beforeComponent[int(val[0]) - 1]
        if (48 <= ord(back) <= 57) or back == " ":
            main.isA = True
            main.isAlphanumeric = True
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
            print("Cadena no valida beforeBis")
            sys.exit(1)


def zerosAmount(val):
    count = 0
    for i in val:
        if i == " ":
            count += count
    return count


def complement(value):
    for i in main.arrayComplement:
        if value.find(i) != 1:
            main.isComplement = True
            break


def qNumb(afterComponent, address):
    s = [int(s) for s in re.findall(r'-?\d+\.?\d*', afterComponent)]
    for i in s:
        if str(i).startswith("-") and len(s) > 2:
            s.remove(i)
    afterComponentAux = afterComponent.replace(" ", "")
    if s[1] < 0:
        s[1] = s[1]*(-1)
    posNumb1 = afterComponent.index(str(s[0]))
    posNum2 = afterComponent.index(str(s[1]))
    if len(s) == 2:
        # print("pos", afterComponent[posNumb1], "pos2", afterComponent[posNum2+1])
        if afterComponent[posNum2] == "-":
            posNum2 = posNum2 + 1
        afterBetweenNumbs = afterComponent[posNumb1:posNum2]
        posNextComponent = whatComponentIsNext(afterBetweenNumbs)
        posNextComponent = posNextComponent.split()
        for i in main.arrayRoadTypes:
            if len(posNextComponent) > 1 and posNextComponent[2] == i:
                main.conditionAfterNumber = True
                break
        if re.search(patternDecimal, afterComponentAux):
            posNumbs = formatRefexRes(re.search(patternDecimal, afterComponentAux))
            posStart = int(posNumbs[1]) + zerosAmount(afterComponent) + 2
            afterComponent = afterComponent[posStart: len(afterComponent)]
            if len(posNextComponent) > 1 and posNextComponent[2] == main.bis:
                main.outPut = main.outPut + '0'
            if len(afterComponent) == 0:
                main.outPut = main.outPut + '0'
                main.isAccepted = True
            else:
                isCardinalValidate(afterComponent)
                complement(afterComponent)
                if main.isCardinal:
                    val = str(re.search(main.patternCardinal, afterComponent).span()).replace("(", "")
                    val = val.replace(")", "")
                    val = val.replace(",", "")
                    val = val.split()
                    afterComponent = afterComponent[int(val[1]):len(afterComponent)]
                    if len(afterComponent) > 0:
                        if main.isComplement:
                            main.outPut = main.outPut + '00'
                            main.isAccepted = True
                    else:
                        main.outPut = main.outPut + '0'
                        main.isAccepted = True
                if main.isComplement:
                    main.outPut = main.outPut + '0'
                    main.isAccepted = True


        else:
            main.patternA = "(([A-Z]){1})"
            main.patternB = "([A-Z]){1}(\s|\-){1}([A-Z]){1}"
            main.patternC = "([A-Z]){1}(\s|\-){1}(\d)(\s|\-){1}([A-Z]){1}"
            re.compile(main.patternA), re.compile(main.patternB), re.compile(main.patternC)
            if afterComponent[posNum2] == "-":
                posNum2 = posNum2 + 1
            afterComponentD = afterComponent[posNumb1:posNum2]
            posBis = afterComponentD.find(main.bis)
            afterComponentD = afterComponentD.replace(" ", "")
            qAfterBistoNumOrTypeR(afterComponent)
            if afterBetweenNumbs.find(main.bis) != -1:
                if 90 <= ord(afterComponentD[posBis]) <= 65:
                    main.outPut = main.outPut + "1"
                    main.isAccepted = False
                else:
                    main.outPut = main.outPut + '0'
                    main.isAccepted = True
            if main.isA or main.isAA or main.isA1A and not main.conditionAfterNumber:
                if posBis != -1:
                    if 90 <= ord(afterComponentD[posBis+2]) <= 65:
                        main.outPut = main.outPut + "1"
                        main.isA = False
                        main.isAA = False
                        main.isA1A = False
                        main.isAccepted = False
                    else:
                        main.outPut = main.outPut + '0'
                        main.isA = False
                        main.isAA = False
                        main.isA1A = False
                        main.isAccepted = True
                else:
                    main.outPut = main.outPut + '0'
                    main.isA = False
                    main.isAA = False
                    main.isA1A = False
                    main.isAccepted = True
            else:
                if main.conditionAfterNumber:
                    main.outPut = main.outPut + '1'
                    main.isAccepted = False
                    main.conditionAfterNumber = False
                    print("Dirección no valida")
                    print(main.outPut)
                if afterBetweenNumbs.find(main.bis) != -1:
                    main.outPut = main.outPut + '0'
                    main.isAccepted = True
    else:
        main.isAccepted = False
        main.outPut = main.outPut + '1'


def qvalidateAfterBis(afterComponent, address):
    posAfterComponent = whatComponentIsNext(afterComponent)
    arrayLimits = posAfterComponent.split()
    if arrayLimits[0] == arrayLimits[1]:
        beforeComponentAfter = afterComponent[0: int(arrayLimits[0])]
        afterComponentAfter = afterComponent[int(arrayLimits[1]) + 1:len(afterComponent)]
    else:
        beforeComponentAfter = afterComponent[0: int(arrayLimits[0])]
        afterComponentAfter = afterComponent[int(arrayLimits[1]):len(afterComponent)]
    qAfterBistoNumOrTypeR(beforeComponentAfter)
    if main.isAA or main.isA1A or main.isA or main.isCardinal or main.isSpace:
        # print("Cardinal", main.isCardinal)
        # print("A", main.isA)
        # print("AA", main.isAA)
        # print("A1A", main.isA1A)
        # print("Space", main.isSpace)
        main.outPut = main.outPut + '0'
        main.isA = False
        main.isAA = False
        main.isA1A = False
        main.isCardinal = False
        qNumb(afterComponentAfter, address)
    else:
        main.outPut = main.outPut + '1'
        print(main.outPut)
        print("Cadena no valida afterbis")
        sys.exit(1)


def qbis(beforeComponent, afterComponent, address2):
    re.compile(main.patternA)
    re.compile(main.patternB)
    re.compile(main.patternC)
    qBeforeBisNum(beforeComponent)
    if main.isAlphanumeric:
        main.outPut = main.outPut + "0"
        if main.isA or main.isAA or main.isA1A:
            main.outPut = main.outPut + "0"
            main.isA = False
            main.isAA = False
            main.isA1A = False
            main.isNumber = False
            main.isAlphanumeric = False
            qvalidateAfterBis(afterComponent, address2)
        else:
            main.isA = False
            main.isAA = False
            main.isA1A = False
            main.isNumber = False
            main.isAlphanumeric = False
            qvalidateAfterBis(afterComponent, address2)
    else:
        main.outPut = main.outPut + '1'
        print(main.outPut)
        print("Cadena no valida bis")
        sys.exit(1)


def q10(address, pos):
    print(address)
    re.compile(main.patternA)
    re.compile(main.patternB)
    re.compile(main.patternC)
    re.compile(main.patternDecimal)
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
                if main.isAccepted:
                    sys.exit(0)
            else:
                qNumb(afterComponent, address2)
                if main.isAccepted:
                    sys.exit(0)
    except:
        if main.isAccepted:
            main.isAccepted = False
            print("Dirección válida")
            print(main.outPut)
            #sys.exit(0)
        else:
            main.outPut = main.outPut + '1'
            print("Cadena no valida q10")
            print(main.outPut)
            sys.exit(1)



def validateTypeOfRoad(address):
    main.ADDRESS = address
    main.arrayRoadTypes = sorted(main.arrayRoadTypes, key=len, reverse=True)
    main.arrayComplement = sorted(main.arrayComplement, key=len, reverse=True)
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
