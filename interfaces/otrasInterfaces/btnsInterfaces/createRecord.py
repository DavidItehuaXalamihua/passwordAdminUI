
import tkinter as tk
from tkinter import Toplevel, font, messagebox
from interfaces.otrasInterfaces.functions.uiFunctions import getBgColor, createNewRecordDB
from interfaces.otrasInterfaces import uiUser

class createNewRecord():

  colors = {
    "bg": getBgColor(),
    "white0": "#ffffff",
    "green0": "#007200",
    "red0": "#d00000",
    "red1": "#9d0208"
  }

  def __init__(self, windowMain):
    super().__init__()
    self.windowMain = windowMain
    self.root = uiUser.uiUser(self.windowMain)
    self.wind = tk.Toplevel()
    self.wind.focus()
    self.wind.grab_set()
    self.wind.iconbitmap(r"Icons/add.ico")
    self.wind.title("Create New Record")
      
    self.x = 480
    self.y = 225
    self.mainScreenWidth = self.wind.winfo_screenwidth()
    self.mainScreenHeight = self.wind.winfo_screenheight()
    self.xPosition = int( (self.mainScreenWidth / 2) - (self.x / 2) )
    self.yPosition = int( (self.mainScreenHeight/ 2) - (self.y / 2) )
    self.myGeometry = "{}x{}+{}+{}".format(self.x, self.y, self.xPosition, self.yPosition)
    self.wind.geometry(self.myGeometry)
    self.wind.resizable(False, False) 
    self.wind.config(bg= createNewRecord.colors["bg"])

    self.entrysNewRecord = tk.Frame(
      self.wind,
      bg= createNewRecord.colors["bg"]
      )

    headers = ["* Platform: ", "* User: ", "* Password: ", "Link / URL: ", "Comments: "]
    for x in range(len(headers)):
      tk.Label(
        self.entrysNewRecord,
        text= headers[x],
        font=("cascadia code", 10, "bold"),
        bg= createNewRecord.colors["bg"],
        fg= createNewRecord.colors["white0"],
        justify= "right",
        anchor='w'
        ).grid(row = x, column= 0,  sticky = "E", padx=(5,5))
      
    # entry platform
    self.ePlatform = tk.Entry(
      self.entrysNewRecord
      )
    self.ePlatform.focus()

    #entry user
    self.eUser = tk.Entry(
      self.entrysNewRecord
      )

    #entry password
    self.ePassword = tk.Entry(
      self.entrysNewRecord
      )

    #entry url
    self.eUrl = tk.Entry(
      self.entrysNewRecord
      )

    #entry comments
    self.eComments = tk.Entry(
      self.entrysNewRecord
      )

    entrys = [self.ePlatform, self.eUser, self.ePassword, self.eUrl, self.eComments]
    for x in range(len(entrys)):
      entrys[x].grid(row = x, column=1)
      entrys[x].config(width=30)
      
    self.createRecord = tk.Button(
      self.entrysNewRecord,
      text = "CREATE RECORD",
      font= ("cascadia code", 11, "bold"),
      bg = createNewRecord.colors["green0"],
      fg = createNewRecord.colors["white0"],
      command= self.verifyEntrys,
      width=40
      )
    self.createRecord.grid(row = 5, column=0, columnspan=2, pady=(15, 15))

    self.entrysNewRecord.grid(row=0, column=0, padx= (10,10), pady=(10,10))
        
    self.wind.mainloop()
  
  def verifyEntrys(self):
    entrys = [self.ePlatform, self.eUser, self.ePassword]
    errors = 0
    for x in entrys:
      if len(x.get()) == 0:
        errors = errors + 1
    
    if errors > 0:
      self.wind.geometry("480x380")
      self.labelNotifications = tk.Label(
        self.entrysNewRecord,
        text = "The filds marked\nwith '*' are required",
        font = ("cascadia code", 12, "bold"),
        bg = createNewRecord.colors["red0"],
        fg = createNewRecord.colors["white0"]
      )
      self.labelNotifications.grid(
        row = 6, 
        column=0, 
        columnspan=2, 
        rowspan=2, 
        pady=(15,15), 
        padx=(15, 15)
        ) 
    else:
      createNewRecordDB(
        f'{self.ePlatform.get()}'.strip(), 
        f'{self.eUser.get()}'.strip(), 
        f'{self.ePassword.get()}'.strip(),
        f'{self.eUrl.get()}'.strip(),
        f'{self.eComments.get()}'.strip()
        )
      self.ePlatform.delete(0,"end")
      deleteValues = [
        self.ePlatform, 
        self.eUser, 
        self.ePassword,
        self.eUrl,
        self.eComments]
      [x.delete(0, "end") for x in deleteValues]
      self.ePlatform.focus()
      self.root.deleteAndUploadItems()
      try:
        self.wind.geometry(self.myGeometry)
        self.labelNotifications.destroy
      except:
        pass



