import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os, sys

from archer_class import Archer

gui = tk.Tk()
gui.geometry("500x500")
gui.title("Arhcery Classifications")

label = ttk.Label(text="Archery Classifications")
label.config(anchor=CENTER)
label.pack(fill=tk.X, padx=5, pady=5)

bowtypes = ["Recurve","Barebow","Compound","Longbow"]
genders = ["Male","Female"]
age_cats = ["Junior","Senior"]
rounds = [file.replace(".csv","").title() for file in os.listdir("rounds")]
 
def combobox_func(options):
    selected = tk.StringVar()
    box = ttk.Combobox(textvariable=selected)
    box["values"] = options
    box["state"] = "readonly"
    box.pack(fill=tk.X, padx=100, pady=5)
    return box
   
bowtype_box = combobox_func(bowtypes)
gender_box = combobox_func(genders)
age_cat_box = combobox_func(age_cats)
round_box = combobox_func(rounds)

def output_scores():
    df = pd.read_csv("rounds/" + classification_round.lower() + ".csv")
    score_needed = list(zip(df["rank"],df[archer.bowtype+"_"+archer.gender]))
    for i in range(len(score_needed)):
        label = ttk.Label(text=f"{score_needed[i][0]} : {score_needed[i][1]}")
        label.config(anchor=CENTER)
        label.pack(fill=tk.X, padx=5, pady=5)
        
def set_attributes():
    bowtype = bowtype_box.get()
    gender = gender_box.get()
    age_cat = age_cat_box.get()
    global classification_round, archer
    classification_round = round_box.get()
    try:
        archer = Archer(bowtype,gender,age_cat)
    except NameError():
        sys.exit("NameError")
    output_scores()

Button(gui,text="Set",command=set_attributes).pack()

gui.mainloop()




