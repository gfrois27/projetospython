import win32com.client as win32
import pandas as pd

listap=pd.read_excel('listaemail.xlsx')
# criar a integração com outlook
outlook = win32.Dispatch('outlook.application')

# criar um email
email = outlook.CreateItem(0)




# configurar as informações do seu e-mail
email.To = 'guilhermefrois15@yahoo.com.br'
email.Subject = 'test'
email.HTMLBody = """
deu bom
"""
email.Send()
print("email enviado")