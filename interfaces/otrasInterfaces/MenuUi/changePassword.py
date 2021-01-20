from sqlite3.dbapi2 import Row
from tkinter import IntVar, READABLE, Toplevel, font
import tkinter as tk
from tkinter.constants import END
from interfaces.otrasInterfaces.functions.uiFunctions import changePasswordDB, getBgColor

class ChangePasswordUI():
  
  colors = {
    "bg": getBgColor(),
    "white0": "#ffffff",
    "green0": "#007200",
    "red0": "#d00000",
    "red1": "#9d0208"
  }

  def __init__(self) -> None:
      super().__init__()
      self.topWind = Toplevel()
      self.topWind.grab_set()
      self.topWind.title("Change Password")
      self.topWind.config(bg= ChangePasswordUI.colors['bg'])
      self.topWind.iconbitmap("Icons/key.ico")

      self.x = 515
      self.y = 350
      self.mainScreenWidth = self.topWind.winfo_screenwidth()
      self.mainScreenHeight = self.topWind.winfo_screenheight()
      self.xPosition = int( (self.mainScreenWidth / 2) - (self.x / 2) )
      self.yPosition = int( (self.mainScreenHeight/ 2) - (self.y / 2) )
      self.myGeometry = "{}x{}+{}+{}".format(self.x, self.y, self.xPosition, self.yPosition)
      self.topWind.geometry(self.myGeometry)
      self.topWind.resizable(False, False)

      def seeAndHidePassword():
        answer = self.responseSeePassword.get()
        if answer == 1:
          for x in range(len(self.entrysData)):
            tk.Label(
              self.frameLabelsAndEntrys,
              text= self.entrysData[x].get(),
              bg = ChangePasswordUI.colors['bg']
            ).grid()


      self.frameLabelsAndEntrys = tk.Frame(
        self.topWind,
        bg= ChangePasswordUI.colors['bg']
      )
      labelsText = ['Old Password:', 'New Password:']
      for x in range(len(labelsText)):
        tk.Label(
          self.frameLabelsAndEntrys,
          text = labelsText[x],
          font= ('Cascadia Code', 11, 'bold'),
          bg= ChangePasswordUI.colors['bg'],
          fg= ChangePasswordUI.colors['white0']
        ).grid(row= x, column=0, padx=(10, 10), sticky= 'E')

      self.oldPassword = tk.Entry(
        self.frameLabelsAndEntrys
      )
      self.oldPassword.focus()

      self.newPassword = tk.Entry(
        self.frameLabelsAndEntrys
      )
      
      self.entrysData = [self.oldPassword, self.newPassword]
      for x in range(len(self.entrysData)):
        self.entrysData[x].config(
          font= ('Cascadia Code', 11),
          justify= 'center',
          show= '*',
          width= 30
        )
        self.entrysData[x].grid(
          row= x, column=1, pady=(5,5)
        )
      
      self.responseSeePassword = IntVar()
      self.seePassword = tk.Checkbutton(
        self.frameLabelsAndEntrys,
        variable= self.responseSeePassword,
        text= "See Password",
        font= ('Cascadia Code', 11, 'bold'),
        bg= ChangePasswordUI.colors['bg'],
        fg= ChangePasswordUI.colors['white0'],
        command= seeAndHidePassword
      )
      self.seePassword.grid(row = 2, column=0, pady=(10, 10), padx=(10, 10))

      self.frameLabelsAndEntrys.grid(row=0, column=0, pady=(10, 10))

      self.topWind.mainloop()
