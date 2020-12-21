from tkinter import*
from PIL import Image, ImageTk
from googletrans import Translator

count = 0

def clear():
    box_top.delete(1.0, END)
    box_bottom.delete(1.0, END)

def translate():
    if count % 2 == 0:
        INPUT = box_top.get(1.0, END)
        t = Translator()
        a = t.translate(INPUT, dest = 'en', src = 'vi')
        b = a.text
        box_bottom.insert(END, b)
    else :
        INPUT = box_top.get(1.0, END)
        t = Translator()
        a = t.translate(INPUT, dest = 'vi', src = 'en')
        b = a.text
        box_bottom.insert(END, b)

def switch():
    global count
    count += 1;

if __name__ == "__main__":
    scr = Tk()
    scr.title('JackyD - Ecosystem: Translator')
    scr.geometry('500x600')
    scr.iconbitmap('logo.ico')

    load = Image.open('background.png')
    render =ImageTk.PhotoImage(load)
    img = Label(scr, image = render)
    img.place(x = 0, y = 0)

    name = Label(scr, text = 'Jacky Trans', fg = '#000000', bd = 0, bg = '#FFDB83')
    name.config(font = ('Transformers Movie', 30))
    name.pack(pady = 10)

    box_top = Text(scr, width = 20, height = 4, font = ('ROBOTO', 16))
    box_top.pack(pady = 50)
    box_bottom = Text(scr, width = 20, height = 4, font = ('ROBOTO', 16))
    box_bottom.pack(pady = 10)

    button_frame = Frame(scr).pack(side = BOTTOM)



    clear_button = Button(button_frame, text = 'clear text', font = (('Arial'),10,'bold'), bg = '#303030', fg = '#FFFFFF', command = clear)
    clear_button.place(x = 150, y = 500)
    trans_button = Button(button_frame, text = 'Translate', font = (('Arial'),10,'bold'), bg = '#303030', fg = '#FFFFFF', command = translate)
    trans_button.place(x = 290, y = 500)
    transfer_button = Button(button_frame, text = 'switch', font = (('Arial'),10,'bold'), bg = '#303030', fg = '#FFFFFF', command = switch)
    transfer_button.place(x = 220, y = 240)

    mainloop()
