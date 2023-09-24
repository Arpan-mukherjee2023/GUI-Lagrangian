import tkinter.font
from tkinter import *
import matplotlib.pyplot as plt
import math
import smtplib
from PIL import Image,ImageTk


def get():
    """This function will return the lagrangian point value between the star and the planet itself"""
    x = star_mass.get()
    if x == '':
        mass_s = 0.0
    else:
        mass_s = float(x)
    x = planet_mass.get()
    if x == '':
        mass_p = 0.0
    else:
        mass_p = float(x)

    if mass_s == '':
        return 0.0
    else:
        dist = (star_planet_dist.get()) * (1.496 * 10 ** 8)
        x = math.pow(mass_p / (3 * mass_s), 1/3)
        point_dist = dist*x
        return point_dist/(10**6)


def get_point_val():
    global img_star, imag_planet
    name_s = star_name.get()
    name_p = planet_name.get()

    fr1 = Frame(root, height=330, width=590)
    fr1.place(x=60, y=130)
    cnv = Canvas(fr1, height=250, width=560, bg='black')
    cnv.place(x=15, y=20)
    img_star = ImageTk.PhotoImage(Image.open("img_1.png"))
    root.one = img_star
    cnv.create_image(350, 10, anchor=NW, image=img_star)
    img_planet = Image.open("img_2.png").rotate(350)
    img_resized = ImageTk.PhotoImage(img_planet.resize((90, 90)))
    root.one = img_resized
    cnv.create_image(10, 80, anchor=NW, image=img_resized)

    # cnv.create_line(50, 210, 455, 210, fill='white', width=2)
    point_dist = get()
    cnv.create_text(60, 180, text=name_p, font='courier 10', fill='white')
    cnv.create_text(450, 220, text=name_s, font='courier 10', fill='white')
    cnv.create_line(60, 210, 230, 210, fill='white', width=2)
    cnv.create_text(160, 200, text=str(round(point_dist, 2)), font='courier 10', fill='white')
    cnv.create_text(160, 220, text="Lagrangian Point(L1)", font='courier 10', fill='white')

    show_str = f"The Lagrangian point(L1) between {name_p} and {name_s} is located at \na distance of {round(point_dist, 2)} million Km from {name_p}"
    Label(fr1, text=show_str, font='courier').place(x=15, y=285)


if __name__ == '__main__':
    root = Tk()
    root.geometry("700x500")
    root.title('Lagrangian Point Calculator')
    # for background image
    bg = PhotoImage(file='img.png')
    label1 = Label(root,image=bg)
    label1.place(x=0,y=0)

    f1 = Frame(root, background='white', width=250, height=30, borderwidth=3)
    f1.place(x=250, y=90)
    Label(f1, text='Lagrangian Point', font='courier 17').place(x=3, y=0)

    #variables
    star_name = StringVar()
    planet_name = StringVar()
    star_mass = StringVar()
    planet_mass = StringVar()
    star_planet_dist = DoubleVar()
    gravity_star = StringVar()
    gravity_planet = StringVar()


    star_label = Label(root, text="Star Name : ", font='courier')
    star_label.place(x=100,y=200)

    star_name_entry = Entry(root, bg='white', highlightcolor='black', textvariable=star_name, width=50)
    star_name_entry.place(x=340, y=200)

    planet_label = Label(root, text="Planet Name : ", bg='#F2F0EB', font='courier')
    planet_label.place(x=100, y=230)

    planet_name_entry = Entry(root, bg='white', highlightcolor='black', textvariable=planet_name, width=50)
    planet_name_entry.place(x=340, y=230)

    star_mass_label = Label(root, text="Mass of Star(Kg)  : ", bg='white', font='courier')
    star_mass_label.place(x=100, y=260)

    star_mass_entry = Entry(root, bg='white', highlightcolor='black', textvariable=star_mass, width=50)
    star_mass_entry.place(x=340, y=260)

    planet_mass_label = Label(root, text="Mass of Planet(Kg) : ", bg='white', font='courier')
    planet_mass_label.place(x=100, y=290)

    planet_mass_entry = Entry(root, bg='white', highlightcolor='black', textvariable=planet_mass, width=50)
    planet_mass_entry.place(x=340, y=290)

    planet_star_dist_label = Label(root, text="Distance(AU) : ", bg='white', font='courier')
    planet_star_dist_label.place(x=100, y=320)

    planet_star_dist_entry = Entry(root, bg='white', highlightcolor='black', textvariable=star_planet_dist, width=50)
    planet_star_dist_entry.place(x=340, y=320)

    mf = tkinter.font.Font(weight='bold',size=20,family='Helvetica')
    get_button = Button(root, activebackground='Skyblue', image=bg,text='Get Point',command=get_point_val, font=mf, width=300, height=40)
    get_button.place(x=200, y=380)
    root.mainloop()