from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def pozycjonowanie_okna(okno,w, h):
    ws = okno.winfo_screenwidth()
    hs = okno.winfo_screenheight()
    x = ws/2 - w/2
    y = hs/2 - h/2
    okno.geometry('%dx%d+%d+%d' % (w, h, x, y))

def zmiana_koloru(btn, input, output):
    btn.bind('<Enter>', lambda e: btn.config(fg=output))
    btn.bind('<Leave>', lambda e: btn.config(fg=input))

def gra():
    messagebox.showerror("Error", "Gra nie jest zainstalowana!")

def save(j,d,r,f,t,c,fx,m):
    global g_jezyk, g_dzwiek, g_rozdzielczosc, g_fullscreen, g_tekstury, g_cienie, g_fxaa, g_motion
    g_jezyk=j.get()
    g_dzwiek = d.get()
    g_rozdzielczosc = r.get()
    g_fullscreen = f.get()
    g_tekstury = t.get()
    g_cienie = c.get()
    g_fxaa = fx.get()
    g_motion = m.get()

def opcje_okienko(g_jezyk, g_dzwiek, g_rozdzielczosc, g_fullscreen, g_tekstury, g_cienie, g_fxaa, g_motion):
    def zamykanie_okna():
        menu.deiconify()
        opcje_okno.destroy()

    menu.withdraw()
    opcje_okno = Toplevel()
    pozycjonowanie_okna(opcje_okno, 361, 490)
    opcje_okno.title('Opcje gry')
    opcje_okno.iconbitmap('logo_opcje.ico')
    opcje_okno.resizable(width=FALSE, height=FALSE)
    opcje_okno.protocol("WM_DELETE_WINDOW", zamykanie_okna)

    img = PhotoImage(file='logo.png')
    Label(opcje_okno, image=img, borderwidth=0).grid(column=0, row=0)

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = IntVar()
    var7 = IntVar()

    Label(opcje_okno, text='Język gry', font=("Times", 11)).grid(column=0, row=1, sticky='W')
    jezyk=OptionMenu(opcje_okno, var1, "Polski", "Angielski", "Niemiecki", "Francuski", "Rosyjski")
    jezyk.grid(column=0, row=2, sticky='W')
    var1.set(g_jezyk)

    Label(opcje_okno, text='Dźwięk', font=("Times", 11)).grid(column=0, row=3, sticky='W')
    dzwiek=Scale(opcje_okno, from_=0, to=100, orient=HORIZONTAL)
    dzwiek.grid(column=0, row=4, sticky='W')
    dzwiek.set(g_dzwiek)

    Label(opcje_okno, text='Rozdzielczość ekranu', font=("Times", 11)).grid(column=0, row=5, sticky='W')
    rozdzielczosc = OptionMenu(opcje_okno, var2, "1920x1080", "1600×900", "1366×768", "1280x720", "1024×600")
    rozdzielczosc.grid(column=0, row=6, sticky='W')
    var2.set(g_rozdzielczosc)

    Label(opcje_okno, text='Pełny ekran', font=("Times", 11)).grid(column=0, row=7, sticky='W')
    fullscreen = OptionMenu(opcje_okno, var3, "Włączone", "Wyłączone")
    fullscreen.grid(column=0, row=8, sticky='W')
    var3.set(g_fullscreen)

    Label(opcje_okno, text='Tekstury', font=("Times", 11)).grid(column=1, row=1, sticky='W')
    tekstury = OptionMenu(opcje_okno, var4, "Epickie", "Wysokie", "Średnie", "Niskie")
    tekstury.grid(column=1, row=2, sticky='W')
    var4.set(g_tekstury)

    Label(opcje_okno, text='Cienie', font=("Times", 11)).grid(column=1, row=3, sticky='W')
    cienie = OptionMenu(opcje_okno, var5, "Epickie", "Wysokie", "Średnie", "Niskie")
    cienie.grid(column=1, row=4, sticky='W')
    var5.set(g_cienie)
    fxaa = Checkbutton(opcje_okno, text="FXAA", variable=var6)
    fxaa.grid(column=1, row=5, sticky='W')
    var6.set(g_fxaa)
    motion = Checkbutton(opcje_okno, text="Motion Blur (Rozmycie tła)", variable=var7)
    motion.grid(column=1, row=6, sticky='W')
    var7.set(g_motion)

    domyslne = Button(opcje_okno, text="Domyślne ustawienia", font=("Times", 11),
    activeforeground="orange", command=lambda: [var1.set('Polski'), dzwiek.set('100'),
    var2.set('1920x1080'), var3.set('Włączone'), var4.set('Epickie'), var5.set('Epickie'), var6.set(0), var7.set(0)])
    zmiana_koloru(domyslne, 'black', 'orange')
    domyslne.grid(column=1, row=9, sticky='nsew')

    exit = Button(opcje_okno, text="Wyjdź", font=("Times", 11), activeforeground="orange", command=zamykanie_okna)
    zmiana_koloru(exit, 'black', 'orange')
    exit.grid(column=0, row=10, sticky='nsew')

    zapisz = Button(opcje_okno, text='Zapisz', font=("Times", 11), activeforeground="orange",
    command=lambda: save(var1, dzwiek, var2, var3, var4, var5, var6, var7))
    zmiana_koloru(zapisz, 'black', 'orange')
    zapisz.grid(column=1, row=10, sticky='nsew')

    opcje_okno.mainloop()

def mody_okienko():
    def zamykanie_okna():
        menu.deiconify()
        mody_okno.destroy()

    def dodanie_moda():
        filename = filedialog.askopenfilename()
        if filename:
            Label(mody_okno, text=filename, wraplength=256, bg='white').pack()
            messagebox.showinfo("Mody", "Mod został dodany!")

    menu.withdraw()

    mody_okno = Toplevel()
    pozycjonowanie_okna(mody_okno, 256, 500)
    mody_okno.title('Mody')
    mody_okno.iconbitmap('dragon_logo.ico')
    mody_okno.resizable(width=FALSE, height=FALSE)
    mody_okno.configure(bg = 'white')
    mody_okno.protocol("WM_DELETE_WINDOW", zamykanie_okna)

    img2=PhotoImage(file='japan.png')
    Label(mody_okno, image=img2, borderwidth=0).pack()

    exit = Button(mody_okno, text='Wyjdź', font=("Times", 11), activeforeground="orange", command=zamykanie_okna)
    zmiana_koloru(exit, 'black', 'orange')
    exit.pack(side='bottom', fill=BOTH)

    dodaj=Button(mody_okno, text='Przeglądaj', font=("Times", 11), activeforeground="orange", command=dodanie_moda)
    zmiana_koloru(dodaj, 'black', 'orange')
    dodaj.pack(side='bottom', fill=BOTH)

    mody_okno.mainloop()

g_jezyk='Polski'
g_dzwiek=100
g_rozdzielczosc='1920x1080'
g_fullscreen='Włączone'
g_tekstury='Epickie'
g_cienie='Epickie'
g_fxaa=0
g_motion=0

menu = Tk()
pozycjonowanie_okna(menu, 428, 533)
menu.title('Times of Dragons')
menu.iconbitmap('dragon_logo.ico')
menu.geometry('428x533')
menu.attributes('-alpha', 0.95)
menu.resizable(width=FALSE, height=FALSE)

img = PhotoImage(file='obraz.png')
tlo = Label(menu, image=img)
tlo.place(relwidth=1, relheight=1)

exit = Button(menu, text="Wyjdź\n", fg="white", bg="black", activebackground="black", activeforeground="orange", borderwidth=0, font=("Times", 14), command=menu.destroy)
zmiana_koloru(exit, 'white', 'orange')
exit.pack(side='bottom')

mody = Button(menu, text="Mody", fg="white", bg="black", activebackground="black", activeforeground="orange", borderwidth=0, font=("Times", 14), command=mody_okienko)
zmiana_koloru(mody, 'white', 'orange')
mody.pack(side='bottom')

opcje = Button(menu, text="Opcje", fg="white", bg="black",
activebackground="black", activeforeground="orange", borderwidth=0, font=("Times", 14),
command= lambda: opcje_okienko(g_jezyk, g_dzwiek, g_rozdzielczosc,
g_fullscreen, g_tekstury, g_cienie, g_fxaa, g_motion))

zmiana_koloru(opcje, 'white', 'orange')
opcje.pack(side='bottom')

graj = Button(menu, text="Graj", fg="white", bg="black", activebackground="black", activeforeground="orange", borderwidth=0, font=("Times", 14), command=gra)
zmiana_koloru(graj, 'white', 'orange')
graj.pack(side='bottom')

Label(menu, text="Times of Dragons\n", font=("Times", "22", "bold italic"), bg="black", fg="white").pack(side='bottom')

menu.mainloop()
