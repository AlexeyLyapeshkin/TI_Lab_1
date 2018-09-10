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




