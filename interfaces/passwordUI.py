from sqlite3.dbapi2 import connect
import tkinter as tk
from tkinter import messagebox
from interfaces.otrasInterfaces.functions.uiFunctions import validatePassword
from interfaces.otrasInterfaces import uiUser

class UIPassword():
  colors = {
    "blue0":"#14213d",
    "red0": "#d00000",
    "red1": "#9d0208",
    "green0": "#007200",
    "green1": "#004b23",
    "white0": "#ffffff"
  }

  def __init__(self, wind) -> None:
      super().__init__()
      self.wind = wind
      self.mainScreenWidth = self.wind.winfo_screenwidth()
      self.mainScreenHeight = self.wind.winfo_screenheight()
      x = 400
      y = 100
      xPosition = int( (self.mainScreenWidth / 2) - (x / 2) )
      yPosition = int( (self.mainScreenHeight/ 2) - (y / 2) )
      myGeometry = "{}x{}+{}+{}".format(x, y, xPosition, yPosition)
      self.wind.geometry(myGeometry)
      self.wind.iconbitmap("Icons\key.ico")
      self.wind.resizable(False, False)
      self.wind.configure(bg= UIPassword.colors["blue0"])
      self.wind.title("User Password")
      '''
      # frame del password
      '''
      self.framePasswords = tk.Frame(
        self.wind,
        bg= UIPassword.colors["blue0"]
      )
      tk.Label(
        self.framePasswords,
        text= 'Password: ',
        bg= UIPassword.colors["blue0"],
        fg= 'white',
        font=("Cascadia Code", 12, 'bold')
      ).grid(row=0, column=0, padx=(10,10), pady=(10,10))

      self.userPassword = tk.Entry(
        self.framePasswords,
        justify= "center",
        show= '*',
        font=("Cascadia Code", 12, 'bold')
      )
      self.userPassword.focus()
      self.userPassword.grid(row=0, column=1, padx=(0,5))

      self.frameMainBtns = tk.Frame(
        self.framePasswords,
        bg = UIPassword.colors['blue0']
      )
      self.btnExit = tk.Button(
        self.frameMainBtns,
        text= 'Exit',
        command= self.wind.destroy,
        width=15,
        font=("Cascadia Code", 10, 'bold'),
        bg= UIPassword.colors['red0'],
        fg= UIPassword.colors['white0']
      )
      self.btnExit.grid(row= 0, column=0, padx=(5,5))

      self.btnAccess = tk.Button(
        self.frameMainBtns,
        text= 'Access',
        width= 15,
        font=("Cascadia Code", 10, 'bold'),
        bg= UIPassword.colors['green0'],
        fg= UIPassword.colors['white0'],
        command= self.verifyUser
      )
      self.btnAccess.grid(row=0, column=1, padx=(5,5))
      

      self.frameMainBtns.grid(row=1, column=0, columnspan=3)
      self.framePasswords.grid(row=0, column=0, columnspan=3)
  
  def verifyUser(self):
    userPassword = self.userPassword.get()
    dbResponse = validatePassword(userPassword)
    if dbResponse == False:
      messagebox.showwarning("Wrong Password", "Verifica la contraseña")
    else:
      self.framePasswords.destroy()
      app = uiUser.uiUser(self.wind)