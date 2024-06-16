import socket
from threading import Thread
from tkinter import *

# nickname = input('Enter your name:')

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port =8000
client.connect((ip_address,port))
print('Client connected.')

class GUI:
    def __init__(self):
        self.window=Tk()
        self.window.withdraw()

        self.login=Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False,height=False)
        self.login.configure(width=775,height=550,bg='#36393F')

        self.pls = Label(self.login,text = "Please login to continue",justify = CENTER,font = "Helvetica 14 bold")
        self.pls.place(relHeight=0.15,relx=0.2,rely=0.07)

        self.labelName=Label(self.login,text="Name:",font="Helvetica 12")
        self.labelName.place(relHeight=0.2,relx=0.1,rely=0.2)

        self.entryName=Entry(self.login,font="Helvetica 12")
        self.entryName.place(relwidth=0.4,relHeight=0.12,relx=0.35,rely=0.2)

        self.loginBtn = Button(self.login,text="Login",font='Helvetica 14 bold',bg='#5865F2',fg='#FFF',justify=CENTER,width=24,bd=0,command=lambda: self.goAhead(self.entryName.get()))
        self.loginBtn.place(anchor=CENTER,relx=0.53,rely=0.6)
        self.window.mainloop()

    def goAhead(self,name):
        self.login.destroy()
        self.name=name
        rcv=Thread(target=self.recieve)
        rcv.start()


def recieve():
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            if msg == 'NICKNAME':
                client.send(self.name.encode('utf-8'))
            else:
                print(msg)
        except:
            print('Connection error.')
            client.close()
            break
g1 = GUI()