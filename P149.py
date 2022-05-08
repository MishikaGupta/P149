# -*- coding: utf-8 -*-
"""
Created on Wed May  4 19:44:38 2022

@author: Beautiful Mishika
"""

from tkinter import *
import random 

root=Tk()
root.title("Random Word")
root.geometry("500x500")

label = Label(root)

def random_word():
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    random_number1 = random.randint(0, 25)
    random_number2 = random.randint(0, 25)
    random_number3 = random.randint(0, 25)
    random_number4 = random.randint(0, 25)
    random_number5 = random.randint(0, 25)
    
    alpha1 = list[random_number1]
    alpha2 = list[random_number2]
    alpha3 = list[random_number3]
    alpha4 = list[random_number4]
    alpha5 = list[random_number5]
    
    label["text"]= alpha1 + alpha2 + alpha3 + alpha4 + alpha5
    
btn=Button(root, text="Generate a random word", command=random_word)

btn.place(rely=0.5, relx=0.5, anchor=CENTER)
label.place(rely=0.6, relx=0.6, anchor=CENTER)

root.mainloop()