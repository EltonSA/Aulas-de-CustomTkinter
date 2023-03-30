import customtkinter as c

#Criação da jnale
janela = c.CTk()

#Configuração da janela principal 
janela.title("App Teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)

#Frames
#frame1 = c.CTkFrame(master= janela, width= 200, height= 330, fg_color="teal", bg_color="transparent", border_width=10, corner_radius=30).place(x= 10, y= 60)f#rame2 = c.CTkFrame(master= janela, width= 200, height=330, fg_color="green", bg_color="transparent", border_width=10, corner_radius=30).place(x= 230, y= 60)
#frame3 = c.CTkFrame(master= janela, width= 200, height=330, fg_color="white", bg_color="transparent", border_width=10, corner_radius=30).place(x= 450, y=60)

#tabvie(Aba TKINTER)
tabview = c.CTkTabview(janela, width= 4000)
tabview.pack()
tabview.add ("Nome")
tabview.add("Idade")
tabview.add("Genero")

tabview.tab("Nome").grid_columnconfigure(0, weight=1)
tabview.tab("Idade").grid_columnconfigure(0, weigth=1)
tabview.tab("Genero").grid_columnconfigure(0, weigth=1)

#Adcionando elementos na tab
texto = c.CTkLabel(tabview.tab("Nome"), text="Manaus Eduardo\n Eduardo \n Antonia tomocente")
texto.pack()



janela.mainloop()