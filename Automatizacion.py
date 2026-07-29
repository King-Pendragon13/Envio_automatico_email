#%pip install yfinance
#%pip install pyautogui
#%pip install matplotlib
import yfinance
import matplotlib
yfinance.download
data= yfinance.download(["AAPL"] ,period="6mo")
# AAPL hace referencia a Apple, puede cambiarse las siglas por la empresa que se desea ver
# 6mo hace referencia a 6 meses atras
cierre= data.Close["AAPL"]
cierre.plot()
Maximo= (round(cierre.max(), 2))
Minimo= (round(cierre.min(), 2))
Medio= (round(cierre.mean(), 2))
# El round se utiliza para redondear las cifras a 2 digitos despues del punto decimal
print(Maximo)
print(Minimo)
print(Medio)
#%pip install pyautogui
#%pip install pyperclip
#Se instalan las librerias si aun no se tienen instaladas
import pyautogui
import pyperclip
import webbrowser
import time

time.sleep(5)
pyautogui.position()
#Se usa para saber la posicion del mouse donde se encuentran los botones que se presionaran automaticamente

webbrowser.open("https://mail.google.com/mail/u/0/#sent")
destinatario = "micorreo@hotmail.com"
asunto="Analisis acciones ultimos 6 meses Apple"
Cuerpo= f"""
Buenas noches,
Le envio el analisis solicitado
Saludos cordiales.
Cotizacion máxima: USD {Maximo}
Cotización minima: USD {Minimo}
Valor medio: USD {Medio}

!Estoy al pendiente de cualquier observacion!

"""
time.sleep(6)
pyautogui.PAUSE = 3
pyautogui.click(105,220)
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy(asunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy(Cuerpo)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyautogui.click(844,689)

pyautogui.hotkey("ctrl", "w")
