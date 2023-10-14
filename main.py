import customtkinter as ctk
from PIL import Image,ImageTk
import pyautogui as aut
import time
import os
import PySimpleGUI as pg

janela = ctk.CTk()#iniciando o app
janela.geometry("760x450")#Tamanho do app
janela.resizable(False, False)#Congelando a tela do App
janela.title("ERP AUT v2.0")#titulo do app v1.0
ctk.set_appearance_mode("light")#tema padrão do app

#Fontes utilizadas no App
Font_tuple = ("Microsoft YaHei UI Light", 12, "bold")
font_ver = ("Lucida Sans", 15, "bold")
font_autor = ("Eras Light ITC", 16, "italic")
Font_tuple1 = ("Microsoft YaHei UI Light", 14, "bold")


def entrar():
    senha = caixaDeEntrada2.get()
    box1 = selectBox1.get()
    box2 = selectBox2.get()
    box3 = selectBox3.get()
    box4 = selectBox4.get()
    box5 = selectBox5.get()
    box6 = selectBox6.get()
    print(box1)
    print(box2)
    print(box3)
    if box1 == 'Selecione uma Base' or box2 =='Selecione uma Base' or box3 =='Selecione uma Base':
        aut.alert(text='Você nao selecionou uma Base', title='ERR0R', button='OK')
    
    else:
                #                                               Abrir o Corporate
        os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
        time.sleep(6)


                        #                                               colocar a senha

        time.sleep(1)
        aut.write (senha)
                        #                                               mudar a matriz desejada
        aut.press('Tab')
        aut.write(box1)
        time.sleep(1)
        aut.press('Enter')
                        #                                               entrar
        aut.press('Enter')
        time.sleep(20)
                        #                                             LOOP1

                        #                                               Abrir o Corporate
        os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
        time.sleep(6)


                        #                                               colocar a senha

        time.sleep(1)
        aut.write(senha)
                        #                                               mudar a matriz desejada
        aut.press('Tab')
        aut.write(box2)
        time.sleep(1)
        aut.press('Enter')
                        #                                               entrar
        aut.press('Enter')
        time.sleep(20)
                        #                                              LOOP2
                        #                                               Abrir o Corporate
        os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
        time.sleep(6)


                        #                                               colocar a senha

        time.sleep(1)
        aut.write(senha)
                        #                                               mudar a matriz desejada
        aut.press('Tab')
        aut.write(box3)
        time.sleep(1)
        aut.press('Enter')
                        #                                               entrar
        aut.press('Enter')
        time.sleep(20)
                        #                                              LOOP3
                        #                                               Abrir o Corporate
 





#Imagem da logo Corporate
img = (Image.open("logo.png"))
resized_image= img.resize((180,180))
my_img=ImageTk.PhotoImage(resized_image)

#colocando a imagem em Label e customizando Logo Corporate
label= ctk.CTkLabel(janela, image=my_img,text="")
label.pack()
label.place(x=50, y=20)

#Imagem do Corporate
img = (Image.open("corporate.png"))
resized_image= img.resize((350,100))
my_img=ImageTk.PhotoImage(resized_image)

#colocando a imagem em Label e customizando Corporate Text
label= ctk.CTkLabel(janela, image=my_img,text="")
label.pack()
label.place(x=350, y=25)

text1 = ctk.CTkLabel(master=janela,state='disabled',text="Usuário:")
text1.pack()
text1.place(x=360,y=150)
text1.configure(Font_tuple)

caixaDeEntrada1 = ctk.CTkEntry(janela,placeholder_text="Digite somente a senha",width=335)
caixaDeEntrada1.place(x=360, y=180)
caixaDeEntrada1.configure(state='disabled')

text2 = ctk.CTkLabel(master=janela,text="Senha:")
text2.pack()
text2.place(x=360,y=230)
text2.configure(font= Font_tuple)

caixaDeEntrada2 = ctk.CTkEntry(janela,width=335, show='*')
caixaDeEntrada2.place(x=360, y=260)
caixaDeEntrada2.configure(font= Font_tuple)

buttonVer = ctk.CTkButton(master=janela,
                        text="Entrar",
                        command=entrar,
                        height=(30),
                        width=(172))
buttonVer.pack(padx=5, pady=10)
buttonVer.place(x=360, y=300)
buttonVer.configure(font= Font_tuple1)

selectText1 = ctk.CTkLabel(master=janela,text="BASE 1")
selectText1.pack()
selectText1.place(x=5,y=200)
selectText1.configure(font= Font_tuple)
bases = ['LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]
selectBox1 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox1.pack()
selectBox1.set('Selecione uma Base')
selectBox1.place(x=60,y=200)

selectText1 = ctk.CTkLabel(master=janela,text="BASE 2")
selectText1.pack()
selectBox1.set('Selecione uma Base')
selectText1.place(x=5,y=240)
selectText1.configure(font= Font_tuple)
bases = ['LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]
selectBox2 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox2.set('Selecione uma Base')
selectBox2.pack()
selectBox2.place(x=60,y=240)

selectText1 = ctk.CTkLabel(master=janela,text="BASE 3")
selectText1.pack()
selectText1.place(x=5,y=280)
selectText1.configure(font= Font_tuple)
bases = ['LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]
selectBox3 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox3.set('Selecione uma Base')
selectBox3.pack()
selectBox3.place(x=60,y=280)

selectText4 = ctk.CTkLabel(master=janela,text="BASE 4")
selectText4.pack()
selectText4.place(x=5,y=320)
selectText4.configure(font= Font_tuple)
bases = ['LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]
selectBox4 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox4.pack()
selectBox4.set('Selecione uma Base')
selectBox4.place(x=60,y=320)

selectText5 = ctk.CTkLabel(master=janela,text="BASE 5")
selectText5.pack()
selectText5.place(x=5,y=360)
selectText5.configure(font= Font_tuple)
bases = ['LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]
selectBox5 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox5.pack()
selectBox5.set('Selecione uma Base')
selectBox5.place(x=60,y=360)

selectText6 = ctk.CTkLabel(master=janela,text="BASE 6")
selectText6.pack()
selectText6.place(x=5,y=400)
selectText6.configure(font= Font_tuple)
bases = ['LIN JBS','Matriz','PRE JBS','EES JBS','EEC JBS','CEL JBS',]
selectBox6 = ctk.CTkComboBox(janela,values=bases,width=200)
selectBox6.pack()
selectBox6.set('Selecione uma Base')
selectBox6.place(x=60,y=400)

label3 = ctk.CTkLabel(janela,text="@AUTOR: Ricardo Rodrigues Lima")
label3.pack()
label3.place(x=260,y=425)
label3.configure(font=font_autor)

janela.mainloop()