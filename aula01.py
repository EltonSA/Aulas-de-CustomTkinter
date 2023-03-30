import customtkinter as c

janela = c.CTk()

#Configuração da jenla principal 
janela.title("App teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)


#Customixando o tema
janela._set_appearance_mode("dark")


#Criando nova janela
def nova_janela():
    nova_janela = c.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry("200x200")

butao_nova_tela = c.CTkButton(master=janela, text="Abrir nova janela", command= nova_janela).place(x=300, y=100)









janela.mainloop()