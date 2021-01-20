import tkinter as tk
from ..MenuUi.changePassword import ChangePasswordUI

class MenuAppIntf():
  def __init__(self, master):
    super().__init__()
    self.master = master
    self.mainMenu = tk.Menu(self.master, tearoff=0)
    self.master.config(menu= self.mainMenu)

    self.menuSettings = tk.Menu(self.mainMenu, tearoff=0)
    self.menuSettings.add_command(label= "Change Password", command= ChangePasswordUI)
    
    self.mainMenu.add_cascade(label= "Settings", menu= self.menuSettings)