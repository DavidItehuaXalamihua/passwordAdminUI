import tkinter as tk
from tkinter import Label, Menu, messagebox
from tkinter import ttk
from tkinter.constants import DISABLED
from interfaces.otrasInterfaces.functions.uiFunctions import createNewRecordDB, getBgColor, getPasswords, deleteRecord, copyData, openUrl
from interfaces.otrasInterfaces.btnsInterfaces.createRecord import createNewRecord
from interfaces.otrasInterfaces.btnsInterfaces.updateRecord import UpdateRecord
from interfaces.otrasInterfaces.btnsInterfaces.Download import DownloadData
from interfaces.otrasInterfaces.btnsInterfaces.MenuApp import MenuAppIntf
import xlwings as xl


class uiUser():
  colors = {
    "bg": getBgColor(),
    "red0": "#d00000",
    "red1": "#9d0208",
    "white0": "#ffffff",
    "blue0": "#006466",
    "orange0": "#ff5400",
    "green0": "#007200",
    "green1": "#004b23"
  }
  def __init__(self, wind) -> None:
      super().__init__()
      self.wind = wind
      self.wind.title("Password Admin")

      x = 1013
      y = 350
      self.mainScreenWidth = self.wind.winfo_screenwidth()
      self.mainScreenHeight = self.wind.winfo_screenheight()
      xPosition = int( (self.mainScreenWidth / 2) - (x / 2) )
      yPosition = int( (self.mainScreenHeight/ 2) - (y / 2) )
      myGeometry = "{}x{}+{}+{}".format(x, y, xPosition, yPosition)
      self.wind.geometry(myGeometry)
      self.wind.iconbitmap(r"Icons/admin.ico")
      self.wind.config(bg= uiUser.colors["bg"])
      
      #Menu
      MenuAppIntf(self.wind)

      def callUiCreateNewRecord():
        createNewRecord(self.wind)

      def returnDataRowSelected():
        selection = self.treeViewPasswords.focus()
        value = self.treeViewPasswords.item(selection, "values")
        return value
      
      def copyUserData():
        user = returnDataRowSelected()[1]
        copyData(user)
        messagebox.showinfo(
          'Copied User',
          'The user name have been copy'
        )
      
      def copyPasswordData():
        password = returnDataRowSelected()[2]
        copyData(password)
        messagebox.showinfo(
          'Copied Password',
          'The password value was copied'
        )
      
      def getAndOpenUrl():
        urlPath = returnDataRowSelected()[3]
        openUrl(urlPath)

      def callUiUpdateRecord():
        selection = self.treeViewPasswords.focus()
        value = self.treeViewPasswords.item(selection, "values")
        if len(value) == 0:
          messagebox.showinfo(
            "No Data Selected", 
            "To update a record you have to select an item")
        else:
          UpdateRecord(
            self.wind, 
            rPlatform = value[0], 
            rUser = value[1],
            rPassword = value[2],
            rUrl = value[3],
            rComment = value[4] 
            )

      def menuRightClickMenu(event):
        item = self.treeViewPasswords.focus()
        itemSelected = self.treeViewPasswords.item(item, "values")

        if len(itemSelected) == 0:
          messagebox.showinfo(
            'No record selected', 
            'In order to get the data from the records you have to select one'
            )
        else:
          try: 
            m.tk_popup(event.x_root, event.y_root) 
          finally: 
            m.grab_release() 

      def deleteRecordUI():
        selection = self.treeViewPasswords.focus()
        value = self.treeViewPasswords.item(selection, "values")
        if len(value) == 0:
          messagebox.showinfo("No Data Selected", "To delete a record you have to select an item")
        else:
          mensaje = messagebox.askokcancel("Delete Record", "you will delete a record, would you like to continue?")
          if mensaje:
            deleteRecord(value[0])
            self.deleteAndUploadItems()
          else:
            messagebox.showinfo("Cancel", "The process was canceled")

      def btnDownloadData():
        data = getPasswords()
        wb = xl.Book()
        ws = wb.sheets[0]

        xl.books.active
        xl.sheets.active
        headers = ['Platform', 'User', 'Password', 'URL', 'Comment']
        ws.range((1,1)).value = headers
        ws.range((2,1)).value = data
        messagebox.showinfo("Downloaded Data", "the data have been downloaded into a excel file")

      self.mainBtnsCrud = tk.Frame(
        self.wind,
        bg = uiUser.colors["bg"]
      )

      self.btnSalir = tk.Button(
        self.mainBtnsCrud,
        bg= uiUser.colors["red0"],
        command= self.wind.destroy
      )

      self.btnCreate = tk.Button(
        self.mainBtnsCrud,
        bg= uiUser.colors["blue0"],
        command=  callUiCreateNewRecord
      )

      self.btnUpdate = tk.Button(
        self.mainBtnsCrud,
        bg= uiUser.colors["blue0"],
        command= callUiUpdateRecord
      )

      self.btnDeleteRecord = tk.Button(
        self.mainBtnsCrud,
        bg= uiUser.colors["orange0"],
        command= deleteRecordUI
      )

      self.btnDownload = tk.Button(
        self.mainBtnsCrud,
        bg= uiUser.colors["green0"],
        command= btnDownloadData
      )

      btnObjs = [
        self.btnSalir, self.btnCreate, 
        self.btnUpdate, self.btnDeleteRecord, 
        self.btnDownload
        ]
      
      txtBtns = ["Exit", "Create", "Update", "Delete", "Download"]
      for x in range(len(btnObjs)):
        btnObjs[x].config(
          text = txtBtns[x],
          font= ("Cascadia code", 12, "bold"),
          fg= uiUser.colors["white0"],
          width= 15
          )
        btnObjs[x].grid(row=0, column=x, padx=(5,5))

      self.mainBtnsCrud.grid(row = 0, column=0, pady=(10, 10))
      '''  
      TREEVIEW
      '''
      self.frameTreeViewPasswords = tk.Frame(
        self.wind,
      )

      self.treeViewPasswords = ttk.Treeview(
        self.frameTreeViewPasswords,
        selectmode= 'browse',
        columns= [f"{x}" for x in range(1,6)],
        show= 'headings',
      )
      
      # set the headers in the treeview
      treevHeaders = ["Plataforma", "User", "Password", "URL", "Comments"]
      for x in range(len(treevHeaders)):
        self.treeViewPasswords.heading(f"{x + 1}", text= treevHeaders[x])
      
      self.treeViewPasswords.grid(row=0, column=0)

      self.treeViewPasswords.bind("<Button-3>",menuRightClickMenu)

      self.frameTreeViewPasswords.grid(row=1, column=0, padx= (5,5), pady=(15,5))
      
      m = Menu(self.treeViewPasswords, tearoff = 0) 
      m.add_command(label ="Copy User", command = copyUserData ) 
      m.add_command(label ="Copy Password", command= copyPasswordData ) 
      m.add_command(label ="Open URL", command= getAndOpenUrl) 

      self.deleteAndUploadItems()

  def deleteAndUploadItems(self):
    #eliminado de los registros previos
    self.data = getPasswords()
    items = self.treeViewPasswords.get_children()
    for item in items:
      self.treeViewPasswords.delete(item)
    
    #carga de los nuevos registros
    for x in self.data:
        self.treeViewPasswords.insert("", 'end', text =x, values =x)    

