import sqlite3 as sql
from tkinter import messagebox
import pyperclip
import os
import codecs

def prettierTxt():
  try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
  except:
    pass

dbPath = r'Database/database.db'

def changePasswordDB(oldPassword: str, newPassword:str):
  conn = sql.connect(dbPath)
  cursor = conn.cursor()
  validateExistPassword = f'SELECT COUNT(*) FROM access WHERE password= "{oldPassword}"'
  registros = cursor.execute(validateExistPassword).fetchall()
  if registros[0][0] == 1:
    query = f'UPDATE access SET password= "{newPassword}" WHERE password = "{oldPassword}"'
    cursor.execute(query)
    conn.commit()
    conn.close()
    messagebox.showinfo(
      'Password Changed',
      'The password was changed successfully')
  else:
    messagebox.showinfo(
      'Value Not Found',
      'The password you trying to change was not found, verify the old password.'
    )


def validatePassword(password: str) -> bool:
  dbPath = r'Database\database.db'
  conn = sql.connect(dbPath)

  cursor = conn.cursor()
  query = f'SELECT * FROM access WHERE password = "{password}"'
  cursor.execute(query)
  data = cursor.fetchall()
  cursor.close()

  if len(data) == 0:
    return False
  else:
    return True
  
def getBgColor() -> str:
  dbPath = r'Database\database.db'
  conn = sql.connect(dbPath)

  cursor = conn.cursor()
  query = 'SELECT * FROM bgColor'
  cursor.execute(query)
  data = cursor.fetchone()
  cursor.close()
  return data[0]

def getPasswords():
  dbPath = r'Database\database.db'
  conn = sql.connect(dbPath)
  cursor = conn.cursor()
  query = 'SELECT * FROM userPasswords ORDER BY platform'
  cursor.execute(query)
  data = cursor.fetchall()
  cursor.close()
  return data

def createNewRecordDB(platform, user, password, url= "", commets=""):
  try:
    dbPath = r'Database\database.db'
    conn = sql.connect(dbPath)
    cursor = conn.cursor()
    query = f'''
    INSERT INTO userPasswords (platform, user, password, url, comments)
    VALUES ("{platform}", "{user}", "{password}", "{url}", "{commets}") 
    '''
    cursor.execute(query)
    conn.commit()
    cursor.close()
    messagebox.showinfo("Info recorded", "The record was succesfuly created")
  except sql.IntegrityError:
    messagebox.showerror("Record","The record was created previously, you should upgrate that record")

def updateRecordDB(primaryKey, newPlatform, newUser, newPassword, newUrl = "", newComments = ""):
  dbPath = r'Database/database.db'
  conn = sql.connect(dbPath)
  cursor = conn.cursor()
  query = f'''
  UPDATE 
  userPasswords 
  SET 
  platform = "{newPlatform}", 
  user = "{newUser}", 
  password = "{newPassword}", 
  url = "{newUrl}",
  comments = "{newComments}"
  WHERE
  platform = "{primaryKey}"
  '''
  cursor.execute(query)
  conn.commit()
  conn.close()

def deleteRecord(primaryKey):
  dbPath = r'Database/database.db'
  conn = sql.connect(dbPath)
  cursor = conn.cursor()
  query = f'''
  DELETE FROM userPasswords WHERE platform = "{primaryKey}"
  '''
  cursor.execute(query)
  conn.commit()
  conn.close()

def copyData(data: str) -> str:
  pyperclip.copy(data)

def openUrl(url = ""):
  if len(url) == 0:
    messagebox.showinfo(
      'URL Empy',
      'The database does´not have an url to open in the web browser'
    )
  else:
    try:
      os.startfile(url)
    except AssertionError:
      messagebox.showinfo(
        'URL Error',
        'The URL path ist'
      )