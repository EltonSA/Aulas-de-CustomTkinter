import customtkinter as c

#Criação da jnale
janela = c.CTk()
c.set_default_color_theme("dark-blue")

#Configuração da janela principal 
janela.title("App Teste")
#Geometria da janela
janela.geometry("700x400")
#largura maxima 
janela.maxsize(width=900, height=550)
#Largura minima
janela.minsize(width=500, height=300)

# AUla06 = TabView (Abas no tknter)
aba = c.CTkTabview(janela, width=400, corner_radius=20, segmented_button_selected_color="blue")
aba.pack()
aba.add("Nomes")
aba.add("Idade")
aba.add("Genero")
#Configuração das abas. 
aba.tab("Nomes").grid_rowconfigure(0, weight=1)
aba.tab("Idade").grid_rowconfigure(0, weight=1)
aba.tab("Genero").grid_rowconfigure(0, weight=1)
#Adicionando elementos na aba 
texto = c.CTkLabel(aba.tab("Nomes"),text="Elton Santos\n Juliano Alencar\n João Maria")
texto.pack()
texto = c.CTkLabel(aba.tab("Idade"), text="Elton tem 20 anos\n Juliano tem 30 anos\n João tem 55 anos")
texto.pack()
texto = c.CTkLabel(aba.tab("Genero"), text="Elton é Cabra Macho\n Juliano é Cabra Macho\n João é Cabra Macho")
texto.pack()


janela.mainloop()