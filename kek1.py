import string

print('Привет, мир!')

class RailRoadHedge():

    def Encode(self, key, E_text):
        E_text = E_text.lower()
        E_text = E_text.replace(' ', '')
        for letter in E_text:
            if not(letter in string.ascii_lowercase):
                E_text.replace(letter,'')
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

        D_text = D_text.lower()
        D_text = D_text.replace(' ', '')
        #for letter in D_text:
        #    if not (letter in string.ascii_lowercase):
        #        D_text.replace(letter, '')
        # initializtion
        key_rez = key
        decodedmessage = ''
        coef = 0
        i = 0
        while key_rez != 0:
            count = len(D_text) // key_rez
            while i != count:
                decodedmessage += D_text[i]
                print(i)
                i += 1;
            key_rez -= 1

        print(decodedmessage)






kek = RailRoadHedge()
a = input('Enter text: ')
b = int(input('Enter key: '))
kek.Encode(b, a)
c = input('Enter d.text: ')
kek.Decode(b, c)


