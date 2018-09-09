import tkinter
import Files
import PIL.Image
import PIL.ImageTk
from RailWay import RailRoadHedge


def cipher(key):
    key = int(key)
    kek = RailRoadHedge()
    text = Files.ReadFromFile()
    Files.WriteInFile(kek.Encode(key, kek.NormilizeText(text)))


def Dechipher(key):
    kek = RailRoadHedge()
    text = Files.ReadFromFile()
    Files.WriteInFile(kek.Decode(key, text))

def MakeImage(path):

    im = PIL.Image.open(path)
    photo = PIL.ImageTk.PhotoImage(im)
    label = tkinter.Label(Main_Window, image=photo, width=320, height=320)
    label.image = photo  # keep a reference!
    label.place(x=650, y=280)


def MakeMainWindow():

    var = tkinter.IntVar()
    rbutton1 = tkinter.Radiobutton(Main_Window, text=b' RAILROAD HEDGE CHIPHER. ', variable=var, value=1)
    rbutton1.place(x = 600, y = 600)
    rbutton2 = tkinter.Radiobutton(Main_Window, text=u" ", variable=var, value=2)
    rbutton2.place(x = 600, y = 650)
    rbutton3 = tkinter.Radiobutton(Main_Window, text=u'3', variable=var, value=3)
    rbutton3.place(x = 600, y = 700)


    Button_Main = tkinter.Button(Main_Window, text='Lets go!',bg = 'Dodger Blue', fg = 'White', command = (lambda : NewWindow(Main_Window,rbutton3,rbutton2,rbutton1,label,Button_Main)))
    Button_Main.place(x=730, y=750)

    # Images

    path = "/home/alexey/Документы/kek2.png"
    im = PIL.Image.open(path)
    photo = PIL.ImageTk.PhotoImage(im)
    label = tkinter.Label(Main_Window, image=photo, width=320, height=320)
    label.image = photo  # keep a reference!
    label.place(x=650, y=280)







def NewWindow(window,rb3,rb2,rb1,img,butt):

    def Hide(lbl1,ent1,buttm,buttb):
        lbl1.place_forget()
        ent1.place_forget()
        buttm.place_forget()
        buttb.place_forget()
        MakeMainWindow()




    # clear window
    rb1.place_forget()
    rb2.place_forget()
    rb3.place_forget()
    img.place_forget()
    butt.place_forget()

    # new

    Label_1 = tkinter.Label(window, text='Enter key here: ')
    Label_1.place(x=20, y=20)
    Key = tkinter.IntVar()
    Entry_1 = tkinter.Entry(window, textvariable=Key)
    Entry_1.configure(width = 20)
    Entry_1.place(x=20, y=60)
    kek = Entry_1.get()
    print(kek)
                                 
    Button_Main = tkinter.Button(window, text='Lets chiphre!',bg = 'Dodger Blue', fg = 'White', command = (lambda : cipher(Entry_1.get())))
    Button_Main.place(x=400, y=60)
    print('kek')



    Button_Back = tkinter.Button(window,  text='Back',bg = 'Dodger Blue', fg = 'White', command = (lambda  :  Hide(Label_1,Entry_1,Button_Main,Button_Back)))
    Button_Back.place(x=900, y=700)






#GUI
Main_Window = tkinter.Tk()
Main_Window.geometry('1600x1000')
Main_Window.title('Easy chiphers')

# RadioButtons

MakeMainWindow()


#end of code
Main_Window.mainloop()


