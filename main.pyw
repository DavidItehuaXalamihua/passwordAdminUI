import tkinter as tk
from interfaces.otrasInterfaces.functions.uiFunctions import prettierTxt
from interfaces.passwordUI import UIPassword

prettierTxt()

if __name__ == "__main__":
  app = tk.Tk()
  mainApp= UIPassword(app)
  app.mainloop()


