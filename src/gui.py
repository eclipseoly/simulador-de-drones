import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Drones")
        self.geometry("800x600")
        self.attributes("-fullscreen",True)
        
  
        self.frame_topo = ctk.CTkFrame(
            self,
            height=40
        )
        self.frame_topo.pack(
            side="top",
            fill="x",
            padx=10,
            pady=5
        )
        self.frame_topo.pack_propagate(False)

        self.botao_minimizar = ctk.CTkButton(
            self.frame_topo,
            text="-",
            font=("Arial",20),
            command=self.minimizar
        )
        self.botao_minimizar.place(relx=0.90, rely=0.0, relwidth=0.05, relheight=1)

        self.botao_sair = ctk.CTkButton(self.frame_topo, text="x",font=("Arial",20), fg_color="red", hover_color="darkred", command=self.sair)
        self.botao_sair.place(relx=0.95, rely=0.0, relwidth=0.05, relheight=1)

    def minimizar(self):
        self.iconify()

    def sair(self):
        self.destroy()

        
    
    def iniciar(self):
        print("iniciando drone")

def run():
    app = App()
    app.mainloop()