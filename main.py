import turtle
import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.title('PyDrawboard')

root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.destroy())
root.resizable(width=False, height=False)

color0 = '#57538c'
color1 = '#867fbd'
color2 = '#6f69a5'
color3 = '#403d74'
color4 = 'BLACK'

root.configure(bg=color0)

content = tk.Frame(root)
frame = tk.Frame(content, width=600, height=600)

canvas = tk.Canvas(master=root, width=800, height=600,
    highlightthickness=5,
    highlightbackground=color2,
    bg='black',
)
canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
tela = turtle.TurtleScreen(canvas)

tela.bgcolor('black')
tela.tracer(0)

t = turtle.RawTurtle(tela)
t.speed(0)
t.pencolor('white')
t.width(4)
t.penup()
t.hideturtle()

colors = ['white',
        '#f98075',
        '#93fd85',
        '#85a8fd',
        '#fd85fc',
        '#75f9f1',]

def espessura_menor():
    t.width(max(1, t.width() - 1))
def espessura_maior():    
    t.width(t.width() + 1)

def start_draw(x, y):
    t.penup()
    t.goto(x-400, -y+300)
    t.pendown()

def draw(x, y):
    t.pendown()
    t.goto(x-400, -y+300)
    tela.update()
    
def limpar_tela():
    t.clear()
    t.penup()
    
def desfazer():
    t.undo()
    
def circle():
    t.circle(5)
    
def color():
    color_picked = colorchooser.askcolor()[1]
    t.pencolor(color_picked)

def color_i(c):
    t.pencolor(c)

rodando = [False]

def random_color_loop():
    if not rodando[0]:
        r_color = random.choice(colors)
        t.pencolor(r_color)
        tela.update()
        root.after(200, random_color_loop)

def toggle_random_color():
        if rodando[0]:
            t.pencolor('white')
            tela.update()
        else:
            random_color_loop()

index = [0]

def num_color(index):
    if index < len(colors):
        t.pencolor(colors[index])

for i in range(len(colors)):
    tecla = str(i+1)
    tela.onkey(lambda idx=i: num_color(idx), tecla)

botoes_frame = tk.Frame(root, bg=color0)

lateral_frame = tk.Frame(root, bg=color0)

img_color = ImageTk.PhotoImage(Image.open('src/color_pick.png'))
img_up = ImageTk.PhotoImage(Image.open('src/arrow_up.png'))
img_down = ImageTk.PhotoImage(Image.open('src/arrow_down.png'))
img_more = ImageTk.PhotoImage(Image.open('src/more.png'))
img_random = ImageTk.PhotoImage(Image.open('src/random.png'))

btn_1 = tk.Button(
    lateral_frame,
    background=color0,
    foreground=color4,
    width=30,
    height=30,
    highlightthickness=2,
    highlightbackground=color2,
    highlightcolor='WHITE',
    activebackground=color3,
    activeforeground=color4,
    cursor='hand2',
    border=0,
    image=img_color,
    compound=tk.LEFT, 
    font=('Arial', 15, 'bold'),
    command=color)
btn_1.pack(padx = 5, side="left")

btn_r = tk.Button(
    lateral_frame,
    background=color0,
    foreground=color4,
    width=30,
    height=30,
    highlightthickness=2,
    highlightbackground=color2,
    highlightcolor='WHITE',
    activebackground=color3,
    activeforeground=color4,
    cursor='hand2',
    border=0,
    image=img_random,
    compound=tk.LEFT, 
    font=('Arial', 15, 'bold'),
    command=toggle_random_color)
btn_r.pack(padx = 5, side="left")



btn_2 = tk.Button(
    botoes_frame,
    background=color0,
    foreground=color4,
    width=30,
    height=30,
    highlightthickness=2,
    highlightbackground=color2,
    highlightcolor='WHITE',
    activebackground=color3,
    activeforeground=color4,
    cursor='hand2',
    border=0,
    image=img_up,
    compound=tk.LEFT,
    font=('Arial', 15, 'bold'),
    command=espessura_maior)
    
btn_2.pack(padx = 5, side="left")
    
btn_3 = tk.Button(
    botoes_frame,
    background=color0,
    foreground=color4,
    width=30,
    height=30,
    highlightthickness=2,
    highlightbackground=color2,
    highlightcolor='WHITE',
    activebackground=color3,
    activeforeground=color4,
    cursor='hand2',
    border=0,
    image=img_down,
    compound=tk.LEFT,
    font=('Arial', 15, 'bold'),
    command=espessura_menor)

btn_3.pack(padx = 5, side="left")

frames_visiveis = [False]  # Usando lista para mutabilidade

def toggle():
    if frames_visiveis[0]:
        botoes_frame.pack_forget()
        lateral_frame.pack_forget()
        frames_visiveis[0] = False
    else:
        botoes_frame.pack(side="right", fill="x", pady=(0,10), padx=5)
        lateral_frame.pack(side="left", fill="x", pady=(0,10), padx=5)
        frames_visiveis[0] = True

tab_frame = tk.Frame(root, bg=color0)
tab_frame.pack(side="top", pady=(0,10), padx=10)
toggle_btn = tk.Button(
    tab_frame,
    background=color0,
    foreground=color4,
    width=50,
    height=10,
    highlightthickness=2,
    highlightbackground=color2,
    highlightcolor='WHITE',
    activebackground=color3,
    activeforeground=color4,
    cursor='hand2',
    border=0,
    image=img_more,
    compound=tk.LEFT,
    font=('Arial', 15, 'bold'),
    command=toggle
)
toggle_btn.pack(side="top", padx=5, pady=5)

botoes = [btn_1, btn_2, btn_3]

def btn_enter(event):
    event.widget.config(highlightbackground=color3)

def btn_leave(event):
    event.widget.config(highlightbackground=color2)

for botao in botoes:
    botao.bind('<Enter>', btn_enter)
    botao.bind('<Leave>', btn_leave)

canvas.bind("<ButtonPress-1>", lambda e: start_draw(e.x, e.y))
canvas.bind("<B1-Motion>", lambda e: draw(e.x, e.y))
#t.ondrag(draw)
#t.onclick(start_draw)

tela.listen()
tela.onkey(desfazer, 'BackSpace')
tela.onkey(limpar_tela, 'space')

tela.onkey(color_i, 'i')

root.mainloop()
