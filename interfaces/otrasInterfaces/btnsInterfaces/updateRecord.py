
import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel, font, messagebox
from interfaces.otrasInterfaces.functions.uiFunctions import getBgColor, updateRecordDB
from interfaces.otrasInterfaces import uiUser


class UpdateRecord():

  colors = {
    "bg": getBgColor(),
    "white0": "#ffffff",
    "green0": "#007200",
    "red0": "#d00000",
    "red1": "#9d0208"
  }

  def __init__(self, windowMain, rPlatform, rUser, rPassword, rUrl, rComment):
    super().__init__()
    self.windowMain = windowMain
    self.rPlatform = rPlatform
    self.rUser = rUser
    self.rPassword = rPassword
    self.rUrl = rUrl
    self.rComments = rComment
    self.root = uiUser.uiUser(self.windowMain)
    self.wind = tk.Toplevel()
    self.wind.focus()
    self.wind.grab_set()
    self.wind.iconbitmap(r"Icons/captcha.ico")
    self.wind.title("Update Record")
      
    self.x = 600
    self.y = 350
    self.mainScreenWidth = self.wind.winfo_screenwidth()
    self.mainScreenHeight = self.wind.winfo_screenheight()
    self.xPosition = int( (self.mainScreenWidth / 2) - (self.x / 2) )
    self.yPosition = int( (self.mainScreenHeight/ 2) - (self.y / 2) )
    self.myGeometry = "{}x{}+{}+{}".format(self.x, self.y, self.xPosition, self.yPosition)
    self.wind.geometry(self.myGeometry)
    self.wind.resizable(False, False) 
    self.wind.config(bg= UpdateRecord.colors["bg"])
    self.frameWholeData = tk.Frame(
      self.wind,
      bg= UpdateRecord.colors['bg']
    )
    
    labelsRows = ['Platform:', 'User:', 'Password:', 'URL:', 'Comments:']
    for x in range(len(labelsRows)):
      tk.Label(
        self.frameWholeData,
        text = labelsRows[x],
        font= ('Cascadia Code', 11, 'bold'),
        fg = UpdateRecord.colors['white0'],
        bg= UpdateRecord.colors['bg']
      ).grid(row=x + 1 , column=0, padx=(10, 10), pady=(2,5), sticky= 'E')
    
    labelsColumns = ['Old Value', 'New Value']
    for x in range(len(labelsColumns)):
      tk.Label(
        self.frameWholeData,
        text = labelsColumns[x],
        font= ('Cascadia Code', 11, 'bold'),
        fg = UpdateRecord.colors['white0'],
        bg= UpdateRecord.colors['bg'],
        justify= 'center'
      ).grid(row= 0, column= 1 + x, padx=(10, 10))

    
    
    self.oldRecPlatform = tk.Entry(
      self.frameWholeData
    )
    # self.oldRecPlatform.insert(0, f'{self.rPlatform}')

    self.oldRecUser = tk.Entry(
      self.frameWholeData
    )

    self.oldRecPassword = tk.Entry(
      self.frameWholeData
    )

    self.oldRecUrl = tk.Entry(
      self.frameWholeData
    )

    self.oldRecComment = tk.Entry(
      self.frameWholeData
    )

    contenedorData = [ 
      self.rPlatform, self.rUser,
      self.rPassword, self.rUrl, self.rComments ]

    self.oldRecData = [
      self.oldRecPlatform, self.oldRecUser, 
      self.oldRecPassword, self.oldRecUrl, self.oldRecComment
    ]

    for x in range(len(self.oldRecData)):
      self.oldRecData[x].insert(0, f'{contenedorData[x]}')
      self.oldRecData[x].config(
        width= 20,
        state= 'readonly',
        justify= 'left',
        font= ('Cascadia Code', 11, 'bold')
        )
      self.oldRecData[x].grid(row= x + 1, column=1, padx= (5,5))

    self.newPlatform = tk.Entry(
      self.frameWholeData
    )
    self.newPlatform.focus()

    self.newUser = tk.Entry(
      self.frameWholeData
    )

    self.newPassword = tk.Entry(
      self.frameWholeData
    )

    self.newUrl = tk.Entry(
      self.frameWholeData
    )

    self.newComment = tk.Entry(
      self.frameWholeData
    )

    self.newDataFields = [
      self.newPlatform, self.newUser, self.newPassword, self.newUrl, self.newComment
    ]

    for x in range(len(self.newDataFields)):
      self.newDataFields[x].config(
        width= 20,
        justify= 'left',
        font= ('Cascadia Code', 11, 'bold')
      )
      self.newDataFields[x].grid(row= x + 1, column= 2, padx=(5,5))

    self.frameWholeData.grid(row = 0, column= 0, pady= (10, 10))

    self.btnUpdate = tk.Button(
      self.wind,
      text = 'Update Data',
      font= ('Cascadia Code', 15, 'bold'),
      width= 25,
      bg= UpdateRecord.colors['green0'],
      fg= UpdateRecord.colors['white0'],
      command= self.validateUpdateInformation
    )
    self.btnUpdate.grid(row=1, column=0, pady=(15, 15))

  def validateUpdateInformation(self):
    self.originalData = [
      self.rPlatform, self.rUser, self.rPassword, 
      self.rUrl, self.rComments
    ]
    modificatedData = 0
    for x in self.newDataFields:
      if len(x.get()) > 0:
        modificatedData = modificatedData + 1
    
    self.newValues = []

    if modificatedData == 0:
      messagebox.showinfo('Modificated Data', 'no data modificated found')
    else:
      for x in range(len(self.newDataFields)):
        if self.newDataFields[x].get() != '':
          self.newValues.append(self.newDataFields[x].get())
        else:
          self.newValues.append(self.originalData[x])

    updateRecordDB(
      self.rPlatform, 
      self.newValues[0],
      self.newValues[1],
      self.newValues[2],
      self.newValues[3],
      self.newValues[4])

    self.root.deleteAndUploadItems()

    messagebox.showinfo('updated information', 'Information updated with succed')
    self.wind.destroy()
    self.wind.mainloop()