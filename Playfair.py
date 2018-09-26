import string
import re


class Playfair():

    def NormilizeText(self, text):


        text = text.upper()
        text = text.replace(' ', '')
        return ''.join(c for c in text if c in string.ascii_letters)

    def encryptDecrypt(self, mode, message, final=""):
        kek = False
        addSymbol = 'X'
        message = list(message)

        def regular(text):
            template = r"[A-Z]{2}"
            return re.findall(template, text)

        matrixKey = [

            ['C', 'R', 'Y', 'P', 'T'],
            ['O', 'G', 'A', 'H', 'B'],
            ['D', 'E', 'F', 'I', 'K'],
            ['L', 'M', 'N', 'Q', 'S'],
            ['U', 'V', 'W', 'X', 'Z']
        ]

        if mode == 'c':

            for index in range(len(message)):

                if message[index] == 'J':
                    message[index] = 'I'

            for index in range(1, len(message)):

                if message[index] == message[index - 1]:
                    message.insert(index, addSymbol)

            if len(message) % 2 != 0:
                message.append(addSymbol)

        binaryList = regular("".join(message))

        for binary in range(len(binaryList)):

            binaryList[binary] = list(binaryList[binary])
            for indexString in range(len(matrixKey)):

                for indexSymbol in range(len(matrixKey[indexString])):

                    if binaryList[binary][0] == matrixKey[indexString][indexSymbol]:
                        y0, x0 = indexString, indexSymbol

                    if binaryList[binary][1] == matrixKey[indexString][indexSymbol]:
                        y1, x1 = indexString, indexSymbol

            for indexString in range(len(matrixKey)):

                if matrixKey[y0][x0] in matrixKey[indexString] and matrixKey[y1][x1] in matrixKey[indexString]:
                    kek = True
                    if mode == 'c':
                        x0 = x0 + 1 if x0 != 4 else 0
                        x1 = x1 + 1 if x1 != 4 else 0
                    else:
                        x0 = x0 - 1 if x0 != 0 else 4
                        x1 = x1 - 1 if x1 != 0 else 4

            if x0 == x1:
                if mode == 'c':
                    y0 = y0 + 1 if y0 != 4 else 0
                    y1 = y1 + 1 if y1 != 4 else 0
                else:
                    y0 = y0 - 1 if y0 != 0 else 4
                    y1 = y1 - 1 if y1 != 0 else 4

            y0, y1 = y1, y0

            if kek == True:
                binaryList[binary][0] = matrixKey[y0][x0]
                binaryList[binary][1] = matrixKey[y1][x1]
                kek = False
            else:
                binaryList[binary][1] = matrixKey[y0][x0]
                binaryList[binary][0] = matrixKey[y1][x1]

        for binary in range(len(binaryList)):
            for symbol in binaryList[binary]:
                final += symbol
        return final



