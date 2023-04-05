import customtkinter as c

#Criação da jnale
janela = c.CTk()

#Configuração da janela principal 
janela.title("App Teste")
#Geometria da janela
janela.geometry("700x400")
#largura maxima 
janela.maxsize(width=900, height=550)
#Largura minima
janela.minsize(width=500, height=300)

#Frames 
frame1 = c.CTkFrame(master= janela, width=200, height=330, fg_color="teal", bg_color="red").place(x= 30, y=60)
frame2 = c.CTkFrame(janela, width=200, height=330, fg_color="green").place(x=250, y=60)
frame3 = c.CTkFrame(janela, width=200, height=330, fg_color="white").place(x=470, y=60) 

janela.mainloop()