from tkinter import *
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from tkinter import messagebox
import os
dataset = [None,"iris"]

files = ["Datasets"]+[i for i in list(os.listdir("C:\\Users\SHIKHAR\Desktop\A\Project\Application")) if ".csv" in i and i[:-4].lower() not in dataset]+[None]
def m():
        df=pd.read_csv(dataset[a.get()]+".csv")
        X=df.iloc[:,:-1]
        Y=df.iloc[:,-1]
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30,random_state=43)
        hi(X_train,X_test,Y_train,Y_test)
def hi(X_train,X_test,Y_train,Y_test):
    frame=Toplevel()
    cols=list(X_train.columns)
    e={}
    i=0
    menu=["Decision Tree Classifier","Random Forest Classifier","Logistic Regression"]
    reg=StringVar()
    reg.set(menu[0])
    for i in range(len(cols)):
        l=Label(frame,text=cols[i],font="Times 15").grid(row=3+i,column=0,pady=10)
        e[i]=StringVar()
        en=Entry(frame,textvariable=e[i]).grid(row=3+i,column=1,pady=10)
    def clear():
        for i in range(len(cols)):
            e[i].set("")
    def predict():
        plist=[]
        r=reg.get()
        try:
            for i in range(len(cols)):
                plist.append(float(e[i].get()))
            if r == "Decision Tree Classifier":
                 dtc=DecisionTreeClassifier()
                 dtc.fit(X_train.values,Y_train)
                 score=dtc.score(X_test.values,Y_test)
                 pr=dtc.predict([plist])
            elif r == "Random Forest Classifier":
                 rfc=RandomForestClassifier()
                 rfc.fit(X_train.values,Y_train)
                 score=rfc.score(X_test.values,Y_test)
                 pr=rfc.predict([plist])
            elif r == "Logistic Regression":
                 lr=LogisticRegression()
                 lr.fit(X_train.values,Y_train.values)
                 score=lr.score(X_test.values,Y_test.values)
                 pr=lr.predict([plist])            
            messagebox.showinfo("Results",f"Model used: {r}\nPrediction results: {pr[0]}\nAccuracy of model is: {round(score,4)}")
        except ValueError:
            messagebox.showerror("Value Error","Please enter numeric values!!")
    pr=Button(frame,text="Predict",command=predict).grid(row=5+i,column=1,pady=10)
    c=Button(frame,text="Clear",command=clear).grid(row=5+i,column=0,pady=10)
    classifier=OptionMenu(frame,reg,*menu).grid(row=4+i,column=1,pady=10)
    mo=Label(frame,text="Select Model",font="Times 15").grid(row=4+i,column=0,pady=10)
    frame.mainloop()
def new1():
    try:
        df=pd.read_csv(data.get())
        if data.get()[:-4].lower() not in dataset:
            dataset.append(data.get()[:-4])
            show()
            messagebox.showinfo("Success","File successfully added")
            files.remove(data.get())
        else:
            messagebox.showinfo("Already exists","File Already exists!!")
    except FileNotFoundError:
        messagebox.showerror("Error",f"Please Choose a file and try again!!!")
    finally:
        op = OptionMenu(root,data,*files[1:]).grid(row=100,column=1)
        data.set(files[0])
root=Tk()
root.title("Prediction App")
a=IntVar()
i=PhotoImage(file = "predict.png")
root.iconphoto(False,i)
def show():
    i=0
    for i in range(1,len(dataset)):
        radio = Radiobutton(root,text=dataset[i].capitalize()+" Prediction App",font="Times 15",variable=a,value=i,command=m).grid(row=i-1,column=1)
    return i
i = show()
label=Label(text="Select app to open:",font="Times 15").grid(row=0,column=0,pady=10)
butt = Button(root,text = "Add Dataset",font = "Times 15", activeforeground='blue',command = new1).grid(row=100,column=2)
data = StringVar()
data.set(files[0])
l = Label(root,text="Enter name of Dataset: ",font = "Times 15").grid(row=100,column=0)
op = OptionMenu(root,data,*files[1:]).grid(row=100,column=1)
root.mainloop()
