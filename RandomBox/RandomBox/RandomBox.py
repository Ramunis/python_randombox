import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import random
from PIL import Image, ImageTk
from ttkthemes import themed_tk as tk
import webbrowser
import math
import itertools
import pprint
import uuid
import sys

window = tk.ThemedTk()
window.get_themes()
window.set_theme("arc")
window.title("Random Box")
#window.iconbitmap('project1.ico')
window.geometry('700x500')
window.resizable(width=False, height=False)

def rn():
    if var1.get() == 1:
       for x in range(int(k0.get())):
          x=random.randint(int(min.get()), int(max.get()))
          text.insert('1.0','{}\n'.format(x))
    if var1.get() == 2:  
        for x in range(int(k0.get())):
          x=random.uniform(int(min.get()), int(max.get()))
          text.insert('1.0','{}\n'.format(x))
def rp():
    if var01.get() == 1:
      i=0
      while i<(int(k1.get())):
         x=random.randint(int(min1.get()), int(max1.get()))
         y=random.randint(int(min1.get()), int(max1.get()))
         text1.insert('1.0',format(x)+','+format(y)+'\n')
         i=i+1
    if var01.get() == 2:
     i=0
     while i<(int(k1.get())):
         x=random.uniform(int(min1.get()), int(max1.get()))
         y=random.uniform(int(min1.get()), int(max1.get()))
         text1.insert('1.0',format(x)+','+format(y)+'\n')
         i=i+1

def rl():
    lat= ["Aa","Bb","Cc","Dd","Ee","Ff","Zz","Hh","Kk","Ll","Mm","Nn","Oo","Pp","Qq","Rr","Ss","Tt","Vv","Xx"]
    cyr= ["Аа","Бб","Вв","Гг","Дд","Ее","Ёё","Жж","Зз","Ии","Йй","Кк","Кк","Лл","Мм","Нн","Оо","Пп","Рр","Сс","Тт","Уу","Фф","Хх","Цц","Чч","Шш","Щщ","Ъъ","Ыы","Ьь","Ээ","Юю","Яя"]
    gr=["Aα","Bβ","Гγ","Δδ","Eε","Zζ","Hη","Θθ","Iι","Kκ","Λλ","Mμ","Nν","Ξξ","Οο","Пπ","Рρ","Σ σ,ς","Тτ","Yυ","Фφ","Χχ","Ψψ","Ωω"]
    for x in range(int(k2.get())):
         if var.get() == 1:
             x=random.choice(lat)
             text2.insert('1.0','{}\n'.format(x))
         elif var.get() == 2:
             x=random.choice(cyr)
             text2.insert('1.0','{}\n'.format(x))
         elif var.get() == 3:
             x=random.choice(gr)
             text2.insert('1.0','{}\n'.format(x))

def rw():
    s = text3.get(1.0, END)
    s1= s.split("\n")
    for x in range(int(k3.get())):
       x=random.choice(s1)
       text4.insert('1.0','{}\n'.format(x))

def rb():
    yn=["Yes","No"]
    if ((k4.get()!="") and (k4.get()!=" ") and (k4.get()!="  ")):
        x=random.choice(yn)
        text5.insert('1.0','{}\n'.format(x))
    else:
        text5.insert('1.0','ERROR\n')

def mix():
    s = text6.get(1.0, END) 
    text6.delete('1.0', END)
    words= s.split('\n')
    l = list(words)
    random.shuffle(l)
    result = '\n'.join(l)
    text6.insert('1.0',result)
    #for i, word in enumerate(map(list, words)):
      #random.shuffle(word)
      #words[i] = ''.join(word)
      #text6.insert('1.0',*words)

def rc():
    text7.delete('1.0',END)
    d= random.randint(-90,90)
    s= random.randint(-180,180)
    d1 = random.randint(1000000,9999999)
    s1 = random.randint(1000000,9999999)
    text7.insert('1.0',format(d)+'.'+format(d1)+','+format(s)+'.'+format(s1))

def b1(event):
    loadab()
    rm()

def rm():
    cn=random.randint(0,1)
    if (cn==0):
        try:
            tab7.img = Image.open("c1.jpg")
        except IOError:
            print("Unable to load image")            
        coin =  ImageTk.PhotoImage(tab7.img)
        lbc = ttk.Label(tab7, image=coin)
        lbc.image = coin
        lbc.place(x=170,y=80)
    else:
        try:
            tab7.img = Image.open("с2.jpg")
        except IOError:
            print("Unable to load image")          
        coin =  ImageTk.PhotoImage(tab7.img)
        lbc = ttk.Label(tab7, image=coin)
        lbc.image = coin
        lbc.place(x=170,y=80)

def loadab():
    try:
        tab11.img = Image.open("1.png")
    except IOError:
        print("Unable to load image")
    ab =  ImageTk.PhotoImage(tab11.img)
    lbimg = ttk.Label(tab11, image=ab)
    lbimg.image = ab
    lbimg.place(x=250,y=60)

def perm():
    if (len(ob.get())>6):
        if messagebox.askyesno("Question", "Powerful processor required.Continue?") == True:
            textc.delete('1.0',END)
            np=math.factorial(len(ob.get()))          
            lbnp = ttk.Label(tab9, text=np)
            lbnp.place(x=170, y=94)
            textc.insert('1.0',list(itertools.permutations(ob.get())))           
        else:
         textc.delete('1.0',END)
         np=math.factorial(len(ob.get()))
         textc.insert('1.0',np)  
    if (len(ob.get())<=6):
      textc.delete('1.0',END)
      np=math.factorial(len(ob.get()))
      lbnp = ttk.Label(tab9, text=np)
      lbnp.place(x=170, y=94)
      textc.insert('1.0',list(itertools.permutations(ob.get())))
    
def c():
   if (len(k.get())>6):
        if messagebox.askyesno("Question", "Powerful processor required.Continue?") == True:
            textcomb.delete('1.0',END)
            k1= (k.get())
            n1 =int(n.get())
            textcomb.insert('1.0',list(itertools.combinations(k1, n1)))
            n0= len(k.get())
            k0= int(n.get())
            nk =n0-k0
            c= (math.factorial(n0)/(math.factorial(k0)*math.factorial(nk)))
            lbout = ttk.Label(tab10, text=c)
            lbout.place(x=170, y=114)
        else:
            textcomb.delete('1.0',END)
            n0= len(k.get())
            k0= int(n.get())
            nk =n0-k0
            c= (math.factorial(n0)/(math.factorial(k0)*math.factorial(nk)))
            textcomb.insert('1.0',c)
   if (len(k.get())<=6):
     textcomb.delete('1.0',END)
     k1= (k.get())
     n1 =int(n.get())
     textcomb.insert('1.0',list(itertools.combinations(k1, n1)))
     n0= len(k.get())
     k0= int(n.get())
     nk =n0-k0
     c= (math.factorial(n0)/(math.factorial(k0)*math.factorial(nk)))
     lbout = ttk.Label(tab10, text=c)
     lbout.place(x=170, y=114)

def hash():
      texth.delete('1.0',END)
      safeId = uuid.uuid4()
      texth.insert('1.0',safeId)
   
def callback(event):
    webbrowser.open_new(r"http://www.ramunisoft.blogspot.com")   

def googlemaps():
    webbrowser.open_new(r"https://www.google.com/maps/@"+text7.get(1.0,END)+",12z") 

def deltext1():
    text.delete('1.0',END)

def deltext2():
    text1.delete('1.0',END)

def deltext3():
    text2.delete('1.0',END)

def deltext4():
    text4.delete('1.0',END)

def deltext5():
    text5.delete('1.0',END)

def deltext6():
    text6.delete('1.0',END)

def write(e):
    window.clipboard_clear()
    window.clipboard_append(text.get(1.0, END) )
   
def write1(e):
    window.clipboard_clear()
    window.clipboard_append(text1.get(1.0, END) )   

def write2(e):
    window.clipboard_clear()
    window.clipboard_append(text2.get(1.0, END) )

def write3(e):
    window.clipboard_clear()
    window.clipboard_append(text4.get(1.0, END) )

def write6(e):
    window.clipboard_clear()
    window.clipboard_append(text6.get(1.0, END) )

def write7(e):
    window.clipboard_clear()
    window.clipboard_append(text7.get(1.0, END) )

def writeperm(e):
    window.clipboard_clear()
    window.clipboard_append(textc.get(1.0, END) )

def writehash(e):
    window.clipboard_clear()
    window.clipboard_append(texth.get(1.0, END) )

def savetext():
    save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')

    if save_text_as:
        text_to_save=text.get('1.0','end-1c')
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo("Error","Error")
 
def savetext1():
    save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')

    if save_text_as:
        text_to_save=text1.get('1.0','end-1c')
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo("Error","Error")

def savetext2():
    save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')

    if save_text_as:
        text_to_save=text2.get('1.0','end-1c')
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo("Error","Error")

def savetext4():
    save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')

    if save_text_as:
        text_to_save=text4.get('1.0','end-1c')
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo("Error","Error")

def savetext6():
    save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')

    if save_text_as:
        text_to_save=text6.get('1.0','end-1c')
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo("Error","Error")

def savetextperm():
    save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')

    if save_text_as:
        text_to_save=textc.get('1.0','end-1c')
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo("Error","Error")

def savetextcomb():
    save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')

    if save_text_as:
        text_to_save=textcomb.get('1.0','end-1c')
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo("Error","Error")

def savetexthash():
    save_text_as = filedialog.asksaveasfile(mode='w', defaultextension='.txt')

    if save_text_as:
        text_to_save=texth.get('1.0','end-1c')
        save_text_as.write(text_to_save)
        save_text_as.close()
    else:
        messagebox.showinfo("Error","Error")

def openfile():
    global filename

    filename= filedialog.askopenfilename(initialdir="/",title="Open File",filetypes=(("Text files","*.txt"),("All Files","*.*")))
    
    if filename:
        the_file=open(filename)
        text3.delete('1.0',tk.END)
        text3.insert(tk.END,the_file.read())
        the_file.close()
    else:
        messagebox.showinfo("Error","Error")
        
def openfile1():
    global filename

    filename= filedialog.askopenfilename(initialdir="/",title="Open File",filetypes=(("Text files","*.txt"),("All Files","*.*")))
    
    if filename:
        the_file=open(filename)
        text6.delete('1.0',tk.END)
        text6.insert(tk.END,the_file.read())
        the_file.close()
    else:
        messagebox.showinfo("Error","Error")   

tabControl = ttk.Notebook(window)
tab1= ttk.Frame(tabControl)
tabControl.add(tab1, text ="Numbers")
tabControl.pack(expan=1,fill ="both")
lb1 = ttk.Label(tab1, text="    Insert number range from")
lb1.place(x=10, y=10)
min = ttk.Entry(tab1)
min.place(x=24, y=30,width=70)
lb2 = ttk.Label(tab1, text="to")
lb2.place(x=95, y=30)
max = ttk.Entry(tab1)
max.place(x=110, y=30,width=75)
lb3 = ttk.Label(tab1, text="    Amount of numbers")
lb3.place(x=10, y=60)
k0= ttk.Entry(tab1)
k0.place(x=140,y=60,width=45)
scrollX = ttk.Scrollbar(tab1,orient=HORIZONTAL)
scrollX.place(x=26,y=350,width=164)
scrollY = ttk.Scrollbar(tab1,orient=VERTICAL)
scrollY.place(x=6,y=150,height=205)
text = Text(tab1,width=20, height=12,  wrap=NONE, xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
text.place(x=25,y=155)
scrollX.config(command=text.xview)
scrollY.config(command=text.yview)
btn = ttk.Button(tab1, text="Random",command = rn)
btn.place(x=24, y=115,width=165)
btncopy = ttk.Button(tab1, text="Copy")
btncopy.bind("<Button-1>",write)
btncopy.place(x=24, y=370,width=165)
btnout = ttk.Button(tab1, text="Output to file",command = savetext)
btnout.place(x=24, y=400,width=165)
btndel = ttk.Button(tab1, text="Clear list",command = deltext1)
btndel.place(x=24, y=430,width=165)
var1 = IntVar()
var1.set(1)
rad01 = ttk.Radiobutton(tab1, text='Integer', value=1, variable=var1)
rad01.place(x=24,y=90)
rad02 = ttk.Radiobutton(tab1, text='Double', value=2, variable=var1)
rad02.place(x=90,y=90)

tab2= ttk.Frame(tabControl)
tabControl.add(tab2, text ="Points ")
tabControl.pack(expan=2,fill ="both")
lb11 = ttk.Label(tab2, text="    Insert point range from")
lb11.place(x=10, y=10)
min1 = ttk.Entry(tab2)
min1.place(x=24, y=30,width=70)
lb22 = ttk.Label(tab2, text="to")
lb22.place(x=95, y=30)
max1 = ttk.Entry(tab2)
max1.place(x=110, y=30,width=75)
lb33 = ttk.Label(tab2, text="    Amount of points(X,Y)")
lb33.place(x=10, y=60)
k1= ttk.Entry(tab2)
k1.place(x=150,y=60,width=35)
scrollX = ttk.Scrollbar(tab2,orient=HORIZONTAL)
scrollX.place(x=26,y=350,width=164)
scrollY = ttk.Scrollbar(tab2,orient=VERTICAL)
scrollY.place(x=6,y=150,height=205)
text1 = Text(tab2,width=20, height=12,  wrap=NONE, xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
text1.place(x=25,y=155)
scrollX.config(command=text1.xview)
scrollY.config(command=text1.yview)
btn1 = ttk.Button(tab2, text="Random", command = rp)
btn1.place(x=24, y=115,width=165)
btncopy1 = ttk.Button(tab2, text="Copy")
btncopy1.bind("<Button-1>",write1)
btncopy1.place(x=24, y=370,width=165)
btnout1 = ttk.Button(tab2, text="Output to file", command = savetext1)
btnout1.place(x=24, y=400,width=165)
btndel1 = ttk.Button(tab2, text="Clear list", command = deltext2)
btndel1.place(x=24, y=430,width=165)
var01 = IntVar()
var01.set(1)
rad001 = ttk.Radiobutton(tab2, text='Integer', value=1, variable=var01)
rad001.place(x=24,y=90)
rad002 = ttk.Radiobutton(tab2, text='Double', value=2, variable=var01)
rad002.place(x=90,y=90)

tab3= ttk.Frame(tabControl)
tabControl.add(tab3, text ="Letters")
tabControl.pack(expan=3,fill ="both")
lb33 = ttk.Label(tab3, text="    Choise alphabet")
lb33.place(x=10, y=10)
var = IntVar()
var.set(1)
rad1 = ttk.Radiobutton(tab3, text='Latin', value=1, variable=var)
rad1.place(x=20,y=30)
rad2 = ttk.Radiobutton(tab3, text='Cyrillic', value=2, variable=var)
rad2.place(x=71,y=30)
rad3 = ttk.Radiobutton(tab3, text='Greek', value=3, variable=var)
rad3.place(x=133,y=30)
lb34 = ttk.Label(tab3, text="    Amount of letters")
lb34.place(x=10, y=60)
k2 = ttk.Entry(tab3)
k2.place(x=124, y=60,width=65)
btn2 = ttk.Button(tab3, text="Random",command = rl)
btn2.place(x=24, y=90,width=165)
scrollY = ttk.Scrollbar(tab3,orient=VERTICAL)
scrollY.place(x=6,y=125,height=230)
text2 = Text(tab3,width=20, height=14,  wrap=NONE,yscrollcommand=scrollY.set)
text2.place(x=25,y=125)
scrollY.config(command=text2.yview)
btncopy2 = ttk.Button(tab3, text="Copy")
btncopy2.bind("<Button-1>",write2)
btncopy2.place(x=24, y=360,width=165)
btnout2 = ttk.Button(tab3, text="Output to file", command = savetext2)
btnout2.place(x=24, y=390,width=165)
btndel2 = ttk.Button(tab3, text="Clear list", command = deltext3)
btndel2.place(x=24, y=420,width=165)

tab4= ttk.Frame(tabControl)
tabControl.add(tab4, text ="Words  ")
tabControl.pack(expan=4,fill ="both")
lb44 = ttk.Label(tab4, text="    Create list or ")
lb44.place(x=10, y=10)
btnl=ttk.Button(tab4, text= "load", command = openfile)
btnl.place(x=95,y=10,height=25,width=47)
scrollX0 = ttk.Scrollbar(tab4,orient=HORIZONTAL)
scrollX0.place(x=25,y=205,width=445)
scrollY0 = ttk.Scrollbar(tab4,orient=VERTICAL)
scrollY0.place(x=6,y=40,height=165)
text3 = Text(tab4,width=55, height=10, wrap=NONE,xscrollcommand=scrollX0.set,yscrollcommand=scrollY0.set)
text3.place(x=25,y=40)
scrollX0.config(command=text3.xview)
scrollY0.config(command=text3.yview)
lb55 = ttk.Label(tab4, text="    Amount of words")
lb55.place(x=10, y=230)
k3= ttk.Entry(tab4)
k3.place(x=125, y=230,width=30)
btn3 =ttk.Button(tab4,text="Random",command = rw)
btn3.place(x=160,y=225,width=75)
scrollX = ttk.Scrollbar(tab4,orient=HORIZONTAL)
scrollX.place(x=25,y=425,width=445)
scrollY = ttk.Scrollbar(tab4,orient=VERTICAL)
scrollY.place(x=6,y=260,height=165)
text4= Text(tab4,width=55,height=10, wrap=NONE, xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
text4.place(x=25,y=260)
scrollX.config(command=text4.xview)
scrollY.config(command=text4.yview)
btncopy3 = ttk.Button(tab4, text="Copy")
btncopy3.bind("<Button-1>",write3)
btncopy3.place(x=240, y=225,width=55)
btnout3 = ttk.Button(tab4, text="Output to file",command = savetext4)
btnout3.place(x=300, y=225,width=95)
btndel3 = ttk.Button(tab4, text="Clear list",command = deltext4)
btndel3.place(x=400, y=225,width=70)

tab5= ttk.Frame(tabControl)
tabControl.add(tab5, text ="Yes or No")
tabControl.pack(expan=5,fill ="both")
lb55 = ttk.Label(tab5, text="    Insert Ask")
lb55.place(x=10, y=10)
k4= ttk.Entry(tab5)
k4.place(x=25,y=30,width=220)
lb66 = ttk.Label(tab5,text="?")
lb66.place(x=245,y=30)
btn4= ttk.Button(tab5,text="Find out the answer",command = rb)
btn4.place(x=25,y=60, width =220)
scrollY = ttk.Scrollbar(tab5,orient=VERTICAL)
scrollY.place(x=6,y=100,height=292)
text5= Text(tab5,width=27,height=18,wrap=NONE,yscrollcommand=scrollY.set)
text5.place(x=25,y=100)
scrollY.config(command=text5.yview)
btndel4 = ttk.Button(tab5, text="Clear list",command = deltext5)
btndel4.place(x=24, y=405,width=220)

tab6= ttk.Frame(tabControl)
tabControl.add(tab6, text ="Mix    ")
tabControl.pack(expan=6,fill ="both")
lb66 = ttk.Label(tab6, text="    Create List or ")
lb66.place(x=10, y=10)
btnl1=ttk.Button(tab6, text= "load", command = openfile1)
btnl1.place(x=95,y=6,height=26,width=46)
scrollX = ttk.Scrollbar(tab6,orient=HORIZONTAL)
scrollX.place(x=24,y=390,width=445)
scrollY = ttk.Scrollbar(tab6,orient=VERTICAL)
scrollY.place(x=6,y=35,height=355)
text6 =Text(tab6, width=55,height=22, wrap=NONE, xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
text6.place(x=25,y=35)
scrollX.config(command=text6.xview)
scrollY.config(command=text6.yview)
btn5= ttk.Button(tab6,text="Mix",command = mix)
btn5.place(x=25,y=410,width=100)
btncopy6 = ttk.Button(tab6, text="Copy")
btncopy6.bind("<Button-1>",write6)
btncopy6.place(x=140, y=410,width=100)
btnout6 = ttk.Button(tab6, text="Output to file", command = savetext6)
btnout6.place(x=260, y=410,width=100)
btndel6 = ttk.Button(tab6, text="Clear list",command = deltext6)
btndel6.place(x=370, y=410,width=100)

tab7= ttk.Frame(tabControl)
tabControl.add(tab7, text ="Coin    ")
tabControl.pack(expan=7,fill ="both")     
window.bind('<Button-1>', b1)

tab8= ttk.Frame(tabControl)
tabControl.add(tab8, text ="Geolocation")
tabControl.pack(expan=8,fill ="both")
lb77 = ttk.Label(tab8, text="    Longitud,latitude")
lb77.place(x=10, y=10)
text7 =Text(tab8, width=27,height=19)
text7.place(x=25,y=30)
btn6= ttk.Button(tab8,text="Random",command = rc)
btn6.place(x=25,y=350,width=220)
btncopy7 = ttk.Button(tab8, text="Open to Google Maps",command = googlemaps)
btncopy7.place(x=25, y=380,width=220)
btnout7 = ttk.Button(tab8, text="Copy coordinates")
btnout7.bind("<Button-1>",write7)
btnout7.place(x=25, y=410,width=220)

tab9= ttk.Frame(tabControl)
tabControl.add(tab9, text ="Permutations")
tabControl.pack(expan=9,fill ="both")
lbp = ttk.Label(tab9, text="    Insert objects")
lbp.place(x=10, y=10)
ob= ttk.Entry(tab9)
ob.place(x=25,y=30,width=220)
btnp= ttk.Button(tab9, text ="Get permunations", command = perm)
btnp.place(x=25,y=60,width=220)
lbpc=ttk.Label(tab9,text="    Number of permutations = ")
lbpc.place(x=10, y=94)
scrollX = ttk.Scrollbar(tab9,orient=HORIZONTAL)
scrollX.place(x=24,y=390,width=223)
scrollY = ttk.Scrollbar(tab9,orient=VERTICAL)
scrollY.place(x=6,y=115,height=276)
textc= Text(tab9, width=27,height=17, wrap=NONE, xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
textc.place(x=25,y=115)
scrollX.config(command=textc.xview)
scrollY.config(command=textc.yview)
btnoutp= ttk.Button(tab9,text="Output to file",command =savetextperm)
btnoutp.place(x=25,y=410,width=220)

tab10= ttk.Frame(tabControl)
tabControl.add(tab10, text ="Combinations")
tabControl.pack(expan=10,fill ="both")
lbk = ttk.Label(tab10, text="    Insert all objects(k)")
lbk.place(x=10, y=10)
lbn = ttk.Label(tab10, text="    Insert amount of selected objects(N)")
lbn.place(x=10, y=55)
k= ttk.Entry(tab10)
k.place(x=25,y=30,width=220)
n= ttk.Entry(tab10)
n.place(x=220,y=55,width=25)
btnc= ttk.Button(tab10, text ="Get combinations",command =c)
btnc.place(x=25,y=85,width=220)
lbpc1=ttk.Label(tab10,text="    Number of combinations = ")
lbpc1.place(x=10, y=114)
scrollX = ttk.Scrollbar(tab10,orient=HORIZONTAL)
scrollX.place(x=24,y=378,width=223)
scrollY = ttk.Scrollbar(tab10,orient=VERTICAL)
scrollY.place(x=6,y=135,height=246)
textcomb= Text(tab10, width=27,height=15, wrap=NONE, xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
textcomb.place(x=25,y=135)
btnsc= ttk.Button(tab10, text="Output to file",command =  savetextcomb)
btnsc.place(x=25,y=405,width=220)
scrollX.config(command=textcomb.xview)
scrollY.config(command=textcomb.yview)

tab11= ttk.Frame(tabControl)
tabControl.add(tab11, text ="About  ")
tabControl.pack(expan=11,fill ="both")
window.bind('<Button-1>', b1)
lb88 = ttk.Label(tab11, text="    Random Box",font="Arial 20")
lb88.place(x=10, y=20)
lb99 = ttk.Label(tab11, text="           2.0")
lb99.place(x=10, y=60)
lb100 = ttk.Label(tab11, text="         © 2020 Ramunis Soft",font="Arial 10")
lb100.place(x=10, y=380)
link = Label(tab11, text="Homepage", fg="blue", cursor="hand2")
link.place(x=45,y=400)
link.bind("<Button-1>", callback)

window.mainloop()

