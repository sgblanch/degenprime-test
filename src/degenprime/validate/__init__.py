import shutil
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class ValidationGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.mainWindow()
    
    def mainWindow(self):
        self.title("DeGenPrime")
        self.geometry(f"{640}x{480}")
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((3), weight=1)

        window_lbl = ctk.CTkLabel(self, text="DeGenPrime", font=ctk.CTkFont(size=20, weight="bold"))
        window_lbl.grid(row=0, column=0, padx=20, pady=20, sticky = "ew", columnspan=2)
        
        cmd_degenprime_lbl = ctk.CTkLabel(self, text="DeGenPrime", font=ctk.CTkFont(weight="bold"))
        cmd_degenprime_lbl.grid(row=1, column=0, padx=20, sticky = "w")
        cmd_degenprime_found = ctk.CTkLabel(self, text=self.which("degenprime"), font=ctk.CTkFont(family="monospaced"))
        cmd_degenprime_found.grid(row=1, column=1, padx=20, sticky = "w")
        
        cmd_mafft_lbl = ctk.CTkLabel(self, text="MAFFT", font=ctk.CTkFont(weight="bold"))
        cmd_mafft_lbl.grid(row=2, column=0, padx=20, sticky = "w")
        cmd_mafft_found = ctk.CTkLabel(self, text=self.which("mafft"), font=ctk.CTkFont(family="monospaced"))
        cmd_mafft_found.grid(row=2, column=1, padx=20, sticky = "w")

        button = ctk.CTkButton(self, text="Click Me", command=self.button_callback)
        button.grid(row=3, column=0, padx=20, pady=20, sticky="s", columnspan=2)

    def button_callback(self):
        CTkMessagebox(master = self, title="Warning Message!", message="Button Clicked!", icon="warning")
    
    def which(self, cmd):
        path = shutil.which(cmd)

        if path is not None and path != "":
            return path
        else:
            return "Not Found"

def validate():
    app = ValidationGUI()
    app.mainloop()
