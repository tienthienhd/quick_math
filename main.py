from tkinter import *
import time
import random
import math

from gtts import gTTS
from pygame import mixer  # Load the popular external library


window = Tk()
window.title("Phep cong ")
window.geometry('350x200')
window.resizable(height=True, width=True)
window.minsize(height=1000, width=1000)

label1 = Label(window, text="So ki tu trong moi phep tinh")
label1.grid(column=0, row=0)


def testVal(inStr, acttyp):
    if acttyp == '1':  # insert
        if not inStr.isdigit():
            return False
    return True


sokitu = Entry(window, validate="key", width=20)
sokitu.insert(0, "2")
sokitu['validatecommand'] = (sokitu.register(testVal), '%P', '%d')
sokitu.grid(column=1, row=0)

label2 = Label(window, text="So phep tinh")
label2.grid(column=0, row=1)
sopheptinh = Entry(window, validate="key", width=20)
sopheptinh.insert(0, "4")
sopheptinh['validatecommand'] = (sopheptinh.register(testVal), '%P', '%d')
sopheptinh.grid(column=1, row=1)

label3 = Label(window, text="Thoi gian hien thi")
label3.grid(column=0, row=2)
thoigian = Entry(window, validate="key", width=20)
thoigian.insert(0, "10")
thoigian['validatecommand'] = (thoigian.register(testVal), '%P', '%d')
thoigian.grid(column=1, row=2)

selected = IntVar()
rad1 = Radiobutton(window, text='Phep cong +', value=1, variable=selected)
rad2 = Radiobutton(window, text='Phep +-', value=2, variable=selected)
rad3 = Radiobutton(window, text='phep nhan *', value=3, variable=selected)
rad4 = Radiobutton(window, text='phep chia :', value=4, variable=selected)
rad1.grid(column=2, row=0)
rad2.grid(column=2, row=1)
rad3.grid(column=2, row=2)
rad4.grid(column=2, row=3)

frame = Frame(window)
frame.grid(column=1, row=12)
frame1 = Frame(window)
frame1.grid(column=1, row=12)

tile_frame = Label(frame, text="", font=("Times", "100", "bold"))
tile_frame.grid(column=1, row=13)

number_digit = {
    1: (1, 9),
    2: (10, 99),
    3: (100, 999),
    4: (1000, 9999),
    5: (10000, 99999),
    6: (100000, 999999),
    7: (1000000, 9999999),

}
n, m, k = None, None, None


def get_random_leter():
    global n, m, k
    n = int(sopheptinh.get())
    m = int(sokitu.get())
    k = int(thoigian.get())

    range_number = number_digit[m]
    tiles_letter = list(set([random.randint(*range_number) for _ in range(n)]))
    while len(tiles_letter) < n:
        k2 = list(set([random.randint(*range_number) for _ in range(n - len(tiles_letter))]))
        tiles_letter.extend(k2)
    return tiles_letter


tiles_letter, kq, current_n = None, None, 0

def read_number(number: int):
    audio = gTTS(text=str(number), lang="en", slow=False)
    audio.save("number.mp3")

    mixer.init()
    mixer.music.load('number.mp3')
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(0.5)


def show():
    global tiles_letter, kq, current_n
    tiles_letter = get_random_leter()
    print(tiles_letter)
    print(len(tiles_letter))
    kq = sum(tiles_letter)
    current_n = 0

    def add_letter():
        global current_n
        if not tiles_letter or current_n > n:
            return

        rand = random.choice(tiles_letter)
        read_number(rand)
        tile_frame.config(text=f"{rand}", fg="black", font=("Times", "100", "bold"))
        window.after(math.trunc(k * 1000 / n), add_letter)
        tiles_letter.remove(rand)

        current_n += 1

    print("call show")

    window.after(0, add_letter)
    window.after(k * 1000, xoadulieu)


def xoadulieu():
    tile_frame.config(text="")


def ketqua():
    tile_frame.config(text=kq, fg="red", font=("Times", "100", "bold"))


def clear():
    xoadulieu()


def pheptinh():
    if selected.get() != 0:
        hienthi.config(text=selected.get())


batdaubt = Button(window, text='Bat dau', bg="green", command=show)
batdaubt.grid(column=0, row=8)

ketquabt = Button(window, text='Ket qua', bg="green", command=ketqua)
ketquabt.grid(column=0, row=9)

xoabt = Button(window, text='Xoa', bg="green", command=clear)
xoabt.grid(column=0, row=10)

window.mainloop()

