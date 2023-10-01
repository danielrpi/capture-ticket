# IMPORTAÇÕES
from tkinter.filedialog import *
import customtkinter  
import img2pdf 
from PIL import Image 
import os 
import pyscreenshot




def capture():
    image = pyscreenshot.grab(bbox=(50, 300, 770, 700)) 
    image.save("trash.png")
    img = Image.open('trash.png') 
    save_path = asksaveasfilename()
    pdf_bytes = img2pdf.convert(img.filename) 
    file = open(save_path+'.pdf', "wb") 
    file.write(pdf_bytes) 
    img.close() 
    file.close() 


janela =customtkinter.CTk() 
janela.geometry("300x150")
janela.title("CAPTURA BOLETO")
button = customtkinter.CTkButton(text='CAPTURAR',master=janela, corner_radius=10, command=capture)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)




janela.mainloop()