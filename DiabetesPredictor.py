
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from tkinter import *
import os
import sysconfig

 

global screen3
screen3 = Tk()
screen3.title("Main Window")
        
Label(screen3, text = "Welcome to Diabetes Prediction",fg = 'Blue', font = ('Calibari',30)).pack()
Label(screen3,text = "").pack()
Label(screen3, text = "Diabetes is a condition in which the amount of glucose (sugar) in your blood is too high because your body cannot use it properly. \nThis happens because your body either cannot use or make a hormone called insulin,which is responsible for turning sugar into food for your body's cells.").pack()
Label(screen3,text = "").pack()
        
Label(screen3, text = "Factors Affecting Diabetes",fg = 'Red',font=('Calibari',25) ).pack()
Label(screen3,text = "").pack()

def bloodPressure():
    global btn1
    btn1=Toplevel(screen3)
    btn1.title("Know more about Blood Pressure ")
Button(screen3,text = "Blood Pressure",command=bloodPressure,fg = 'Green',font = ('Calibari',16)).pack()
Label(screen3,text="Having diabetes raises your risk of heart disease, stroke, kidney disease and other health problems. Having high blood pressure also raises this risk.\n If you have diabetes and high blood pressure together, this raises your risk of health problems even more.If you have diabetes, your doctor will want to be sure that your blood pressure is very well controlled. \nThis means that they will probably want your blood pressure to be below 130 over 80.").pack()
         
def age():
    global btn2
    btn2=Toplevel(screen3)
    btn2.title("How Age affects diabetes?")
Button(screen3,text = "Age",fg = 'Green',command=age,font = ('Calibari',16)).pack()
Label(screen3,text="Diabetes in older adults is a growing public health burden. The unprecedented aging of the world's population is a major contributor to the diabetes epidemic, \nand older adults represent one of the fastest growing segments of the diabetes population").pack()
       
def bmi():
    global btn3
    btn3=Toplevel(screen3)
    btn3.title("Know more about BMI")
Button(screen3,text = "BMI",fg = 'Green',command=bmi,font = ('Calibari',16)).pack()
Label(screen3,text="An increase in body fat is generally associated with an increase in risk of metabolic diseases such as type 2 diabetes mellitus, hypertension and dyslipidaemia  .\n Body mass index (BMI) criteria are currently the primary focus in obesity treatment recommendations, with different treatment cutoff points based upon the presence or absence of obesity-related comorbid disease ").pack()
       
def glucose():
    global btn4
    btn4=Toplevel(screen3)
    btn4.title("How Glucose affects diabetes?")
Button(screen3,text = "Glucose",command=glucose,fg = 'Green',font = ('Calibari',16)).pack()
Label(screen3,text="The presence of glucose in the blood stimulates the pancreas to secrete insulin. ").pack()
        
def insulin():
    global btn5
    btn5=Toplevel(screen3)
    btn5.title("How Insulin affects diabetes?")
Button(screen3,text = "Insulin",command=insulin,fg = 'Green',font = ('Calibari',16)).pack()
Label(screen3,text="The insulin facilitates the transport of glucose from the blood into the cells where it is used. \nIf not enough insulin is secreted, the glucose blood level remains high.\n Consistently high blood glucose levels caused by insufficient insulin is diabetes mellitus.").pack()
      
def dpf():
    global btn6
    btn6=Toplevel(screen3)
    btn6.title("Know more about DiabetesPedigreeFunction")
Button(screen3,text = "DiabetesPedigreeFunction",command=dpf,fg = 'Green',font = ('Calibari',16)).pack()
Label(screen3,text="It provides some data on diabetes mellitus history in relatives and the genetic relationship of those relatives to the patient").pack()

def skin():
    global btn7
    btn7=Toplevel(screen3)
    btn7.title("How skin thickness affects diabetes?")
Button(screen3,text = "SkinThickness",command=skin,fg = 'Green',font = ('Calibari',16)).pack()
Label(screen3,text="Glucose measurement from different skin areas might be influenced by changes in skin texture due to several environmental confounders").pack()
        
def pregnancy():
    global btn8
    btn8=Toplevel(screen3)
    btn8.title("How pregnancy affects diabetes?")
Button(screen3,text = "Pregnancies",command=pregnancy,fg = 'Green',font = ('Calibari',16)).pack()
Label(screen3,text="The effects of pregnancy on acute metabolic complications of diabetes may have important consequences for both mother and fetus.").pack()
Label(screen3,text="").pack()
        
def enter():
    global root
    root=Toplevel(screen3)
    root.title("Diabetes Prediction")

    label_1 = Label(root, text = 'BloodPressure')
    label_2 = Label(root, text = 'Age')
    label_3 = Label(root, text = 'BMI')
    label_4 = Label(root, text = 'Glucose')
    label_5 = Label(root, text = 'Insulin')
    label_6 = Label(root, text = 'DiabetesPedigreeFunction')
    label_7 = Label(root, text = 'SkinThickness')
    label_8 = Label(root, text = 'Pregnancies')


    entry_1 = Entry(root)
    entry_2 = Entry(root)
    entry_3 = Entry(root)
    entry_4 = Entry(root)
    entry_5 = Entry(root)
    entry_6 = Entry(root)
    entry_7 = Entry(root)
    entry_8 = Entry(root)


    label_1.grid(row = 0, sticky = E)
    label_2.grid(row = 1, sticky = E)
    label_3.grid(row = 2, sticky = E)
    label_4.grid(row = 3, sticky = E)
    label_5.grid(row = 4, sticky = E)
    label_6.grid(row = 5, sticky = E)
    label_7.grid(row = 6, sticky = E)
    label_8.grid(row = 7, sticky = E)


    entry_1.grid(row = 0 , column = 1)
    entry_2.grid(row = 1 , column = 1)
    entry_3.grid(row = 2 , column = 1)
    entry_4.grid(row = 3 , column = 1)
    entry_5.grid(row = 4 , column = 1)
    entry_6.grid(row = 5 , column = 1)
    entry_7.grid(row = 6 , column = 1)
    entry_8.grid(row = 7 , column = 1)

    

    def pri():
        df1 = pd.read_csv("diabetes.csv")
        a=float(entry_1.get())
        b=float(entry_2.get())
        c=float(entry_3.get())
        d=float(entry_4.get())
        e=float(entry_5.get())
        f=float(entry_6.get())
        g=float(entry_7.get())
        h=float(entry_8.get())
        
        data = [a,b,c,d,e,f,g,h]
        data=np.array(data)
        x =['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
        y=['Output']

        from sklearn.model_selection import train_test_split
        X_train,X_test,y_train,y_test=train_test_split(df1.drop('Outcome',axis=1),df1['Outcome'],test_size=0.20,random_state=101)

        from sklearn.linear_model import LogisticRegression
        LRModel=LogisticRegression()
        LRModel.fit(X_train,y_train)
        predictions_diabetes=LRModel.predict(X_test)

        from sklearn.metrics import classification_report, confusion_matrix

        x=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
        paitentid_54=pd.DataFrame([data],columns=x)
        predictions_diabetes=LRModel.predict(paitentid_54)
        
        return predictions_diabetes


    var = IntVar()
    var.set(0)

    button2 = Button(root, text="Predict",command = lambda: var.set(pri()))
    button2.grid(columnspan = 3)

    lbl = Label(root, textvariable=var)
    lbl.grid(row = 10, sticky = E)
        
Button(screen3,text = "Prediction",command =enter ).pack()
Label(screen3,text="").pack()

         

screen3.mainloop()
    

