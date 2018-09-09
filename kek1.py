import string

print('Привет, мир!')

class RailRoadHedge():

    def NormilizeText(self,text):
        text = text.lower()
        text = text.replace(' ', '')
        return ''.join(c for c in text if c in string.ascii_letters)


    def Encode(self, key, E_text):

        # initializtion
        key_rez = key
        key_check = key
        flag = True
        i = 0
        k = 0
        encodemessage = ''
        while key_rez != 0:
            while k < len(E_text):

                if key_rez == key_check:
                    encodemessage += E_text[k]

                if key_check == 1:
                    flag = False

                if key_check == key:
                    flag = True

                if flag == True:
                    key_check = key_check - 1
                else:
                    key_check = key_check + 1

                # print('key_rez = ',key_rez,'key_check = ',key_check,'encode = ',encodemessage)
                # a = input()

                k += 1
            key_rez -= 1
            key_check = key_rez
            k = key - key_rez

        print(encodemessage)



    def Decode(self, key, D_text):

        def Distance(self, size, row, iteration):
            if ((size == 0) or (size == 1)):
                return 1

            if ((row == 0) or (row == size - 1)):
                return (size - 1) * 2

            if (iteration % 2 == 0):
                return (size - 1 - row) * 2

            return 2 * row

        if key < 0:
            print("Error")
        else:
            #print(len(D_text))
            decodedmessage = ''
            CurrPosition = 0
            row = 0
            word_list = list(D_text)
            while row < key:
                iter = 0
                i = row
                while i < len(D_text):
                   # print('i: ',i,'row: ', row,'iter: ', iter, CurrPosition,'list: ',word_list)
                   # word_list.insert(i, D_text[CurrPosition])
                    word_list[i] = D_text[CurrPosition]
                    CurrPosition +=1
                    i = i + Distance(self,key,row,iter)
                    iter += 1
                   # print('i: ', i, 'row: ', row, 'iter: ', iter, CurrPosition,'list: ',word_list)
                   # a = input()
                row += 1
            for letter in word_list:
                decodedmessage += letter

            print(decodedmessage)






kek = RailRoadHedge()
a = input('Enter text: ')
b = int(input('Enter key: '))
kek.Encode(b, kek.NormilizeText(a))
c = input('Enter d.text: ')
kek.Decode(b, c)


