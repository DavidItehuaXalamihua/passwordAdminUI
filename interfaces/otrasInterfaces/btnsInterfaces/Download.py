import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
from interfaces.otrasInterfaces.functions.uiFunctions import getBgColor

class DownloadData():
  
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
      self.win = wind
      self.topWind = tk.Toplevel()
      self.topWind.resizable(False, False)
      self.topWind.grab_set()
      self.topWind.iconbitmap(r"Icons\download.ico")
      self.topWind.title("Download Data")

      x = 715
      y = 225
      self.mainScreenWidth = self.topWind.winfo_screenwidth()
      self.mainScreenHeight = self.topWind.winfo_screenheight()
      xPosition = int( (self.mainScreenWidth / 2) - (x / 2) )
      yPosition = int( (self.mainScreenHeight/ 2) - (y / 2) )
      myGeometry = "{}x{}+{}+{}".format(x, y, xPosition, yPosition)
      self.topWind.geometry(myGeometry)
      self.topWind.config(bg= DownloadData.colors['bg'])

      def fileBrowser():
        filedialog.asksaveasfile()


      def fileBrowserFunction(event):
        entry = self.entryFilePath.get()
        if len(entry) == 0:
          fileBrowser()
        else:
          mensaje = messagebox.askyesno("Change Path", "Would you like change the file path?")
          if mensaje:
            fileBrowser()
          else:
            print("do nothing")
          

      self.frameBtnAndEntrys = tk.Frame(
        self.topWind,
        bg= DownloadData.colors['bg']
      )

      labels = ["*File Path:", "*File Name:"]
      for x in range(len(labels)):
        tk.Label(
          self.frameBtnAndEntrys,
          text= labels[x],
          font= ('Cascadia Code', 11, 'bold'),
          fg= DownloadData.colors['white0'],
          bg= DownloadData.colors['bg']
        ).grid(row=x, column=0, sticky= 'E', padx=(5,5))
      
      self.entryFilePath = tk.Entry(
        self.frameBtnAndEntrys,
        font= ("Cascadia Code",11, 'bold'),
        width=50
      )
      self.entryFilePath.bind("<1>", fileBrowserFunction)
      self.entryFilePath.grid(row=0, column=1, pady=(10,10))
      
      self.entryFileName = tk.Entry(
        self.frameBtnAndEntrys,
        font= ("Cascadia Code",11, 'bold'),
        width=50
      )
      self.entryFileName.grid(row=1, column=1)

      self.frameBtnAndEntrys.grid(row=0, column=0, pady=(15,15), padx=(10,10))

      self.btnDownload = tk.Button(
        self.topWind,
        text= 'Download\nData',
        bg= DownloadData.colors['green0'],
        font= ("Cascadia Code", 13, "bold"),
        fg= DownloadData.colors['white0'],
        width= 30
      )
      self.btnDownload.grid(rowspan=1, column=0, pady=(15,15))
      

      self.topWind.mainloop()
