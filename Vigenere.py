import string



class Vigenere():

    def NormilizeText(self, N_text):

        kek = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
        kek = set(kek)

        N_text = N_text.lower()
        N_text = N_text.replace(' ', '')
        text = ''
        for letter in N_text:
            if letter in kek:
                #print(letter)
                text += letter
        #print(text)

        return text



    def encrypt(self, key, plaintext): # ё = 1105
        alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        i = 0
        while len(key) <= len(plaintext):
            key += alph[(alph.index(key[i]) + 1) % 33]
            i += 1
        print(key)

        ciphered = ''
        for indx, chplain in enumerate(plaintext):
            #print(indx)
            ciphered += alph[(alph.index(chplain)+alph.index(key[indx])) % 32]
           # print(ciphered)
          #  a = input()

        return ciphered


    def decrypt(self, key, ciphertext):
        alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        deciphered = ''
        i = 0
        while len(key) <= len(ciphertext):
            key += alph[(alph.index(key[i]) + 1) % 33]
            i += 1
        for indx, plain in enumerate(ciphertext):

            deciphered += alph[(alph.index(plain) - alph.index(key[indx]) + 32) % 32]


        return deciphered


