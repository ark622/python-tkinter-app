from tkinter import *
import tkinter.ttk as ttk # tkinter Library for GUI
import os
import DataScraper
import pandas as pd # pandas Library for making DataFrames and using numpy
from pandas.io.json import json_normalize
import csv  # csv libary for reading csv file
import json # json library to parse and normalize json
import matplotlib # matplotlib Library for plotting graphs
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# Designing window for registration

class LoginForm():  # LoginForm class for handling all the login/registration related activity

    def __init__(self, dash):
        self.redLabel = None
        self.greenLabel = None
        self.callAfter = dash
    def register(self): # register screen
        self.hide(self.main_account_screen)
        self.register_screen = None
        self.register_screen = Toplevel(self.main_account_screen)
        self.register_screen.title("Register")
        self.register_screen.geometry("300x250")

        self.username_entry = None
        self.password_entry = None
        self.username = StringVar()
        self.password = StringVar()
    
        Label(self.register_screen, text="Please enter details below", bg="white").pack()
        Label(self.register_screen, text="").pack()
        username_lable = Label(self.register_screen, text="Username * ")
        username_lable.pack()
        self.username_entry = Entry(self.register_screen, textvariable=self.username)
        self.username_entry.pack()
        password_lable = Label(self.register_screen, text="Password * ")
        password_lable.pack()
        self.password_entry = Entry(self.register_screen, textvariable=self.password, show='*')
        self.password_entry.pack()
        Label(self.register_screen, text="").pack()
        Button(self.register_screen, text="Register", width=10, height=1, bg="white", command = self.register_user).pack()
        Button(self.register_screen, text="Back", width=10, height=1, command = lambda: self.show(self.main_account_screen,self.register_screen)).pack()
        self.register_screen.protocol("WM_DELETE_WINDOW", self.closeAllWindows)
    
    
    # Designing window for login 
    
    def login(self): # login screen
        self.hide(self.main_account_screen)
        self.login_screen = Toplevel()
        self.login_screen.title("Login")
        self.login_screen.geometry("300x250")
        Label(self.login_screen, text="Please enter details below to login").pack()
        Label(self.login_screen, text="").pack()
    
        self.username_verify = None
        self.password_verify = None
    
        self.username_verify = StringVar()
        self.p = StringVar()
    
        self.username_login_entry = None
        self.password_login_entry = None
    
        Label(self.login_screen, text="Username * ").pack()
        self.u = Entry(self.login_screen, textvariable=self.username_verify)
        self.u.pack()
        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Password * ").pack()
        self.password_login_entry = Entry(self.login_screen, textvariable=self.p, show= '*')
        self.password_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Button(self.login_screen, text="Login", width=10, height=1, command = self.login_verify).pack()
        Button(self.login_screen, text="Back", width=10, height=1, command = lambda: self.show(self.main_account_screen,self.login_screen)).pack()
        self.login_screen.protocol("WM_DELETE_WINDOW", self.closeAllWindows)
    
    # Implementing event on register button
    
    def register_user(self):
        if self.greenLabel and self.greenLabel.winfo_exists():
            self.greenLabel.pack_forget()
        if self.redLabel and self.redLabel.winfo_exists():
            self.redLabel.pack_forget()
        username_info = self.username.get()
        password_info = self.password.get()
        list_of_files = os.listdir()
        if username_info in list_of_files:
            self.redLabel = Label(self.register_screen, text="User already Exists", fg="red", font=("calibri", 11))
            self.redLabel.pack()
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            return
        if username_info == "" or password_info == "":
            self.redLabel = Label(self.register_screen, text="Invalid Entry", fg="red", font=("calibri", 11))
            self.redLabel.pack()
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            return
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
    
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
    
        self.greenLabel = Label(self.register_screen, text="Registration Success", fg="green", font=("calibri", 11))
        self.greenLabel.pack()
    # Implementing event on login button 
    
    def login_verify(self):
        username1 = self.username_verify.get()
        password1 = self.p.get()
        self.u.delete(0, END)
        self.password_login_entry.delete(0, END)
    
        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.closeAllWindows()
                self.callAfter() # call dashboard function on successful login
            else:
                self.password_not_recognised()
    
        else:
            self.user_not_found()
    
    # Designing popup for login invalid password
    
    def password_not_recognised(self):
        self.password_not_recog_screen = None
        self.password_not_recog_screen = Toplevel(login_screen)
        self.password_not_recog_screen.title("Invalid Password")
        self.password_not_recog_screen.geometry("150x100")
        Label(self.password_not_recog_screen, text="Invalid Password ").pack()
        Button(self.password_not_recog_screen, text="OK", command=self.delete_password_not_recognised).pack()
    
    # Designing popup for user not found
    
    def user_not_found(self):
        self.user_not_found_screen = None
        self.user_not_found_screen = Toplevel(self.login_screen)
        self.user_not_found_screen.title("User Not Found")
        self.user_not_found_screen.geometry("150x100")
        Label(self.user_not_found_screen, text="User Not Found").pack()
        Button(self.user_not_found_screen, text="OK", command=self.delete_user_not_found_screen).pack()
    
    # Deleting popups
    
    def delete_password_not_recognised(self):
        self.password_not_recog_screen.destroy()
    
    
    def delete_user_not_found_screen(self):
        self.user_not_found_screen.destroy()
    
    def start(self):
        self.main_account_screen()
    
    # Designing Main(first) window
    
    def main_account_screen(self):
        self.main_account_screen = Tk()
        self.main_account_screen.geometry("300x250")
        self.main_account_screen.title("Account Login")
        Label(text="Select Your Choice", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command = self.login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=self.register).pack()
        self.main_account_screen.mainloop()
    def hide(self,someFrame):
        someFrame.withdraw()

    def show(self,someFrame,thisFrame):
        someFrame.update()
        someFrame.deiconify()
        thisFrame.withdraw()

    def closeAllWindows(self):
        self.main_account_screen.destroy()

def flatten_json(y): # function to remove tree structure in json and convert it to flat structure
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name)
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

count = None
lab1 = None
lab2 = None

def dashboard():
    global count
    global lab1
    global lab2
    companyData = None
    compData = None
    df = None
    selectedData = []
    
    def updateTable(): # Function to update table after each link is added
        with open('output.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                companyName = row['COMPANY NAME'] if 'COMPANY NAME' in row else ""
                curPrice = row['CURRENT PRICE'] if 'CURRENT PRICE' in row else ""
                curGrowth = row['CURRENT GROWTH'] if 'CURRENT GROWTH' in row else ""
                prevClose = row['PREVIOUS CLOSE VALUE'] if 'PREVIOUS CLOSE VALUE' in row else ""
                openRate = row['OPEN'] if 'OPEN' in row else ""
                bid = row['BID'] if 'BID' in row else ""
                ask = row['ASK'] if 'ASK' in row else ""
                daysRange = row['DAYS RANGE'] if 'DAYS RANGE' in row else ""
                week52 = row['52 WEEK RANGE'] if '52 WEEK RANGE' in row else ""
                tdVol = row['TD VOL'] if 'TD VOL' in row else ""
                avgVol = row['AVG VOLUME 3 MONTHS'] if 'AVG VOLUME 3 MONTHS' in row else ""
                marketCap = row['MARKET CAP'] if 'MARKET CAP' in row else ""
                pe = row['PE RATIO'] if 'PE RATIO' in row else ""
                eps = row['EPS RATIO'] if 'EPS RATIO' in row else ""
                earnDate = row['EARNINGS DATE'] if 'EARNINGS DATE' in row else ""
                dny = row['DIVIDEND & YIELD'] if 'DIVIDEND & YIELD' in row else ""
                exdiv = row['EX DIVIDEND DATE'] if 'EX DIVIDEND DATE' in row else ""
                oyp = row['ONE YR PREDICTION'] if 'ONE YR PREDICTION' in row else ""
                tree.insert("", 0, values=(companyName, curPrice, curGrowth, prevClose, openRate, bid, ask, daysRange, week52, tdVol, avgVol ,marketCap, pe, eps, earnDate, dny, exdiv, oyp))

    def getData(dataLink): # Funcion to fetch data from the datascraper in the form of json object
        companyData = DataScraper.ScrapeData(dataLink.get())
        compData = flatten_json(companyData)
        compData = json_normalize(compData)
        ip.delete(0,END)
        df = pd.DataFrame(compData)
        df.to_csv("output.csv", mode='w')  # converting json to csv with the help of DataFrame
        print(df)
        updateTable()

    root = Tk()
    root.geometry("1000x500")
    root.title("Dashboard") # Main dashboard window
    TableMargin = Frame(root, width=700, height = 450)
    TableMargin.pack(side=LEFT)
    TableMargin.pack_propagate(False)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

    # Creating table inside the dashboard screen
    tree = ttk.Treeview(TableMargin, columns=("COMPANY NAME", "CURRENT PRICE", "CURRENT GROWTH", "PREVIOUS CLOSE VALUE", "OPEN", "BID", "ASK", "DAYS RANGE", "52 WEEK RANGE",  "TD VOL", "AVG VOLUME 3 MONTHS", "MARKET CAP", "PE RATIO", "EPS RATIO", "EARNINGS DATE", "DIVIDEND & YIELD", "EX DIVIDEND DATE", "ONE YR PREDICTION"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill = Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill = X)
    tree.heading('COMPANY NAME', text="COMPANY NAME", anchor=W)
    tree.heading('CURRENT PRICE', text="CURRENT PRICE", anchor=W)
    tree.heading('CURRENT GROWTH', text="CURRENT GROWTH", anchor=W)
    tree.heading('PREVIOUS CLOSE VALUE', text="PREVIOUS CLOSE VALUE", anchor=W)
    tree.heading('OPEN', text="OPEN", anchor=W)
    tree.heading('BID', text="BID", anchor=W)
    tree.heading('ASK', text="ASK", anchor=W)
    tree.heading('DAYS RANGE', text="DAYS RANGE", anchor=W)
    tree.heading('52 WEEK RANGE', text="52 WEEK RANGE", anchor=W)
    tree.heading('TD VOL', text="TD VOL", anchor=W)
    tree.heading('AVG VOLUME 3 MONTHS', text="AVG VOLUME 3 MONTHS", anchor=W)
    tree.heading('MARKET CAP', text="MARKET CAP", anchor=W)
    tree.heading('PE RATIO', text="PE RATIO", anchor=W)
    tree.heading('EPS RATIO', text="EPS RATIO", anchor=W)
    tree.heading('EARNINGS DATE', text="EARNINGS DATE", anchor=W)
    tree.heading('DIVIDEND & YIELD', text="DIVIDEND & YIELD", anchor=W)
    tree.heading('EX DIVIDEND DATE', text="EX DIVIDEND DATE", anchor=W)
    tree.heading('ONE YR PREDICTION', text="ONE YR PREDICTION", anchor=W)
    tree.column('#0', stretch=False, minwidth=0, width=0)
    tree.column('#1', stretch=False, minwidth=0, width=105)
    tree.column('#2', stretch=False, minwidth=0, width=95)
    tree.column('#3', stretch=False, minwidth=0, width=115)
    tree.column('#4', stretch=False, minwidth=0, width=140)
    tree.column('#5', stretch=False, minwidth=0, width=40)
    tree.column('#6', stretch=False, minwidth=0, width=70)
    tree.column('#7', stretch=False, minwidth=0, width=70)
    tree.column('#8', stretch=False, minwidth=0, width=80)
    tree.column('#9', stretch=False, minwidth=0, width=95)
    tree.column('#10', stretch=False, minwidth=0, width=50)
    tree.column('#11', stretch=False, minwidth=0, width=145)
    tree.column('#12', stretch=False, minwidth=0, width=80)
    tree.column('#13', stretch=False, minwidth=0, width=60)
    tree.column('#14', stretch=False, minwidth=0, width=65)
    tree.column('#15', stretch=False, minwidth=0, width=95)
    tree.column('#16', stretch=False, minwidth=0, width=110)
    tree.column('#17', stretch=False, minwidth=0, width=110)
    tree.column('#18', stretch=False, minwidth=0, width=120)
    tree.pack()

    count = 0
    lab1 = Label(root,text="1.____________")
    lab2 = Label(root,text="2.____________")
    def getSelection(): # Function to get the selected record from the table
        global count
        global lab1
        global lab2
        if(count>1):
            count = 0
        slcted = tree.focus()
        try: 
            selectedData[count] = tree.item(slcted)['values']
        except IndexError:
            selectedData.append(tree.item(slcted)['values'])
        if(count == 0 and selectedData[count]):
            cName1 = str(count+1)+". "+str(selectedData[count][0])
            lab1.config(text=cName1)
        if(count == 1 and selectedData[count]):
            cName2 = str(count+1)+". "+str(selectedData[count][0])
            lab2.config(text=cName2)
        count += 1
    
    def displayGraphs(): # function to display the 3 types of graphs for comparison between two companies
        graphScreen = Toplevel(root)
        graphScreen.title("Comparison Graphs")
        graphScreen.geometry("1600x800")


        # Line Plot
        x=np.array ([float(selectedData[0][3]), float(selectedData[0][1])])
        v= np.array ([1,2])
        x2 = np.array([float(selectedData[1][3]), float(selectedData[1][1])])
        fig, (ax1, ax2) = plt.subplots(2,figsize=(4,4))    
        fig.suptitle('Change in Market Value')
        ax1.plot(v, x, color="blue")
        ax1.set_title(selectedData[0][0])
        ax1.tick_params(axis='x',which='both',bottom=False,labelbottom=False)
        ax2.plot(v, x2, color="red")
        ax2.set_title(selectedData[1][0])
        ax2.tick_params(axis='x',which='both',bottom=False,labelbottom=False)

        canvas = FigureCanvasTkAgg(fig, master=graphScreen)
        canvas.get_tk_widget().pack(side=LEFT)
        canvas.draw()

        # Bar chart
        markCap1 = selectedData[0][11]
        if markCap1[-1:] == 'T':   # converting Trillion, Billion to Million for comparison
            markCap1 = float(markCap1[:-1]) * 1000000
        elif markCap1[-1:] == 'B':
            markCap1 = float(markCap1[:-1]) * 1000
        elif markCap1[-1:] == 'M':
            markCap1 = float(markCap1[:-1])
        else:
            markCap1 = float(markCap1[:-1]) / 1000000
        markCap2 = selectedData[1][11]
        if markCap2[-1:] == 'T':
            markCap2 = float(markCap2[:-1]) * 1000000
        elif markCap2[-1:] == 'B':
            markCap2 = float(markCap2[:-1]) * 1000
        elif markCap2[-1:] == 'M':
            markCap2 = float(markCap2[:-1])
        else:
            markCap2 = float(markCap2[:-1]) / 1000000
        
        f = Figure(figsize=(8,4))
        ax = f.add_subplot(111)
        ax.set_title("Market Capitalisation")
        ax.set_ylabel("Million USD")
        data = (markCap1,markCap2)
        labels = [selectedData[0][0], selectedData[1][0]]
        ind = np.arange(2)  # the x locations for the groups
        width = .5
        ax.set_xticks(ind)
        ax.set_xticklabels(labels)
        rects1 = ax.bar(ind, data, width, color=("blue","green"))

        canvas2 = FigureCanvasTkAgg(f, master=graphScreen)
        canvas2.get_tk_widget().pack(side=LEFT)
        canvas2.draw()


        # Scatter plot
        N = 60
        dif1 = float(selectedData[0][1]) - float(selectedData[0][3])
        dif2 = float(selectedData[1][1]) - float(selectedData[1][3])
        g1 = ( (float(selectedData[0][1]) - dif1) + (float(selectedData[0][1]) + dif1) * np.random.rand(N), np.random.rand(N))
        g2 = ( (float(selectedData[1][1]) - dif2) + (float(selectedData[1][1]) + dif2) * np.random.rand(N), np.random.rand(N))
        data2 = (g1,g2)
        colors = ("green", "blue")
        groups = (selectedData[0][0], selectedData[1][0])
        fig3 = plt.figure(figsize=(4,4))
        ax4 = fig3.add_subplot(1,1,1)
        for data2, color, group in zip(data2, colors, groups):
            x, y = data2
            ax4.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
        ax4.legend()
        ax4.set_title("Variation in Price")
        ax4.set_xlabel("Price")

        canvas3 = FigureCanvasTkAgg(fig3, master=graphScreen)
        canvas3.get_tk_widget().pack(side=LEFT)
        canvas3.draw()

        def cleanup():
            plt.close('all') # remove graphs from memory after the window is closed
            graphScreen.destroy()
        
        graphScreen.protocol("WM_DELETE_WINDOW", cleanup)

    #rest of labels and buttons on dashboard
    dataLink = StringVar()
    Label(root, text="").pack()
    Label(root, text="Commodity Link").pack()
    ip = Entry(root, textvariable = dataLink, width = "40")
    ip.pack()
    Label(root, text="").pack()
    Button(text="Add Data", height="2", width="30", command = lambda: getData(dataLink)).pack()
    Label(root, text="").pack()
    Label(root,text="Select a company from table and press this button").pack()
    Label(root,text="").pack()
    Button(text="Add Company for comparison", height="2", width="30", command = lambda: getSelection()).pack()
    Label(root,text="").pack()
    Label(root, text="Selected Options:").pack()
    lab1.pack()
    lab2.pack()
    Label(root, text="").pack()
    Button(text="Draw Graphs", height="2", width="30", command = displayGraphs).pack()
    



    root.mainloop()

    


newLogin = LoginForm(dashboard)
newLogin.start()
