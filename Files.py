def ReadFromFile():
    from tkinter.filedialog import askopenfilename

    filename = askopenfilename()

    text = ''
    file = open(filename, 'r')
    for str in file:
        text += str

    return text

def WriteInFile(text):

    from tkinter.filedialog import askopenfilename

    filename = askopenfilename()
    file = open(filename, 'w')

    file.write(text)



