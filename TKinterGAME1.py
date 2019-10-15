from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x670')
root.title('QUIDDITCH Game')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
name_entry = 'ANONIM'
name_label = Label(text = 'PLEASE ENTER YOUR NAME:')
name_label.pack()
name_entry = Entry()
name_entry.pack()
name_entry.insert(0, "ANONIM")


x,y = 400,300
mouseX,mouseY = x,y
canv.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red', width=0, tag = 'ded')

# ОПРЕДЕЛЯЕМ РЕКОРД
file = open('record.txt' , 'r')
file.readlines()

# УЗНАТЬ КООРДИНАТУ КЛИКА
def click(event):
    global mouseX,mouseY
    mouseX,mouseY = event.x, event.y

# ДВИЖЕНИЕ ИГРОКА
boo = True
count = 0
def moov():
    global x,y,stop,mouseX,mouseY,circX,circY,r,boo,count
    canv.delete('ded')
    canv.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red', width=0, tag = 'ded')
    x += (mouseX-x)/10
    y += (mouseY-y)/10
    if circX +r > x and circX - r < x and circY +r > y and circY - r < y:
        if boo == True:
            boo = False
            count += 10
            print(count)
    else:
        boo = True
    root.after(50, moov)

# СНИТЧ
boo1 = True
snitchX = 100
snitchY = 100
sx = rnd(-5,5)
sy = rnd(-5,5)
canv.create_oval(snitchX - 7, snitchY - 7, snitchX + 7, snitchY + 7, fill='yellow', width=0, tag='snitch')
def snitch():
    global snitchX, snitchY, sx , sy,x,y,boo1,count
    canv.delete('snitch')
    canv.create_oval(snitchX - 7, snitchY - 7, snitchX + 7, snitchY + 7, fill='yellow', width=0, tag='snitch')
    snitchX += sx
    snitchY += sy
    if snitchX <0 or snitchX>800:
        sx = -sx
    if snitchY <0 or snitchY>600:
        sy = -sy
    if snitchX +7 > x and snitchX - 7 < x and snitchY +7 > y and snitchY - 7 < y:
        if boo1 == True:
            boo1 = False
            count += 150
            print(count)
        file = open('record.txt', 'a')
        file.writelines(name_entry.get()+' '+str(count)+' ')
        exit()

    else:
        boo1 = True
    button1['text'] = 'count', count
    root.after(10,snitch)

# КВОФЛ
circX = 0
circY = 0
r = 0
i = 0
def new_ball():
    global circX,circY,r,i
    canv.delete(ALL)
    circX = rnd(100, 700)
    circY = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(circX - r, circY - r, circX + r, circY + r, fill='brown', width=0)
    i +=10
    root.after(1500 - i, new_ball)

button1=Label(root,text='count0',width=25,height=1,bg='purple',fg='red',font='arial 14')
button1.pack()

moov()
new_ball()
snitch()
canv.bind('<Button-1>', click)

mainloop()