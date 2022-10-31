import re
import sys

arrayTypeOfStartVer = ['CORREGIMIENTO', 'CARRETERA', 'KILOMETRO',
                 'MUNICIPIO',	'HACIENDA',	'VARIANTE',	'ENTRADA',
                 'CAMINO',	'BARRIO',	'PREDIO',	'SECTOR',	'VEREDA',
                 'FINCA', 'VIA',	'CARR',	'CASA',	'CORR',	'LOTE',	'BRR',	'FCA', 'KR',
                 'MCP',	'SEC',	'VTE',	'VDA',	'VRD',	'VIA',	'CN',	'CT',
                 'CA',	'CS',	'BR',	'EN',	'FI',	'HC',	'KM',
                 'PD',	'LT',	'SC',	'VT',	'VI']

arrayComplementVer = ['HACIENDA', 'ENTRADA', 'CAMINO',	'BARRIO',	'PREDIO',	'SECTOR',	'VEREDA',
                 'FINCA', 'CASA', 'PARCELA', 'LOTE']


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
    global arrayNumeralV
    global arrayRoadTypesNoneTwoWords
    arrayNumeralV = sorted(arrayNumeralV, key=len, reverse=True)
    arrayRoadTypesNoneTwoWords = sorted(arrayRoadTypesNoneTwoWords, key=len, reverse=True)
    posBis1 = address.find(bis)
    posNumb = -1
    posTypeRoad = -1
    strComp = ''
    strTypeR = ''
    res = ''
    for i in arrayNumeralV:
        if address.find(i) != -1:
            posNumb = address.find(i)
            strComp = i
            break
    for i in arrayRoadTypesNoneTwoWords:
        if address.find(i) != -1:
            if i != ADDRESS[0:(len(ADDRESS) - len(address)) - 1]:
                posTypeRoad = address.find(i)
                strTypeR = i
                break
            else:
                break
    if not re.search("|".join(arrayRoadTypes), address[posTypeRoad+len(strTypeR):len(address)]) and not re.search("|".join(arrayNumeralV), address[posTypeRoad+len(strTypeR):len(address)]):
        if posBis1 != -1 and posNumb != -1 and posBis1 < posNumb:
            res = str(posBis1) + " " + str(len(bis) + posBis1) + " " + bis
            return res
        elif posBis1 != -1 and posNumb != -1 and posBis1 > posNumb:
            res = str(posNumb) + " " + str(len(strComp) + posNumb) + " " + strComp
            return res
        elif posBis1 == -1 and posNumb != -1:
            res = str(posNumb) + " " + str(len(strComp) + posNumb) + " " + strComp
            return res
        elif posBis1 != -1 and posNumb == -1 and posTypeRoad == -1:
            res = str(posBis1) + " " + str(len(bis) + posBis1) + " " + bis
            return res
        elif posBis1 == -1 and posNumb == -1 and posTypeRoad != -1:
            res = str(posTypeRoad) + " " + str(len(strTypeR) + posTypeRoad) + " " + strTypeR
            return res
        elif posBis1 != -1 and posTypeRoad != -1 and posTypeRoad < posBis1:
            res = str(posTypeRoad) + " " + str(len(strTypeR) + posTypeRoad) + " " + strTypeR
            return res
        elif posBis1 != -1 and posTypeRoad != -1 and posTypeRoad > posBis1:
            res = str(posBis1) + " " + str(len(bis) + posBis1) + " " + bis
            return res
        else:
            res = res + '-1'
            return res
    else:
        res = res + '-1'
        return res



def isCardinalValidate(address):
    global isCardinal
    re.compile(patternCardinal)
    isCardinal = True if re.search(patternCardinal, address) else False


def formatRefexRes(value):
    value = str((value.span())).replace("(", "")
    value = value.replace(")", "")
    value = value.replace(",", "")
    return value.split()


def qAfterBistoNumOrTypeR(afterComponent):
    global isSpace
    global isCardinal
    global isA
    global isAA
    global isA1A
    isCardinalValidate(afterComponent)
    if afterComponent is None or len(afterComponent) == 0:
        isSpace = True
    else:
        if isCardinal:
            posCardinal = formatRefexRes(re.search(patternCardinal, afterComponent))
            afterComponent = afterComponent[0:int(posCardinal[0])]
        if afterComponent[0] == ' ' and len(afterComponent) > 1:
            afterComponent = afterComponent[1:len(afterComponent)]
        if afterComponent[len(afterComponent) - 1] == ' ':
            afterComponent = afterComponent[0:len(afterComponent) - 1]
        if re.search(patternA, afterComponent):
            val = formatRefexRes(re.search(patternA, afterComponent))
            back = afterComponent[int(val[0]) - 1]
            if (48 <= ord(back) <= 57) and len(afterComponent) < 1 or back == " " or back == "":
                isA = True
            else:
                if afterComponent[0] == ' ':
                    qAfterBistoNumOrTypeR(afterComponent)
                else:
                    isA = True
                    if re.search(patternB, afterComponent):
                        isAA = True
                        isA = False
                    if re.search(patternC, afterComponent):
                        isA1A = True
                        isA = False
                        isAA = False

        else:
            if afterComponent == "" or afterComponent == " ":
                isSpace = True


def qBeforeBisNum(beforeComponent):
    global outPut
    global isSpace
    global isCardinal
    global isA
    global isAA
    global isA1A
    global isAlphanumeric
    global isNumber
    if beforeComponent[len(beforeComponent) - 1] == ' ':
        beforeComponent = beforeComponent[0:len(beforeComponent) - 1]
    if re.search(patternC, beforeComponent):
        val = str(re.search(patternC, beforeComponent).span()).replace("(", "")
        val = val.replace(")", "")
        val = val.replace(",", "")
        val = val.split()
        beforeComponent = beforeComponent[0: (int(val[0]))]
        isA1A = True
        if re.search("(\\d|\w)", beforeComponent):
            isAlphanumeric = True
        elif re.search("(\\d)", beforeComponent):
            isNumber = True
        else:
            outPut = outPut + '1'
            print(outPut)
            print("Cadena no valida BeforeBis1")
    elif re.search(patternB, beforeComponent):
        val = str(re.search(patternB, beforeComponent).span()).replace("(", "")
        val = val.replace(")", "")
        val = val.replace(",", "")
        val = val.split()
        beforeComponent = beforeComponent[0: int(val[0]) - 1]
        isAA = True
        if re.search("(\\d|\w)", beforeComponent):
            isAlphanumeric = True
        elif re.search("(\\d)", beforeComponent):
            isNumber = True
        else:
            outPut = outPut + '1'
            print(outPut)
            print("Cadena no valida")
    elif re.search(patternA, beforeComponent):
        val = str(re.search(patternA, beforeComponent).span()).replace("(", "")
        val = val.replace(")", "")
        val = val.replace(",", "")
        val = val.split()
        back = beforeComponent[int(val[0]) - 1]
        if (48 <= ord(back) <= 57) or back == " ":
            isA = True
            isAlphanumeric = True
        else:
            if re.search("(\\d|\w)", beforeComponent):
                isAlphanumeric = True
            elif re.search("(\\d)", beforeComponent):
                isNumber = True
            else:
                outPut = outPut + '1'
                print(outPut)
                print("Cadena no valida")
    else:
        if re.search("(\\d|\w)", beforeComponent):
            isAlphanumeric = True
        elif re.search("(\\d)", beforeComponent):
            isNumber = True
        else:
            outPut = outPut + '1'
            print(outPut)
            print("Cadena no valida beforeBis")


def zerosAmount(val):
    count = 0
    for i in val:
        if i == " ":
            count += count
    return count


def complement(value):
    global isComplement
    for i in arrayComplement:
        if value.find(i) != 1:
            isComplement = True
            break


def qNumb(afterComponent, address):
    global outPut
    global isSpace
    global isCardinal
    global isA
    global isAA
    global isA1A
    global isAlphanumeric
    global isNumber
    global isAccepted
    s = [int(s) for s in re.findall(r'-?\d+\.?\d*', afterComponent)]
    for i in s:
        if str(i).startswith("-") and len(s) > 2:
            s.remove(i)
    afterComponentAux = afterComponent.replace(" ", "")
    if s[1] < 0:
        s[1] = s[1]*(-1)
    posNumb1 = afterComponent.index(str(s[0]))
    posNum2 = afterComponent.index(str(s[1]))
    isCardinalValidate(afterComponent[posNumb1:posNum2])
    if not isCardinal:
        if len(s) == 2:
            # print("pos", afterComponent[posNumb1], "pos2", afterComponent[posNum2+1])
            if afterComponent[posNum2] == "-":
                posNum2 = posNum2 + 1
            afterBetweenNumbs = afterComponent[posNumb1:posNum2]
            posNextComponent = whatComponentIsNext(afterBetweenNumbs)
            posNextComponent = posNextComponent.split()
            for i in arrayRoadTypes:
                if len(posNextComponent) > 1 and posNextComponent[2] == i:
                    conditionAfterNumber = True
                    break
            if re.search(patternDecimal, afterComponentAux):
                posNumbs = formatRefexRes(re.search(patternDecimal, afterComponentAux))
                posStart = int(posNumbs[1]) + zerosAmount(afterComponent) + 2
                afterComponent = afterComponent[posStart: len(afterComponent)]
                if len(posNextComponent) > 1 and posNextComponent[2] == bis:
                    outPut = outPut + '0'
                if len(afterComponent) == 0:
                    outPut = outPut + '0'
                    isAccepted = True
                else:
                    isCardinalValidate(afterComponent)
                    complement(afterComponent)
                    if isCardinal:
                        val = str(re.search(patternCardinal, afterComponent).span()).replace("(", "")
                        val = val.replace(")", "")
                        val = val.replace(",", "")
                        val = val.split()
                        afterComponent = afterComponent[int(val[1]):len(afterComponent)]
                        if len(afterComponent) > 0:
                            if isComplement:
                                outPut = outPut + '00'
                                isAccepted = True
                        else:
                            outPut = outPut + '0'
                            isAccepted = True
                    if isComplement:
                        outPut = outPut + '0'
                        isAccepted = True


            else:
                patternA = "(([A-Z]){1})"
                patternB = "([A-Z]){1}(\s|\-){1}([A-Z]){1}"
                patternC = "([A-Z]){1}(\s|\-){1}(\d)(\s|\-){1}([A-Z]){1}"
                re.compile(patternA), re.compile(patternB), re.compile(patternC)
                if afterComponent[posNum2] == "-":
                    posNum2 = posNum2 + 1
                afterComponentD = afterComponent[posNumb1:posNum2]
                posBis = afterComponentD.find(bis)
                afterComponentD = afterComponentD.replace(" ", "")
                qAfterBistoNumOrTypeR(afterComponent)
                isCardinalValidate(afterComponent)
                if afterBetweenNumbs.find(bis) != -1:
                    if 90 <= ord(afterComponentD[posBis]) <= 65:
                        outPut = outPut + "1"
                        isAccepted = False
                    else:
                        outPut = outPut + '0'
                        isAccepted = True
                if isA or isAA or isA1A and not conditionAfterNumber:
                    if posBis != -1:
                        if 90 <= ord(afterComponentD[posBis + 2]) <= 65:
                            outPut = outPut + "1"
                            isA = False
                            isAA = False
                            isA1A = False
                            isAccepted = False
                        else:
                            outPut = outPut + '0'
                            isA = False
                            isAA = False
                            isA1A = False
                            isAccepted = True
                    else:
                        outPut = outPut + '0'
                        isA = False
                        isAA = False
                        isA1A = False
                        isAccepted = True
                else:
                    if conditionAfterNumber:
                        outPut = outPut + '1'
                        isAccepted = False
                        conditionAfterNumber = False
                        print("Dirección no valida")
                        print(outPut)
                    if afterBetweenNumbs.find(bis) != -1:
                        outPut = outPut + '0'
                        isAccepted = True
        else:
            indexSecondNumb = afterComponent.index(str(s[1]))
            indexThirdNumb = afterComponent.index(str(s[2]))
            if indexThirdNumb > indexSecondNumb:
                afterComponent = afterComponent[indexSecondNumb:len(afterComponent)]
                if re.search('|'.join(arrayComplement), afterComponent):
                    val = str(re.search('|'.join(arrayComplement), afterComponent).span())
                    val = val.replace("(", "")
                    val = val.replace(")", "")
                    val = val.replace(",", "")
                    val = val.split()
                    if indexThirdNumb > int(val[1]):
                        outPut = outPut + '0'
                        isAccepted = True
                    else:
                        outPut = outPut + '1'
                        isAccepted = False
            else:
                isAccepted = False
                outPut = outPut + '1'
    else:
        outPut = outPut + '1'
        isAccepted = False
        isCardinal = False
        print(outPut)
        print("Cadena no valida")


def qvalidateAfterBis(afterComponent, address):
    global outPut
    global isSpace
    global isCardinal
    global isA
    global isAA
    global isA1A
    global isAlphanumeric
    global isNumber
    global isAccepted
    posAfterComponent = whatComponentIsNext(afterComponent)
    arrayLimits = posAfterComponent.split()
    if arrayLimits[0] == arrayLimits[1]:
        beforeComponentAfter = afterComponent[0: int(arrayLimits[0])]
        afterComponentAfter = afterComponent[int(arrayLimits[1]) + 1:len(afterComponent)]
    else:
        beforeComponentAfter = afterComponent[0: int(arrayLimits[0])]
        afterComponentAfter = afterComponent[int(arrayLimits[1]):len(afterComponent)]
    qAfterBistoNumOrTypeR(beforeComponentAfter)
    if isAA or isA1A or isA or isCardinal or isSpace:
        # print("Cardinal", isCardinal)
        # print("A", isA)
        # print("AA", isAA)
        # print("A1A", isA1A)
        # print("Space", isSpace)
        outPut = outPut + '0'
        isA = False
        isAA = False
        isA1A = False
        isCardinal = False
        qNumb(afterComponentAfter, address)
    else:
        outPut = outPut + '1'
        print(outPut)
        print("Cadena no valida afterbis")


def qbis(beforeComponent, afterComponent, address2):
    global outPut
    global isSpace
    global isCardinal
    global isA
    global isAA
    global isA1A
    global isAlphanumeric
    global isNumber
    global isAccepted
    re.compile(patternA)
    re.compile(patternB)
    re.compile(patternC)
    qBeforeBisNum(beforeComponent)
    if isAlphanumeric:
        outPut = outPut + "0"
        if isA or isAA or isA1A:
            outPut = outPut + "0"
            isA = False
            isAA = False
            isA1A = False
            isNumber = False
            isAlphanumeric = False
            qvalidateAfterBis(afterComponent, address2)
        else:
            isA = False
            isAA = False
            isA1A = False
            isNumber = False
            isAlphanumeric = False
            qvalidateAfterBis(afterComponent, address2)
    else:
        outPut = outPut + '1'
        print(outPut)
        print("Cadena no valida bis")


def q10(address, pos):
    global outPut
    global isSpace
    global isCardinal
    global isA
    global isAA
    global isA1A
    global isAlphanumeric
    global isNumber
    global isAccepted
    re.compile(patternA)
    re.compile(patternB)
    re.compile(patternC)
    re.compile(patternDecimal)
    try:
        address2 = address[pos + 1: (len(address))] if address[pos + 1] == " " else address[pos: (len(address))]
        address2 = address2[1:len(address)] if address2[0] == ' ' else address2[0:len(address)]
        posNextComponent = whatComponentIsNext(address2)
        if len(posNextComponent) == 2:
            outPut = outPut + '1'
            print("Cadena no valida q10")
            print(outPut)
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
                if isAccepted:
                    sys.exit(0)
            else:
                qNumb(afterComponent, address2)
                if isAccepted:
                    sys.exit(0)
    except:
        if isAccepted:
            isAccepted = False
            print("Dirección válida")
            print(outPut)
            #sys.exit(0)
        else:
            outPut = outPut + '1'
            print("Cadena no valida q10")
            print(outPut)


def vereda(address, pos, direcV):
    global outPut
    global isSpace
    global isCardinal
    global isA
    global isAA
    global isA1A
    global isAlphanumeric
    global isNumber
    global isAccepted
    global isComplement
    try:
        if direcV == "VIA" or direcV == "VI" or direcV == "KM" or direcV == "KILOMETRO" or direcV == "VARIANTE" or direcV == "VT" or direcV == "CARRETERA" or direcV == "CARR" or direcV == "KR":
            afterRoad = address[len(direcV):len(address)]
            if afterRoad[0] == " ":
                afterRoad = afterRoad[1:len(afterRoad)]
                s = [int(s) for s in re.findall(r'-?\d+\.?\d*', afterRoad)]
            if len(s) >= 1:
                posFirstNumber = afterRoad.index(str(s[0]))
                posSecondNumber = s[1] if len(s) >= 2 else None
                if posSecondNumber is not None:
                    complement(afterRoad[posFirstNumber:posSecondNumber])
                    if isComplement:
                        val = str(re.search("|".join(arrayComplementVer),
                                            afterRoad[posFirstNumber:posSecondNumber]).span())
                        val = val.replace("(", "")
                        val = val.replace(")", "")
                        val = val.replace(",", "")
                        val = val.split()
                        if re.search("(\w|\\d)", afterRoad[int(val[1]):posSecondNumber]):
                            outPut = outPut + '00'
                            isComplement = False
                            print(outPut)
                            print("Direccion rural correcta")
                        else:
                            outPut = outPut + '1'
                            isComplement = False
                            print(outPut)
                            print("Direccion rural incorrecta")
                    else:
                        outPut = outPut + '1'
                        isComplement = False
                        print(outPut)
                        print("Direccion rural incorrecta")
                else:
                    complement(afterRoad)
                    if isComplement:
                        val = str(
                            re.search("|".join(arrayComplementVer),
                                      afterRoad[posFirstNumber:posSecondNumber]).span())
                        val = val.replace("(", "")
                        val = val.replace(")", "")
                        val = val.replace(",", "")
                        val = val.split()
                        if re.search("(\w|\\d)", afterRoad[int(val[1]):posSecondNumber]):
                            outPut = outPut + '00'
                            isComplement = False
                            print(outPut)
                            print("Direccion rural correcta")
                        else:
                            outPut = outPut + '1'
                            isComplement = False
                            print(outPut)
                            print("Direccion rural incorrecta")
        else:
            if re.search("|".join(arrayComplementVer), address):
                val = str(re.search("|".join(arrayComplementVer), address).span())
                val = val.replace("(", "")
                val = val.replace(")", "")
                val = val.replace(",", "")
                val = val.split()
                afterComplement = address[int(val[1]):len(address)]
                if re.search("(\w|\\d)", afterComplement):
                    outPut = outPut + '00'
                    isComplement = False
                    print(outPut)
                    print("Direccion rural correcta")
                else:
                    outPut = outPut + '1'
                    isComplement = False
                    print(outPut)
                    print("Direccion rural incorrecta")
            else:
                outPut = outPut + '1'
                isComplement = False
                print(outPut)
                print("Direccion rural incorrecta")

    except:
        outPut = outPut + '1'
        isComplement = False
        print(outPut)
        print("Direccion rural incorrecta")


def validateTypeOfRoad(address):
    global arrayRoadTypes
    global arrayComplement
    global arrayComplementVer
    global ADDRESS
    global outPut
    print(address)
    ADDRESS = address
    arrayRoadTypes = sorted(arrayRoadTypes, key=len, reverse=True)
    arrayComplement = sorted(arrayComplement, key=len, reverse=True)
    arrayComplementVer = sorted(arrayComplementVer, key=len, reverse=True)
    pattern = r'\s+'
    addressPiv = re.sub(pattern, '', address)
    direc = ""
    direcV = ""
    for i in arrayRoadTypes:
        if address.startswith(i) or addressPiv.startswith(i):
            direc += i
            break
    if re.search('|'.join(arrayTypeOfStartVer), address) or re.search('|'.join(arrayTypeOfStartVer), direc):
        for i in arrayTypeOfStartVer:
            if address.startswith(i) or addressPiv.startswith(i):
                direcV = i
                break
    if len(direc) > 1:
        if len(direcV) > 1:
            outPut = '0'
            pos = whatComponentIsNext(address[len(direcV):len(address)])
            if pos == '-1':
                vereda(address, len(direcV), direcV)
            else:
                outPut = '0'
                q10(address, len(direc))
        else:
            outPut = '0'
            q10(address, len(direc))
    else:
        if len(direcV) > 1:
            outPut = '0'
            vereda(address[len(direcV):len(address)], len(direcV), direcV)
        else:
            outPut = outPut + '1'
            print("Cadena no valida q10")
            print(outPut)



def traverseString(arrayAddresses):
    for i in arrayAddresses:
        validateTypeOfRoad(i)


def run():
    fileName = input()
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
