import tkinter
import Files
import PIL.Image
import PIL.ImageTk
from Vigenere import Vigenere
from RailWay import RailRoadHedge


def cipherRail(key):
    key = int(key)
    kek = RailRoadHedge()
    text = Files.ReadFromFile()
    Files.WriteInFile(kek.Encode(key, kek.NormilizeText(text)))


def DechipherRail(key):
    kek = RailRoadHedge()
    text = Files.ReadFromFile()
    Files.WriteInFile(kek.Decode(key, text))

def cipherVig(key):
    #key = int(key)
    key = str(key)
    kek = Vigenere()
    text = Files.ReadFromFile()
    print('text:',kek.NormilizeText(text),'key:',key)
    #a = input()

    Files.WriteInFile(kek.encrypt(key, kek.NormilizeText(text)))

def dechipherVig(key):
    key = str(key)
    kek = Vigenere()
    text = Files.ReadFromFile()
    Files.WriteInFile(kek.decrypt(key, kek.NormilizeText(text)))



def MakeImage(path):

    im = PIL.Image.open(path)
    photo = PIL.ImageTk.PhotoImage(im)
    label = tkinter.Label(Main_Window, image=photo, width=320, height=320)
    label.image = photo  # keep a reference!
    label.place(x=650, y=280)


def MakeMainWindow():

    var = tkinter.IntVar()
    rbutton1 = tkinter.Radiobutton(Main_Window, text=b' Rail Road Hedge. ', height=1, font='20', variable=var, value=1)
    rbutton1.place(x = 600, y = 600)
    #print(var.get())
    rbutton2 = tkinter.Radiobutton(Main_Window, text=b' Chiffre de Vigenere. ',height=1, font='20', variable=var, value=2)
    rbutton2.place(x = 600, y = 650)
    rbutton3 = tkinter.Radiobutton(Main_Window, text=b' Playfair cipher. ',height=1, font='20' , variable=var, value=3)
    rbutton3.place(x = 600, y = 700)


    Button_Main = tkinter.Button(Main_Window, text='Lets go!',bg = 'Dodger Blue', fg = 'White', command = (lambda : NewWindow(Main_Window,rbutton3,rbutton2,rbutton1,label,Button_Main, var)))
    Button_Main.place(x=730, y=760)

    # Images

    path = "/home/alexey/Документы/kek2.png"
    im = PIL.Image.open(path)
    photo = PIL.ImageTk.PhotoImage(im)
    label = tkinter.Label(Main_Window, image=photo, width=320, height=320)
    label.image = photo  # keep a reference!
    label.place(x=650, y=280)


def Choose(count, entry, m):
    count = int(count)

    if count == 1 and m == 'c':
        cipherRail(entry)
    if count == 1 and m == 'd':
        DechipherRail(entry)
    if count == 2 and m == 'c':
        cipherVig(entry)
    if count == 2 and m == 'd':
        dechipherVig(entry)
    if count == 3:
        return 0;





def NewWindow(window,rb3,rb2,rb1,img,butt,var):

    def Hide(lbl1,ent1,buttm,buttb,buttd):
        lbl1.place_forget()
        ent1.place_forget()
        buttm.place_forget()
        buttb.place_forget()
        buttd.place_forget()
        MakeMainWindow()

    print(var.get())

    # clear window
    rb1.place_forget()
    rb2.place_forget()
    rb3.place_forget()
    img.place_forget()
    butt.place_forget()

    # new

    Label_1 = tkinter.Label(window, text='Enter key here: ')
    Label_1.place(x=700, y=600)


    Key = tkinter.IntVar()
    Entry_1 = tkinter.Entry(window, textvariable=Key)
    Entry_1.configure(width = 20)
    Entry_1.place(x=635, y=650)

    kek = Entry_1.get()
    print(kek)
     # Buttons
    Button_Main = tkinter.Button(window, text='Lets chiphre!',bg = 'Dodger Blue', fg = 'White', width = 14, command = (lambda : Choose(var.get(),Entry_1.get(),'c')))
    Button_Main.place(x=635, y=700)
    print('kek')

    Button_Dechipher = tkinter.Button(window, text='Lets Dechiphre!', bg='Dodger Blue', fg='White', width=19, command=(lambda: Choose(var.get(),Entry_1.get(),'d')))
    Button_Dechipher.place(x=635, y=750)

    Button_Back = tkinter.Button(window,  text='Back',bg = 'Dodger Blue', fg = 'White',width=4, command = (lambda  :  Hide(Label_1,Entry_1,Button_Main,Button_Back,Button_Dechipher)))
    Button_Back.place(x=890, y=700)

    path = "/home/alexey/Документы/kek2.png"
    im = PIL.Image.open(path)
    photo = PIL.ImageTk.PhotoImage(im)
    label = tkinter.Label(Main_Window, image=photo, width=320, height=320)
    label.image = photo  # keep a reference!
    label.place(x=650, y=280)




#GUI
Main_Window = tkinter.Tk()
Main_Window.geometry('1600x1000')
Main_Window.title('Easy chiphers')

# RadioButtons

MakeMainWindow()


#end of code
Main_Window.mainloop()


