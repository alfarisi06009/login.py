#python
#login Script

from os import access, name
from typing import Optional


def login(name,password):
    sukses = False
    file = open("login.txt", "r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==name and b==password):
            sukses = True
            break
    file.close()
    if(sukses):
        print("******************************")
        print("login berhasil, silahkan masuk")
        print("******************************")
    else:
        print("***************************************")
        print("anda belum terdaftar, silahkan register")
        print("***************************************")

def register(name,password):
    file = open("login.txt", "a")
    file.write("\n"+name+","+password)

def access(option):
    global name
    if(option == "login"):
        name = input("masukan ID : ")
        Password = input("masukan password : ")
        login(name,Password)
    else:
        print("Masukan ID dan password anda yang baru")
        name = input("masukan ID : ")
        Password = input("masukan password : ")
        register(name,Password)
        print("register anda berhasil, silahkan masuk")

def begin():
    global option
    print("Selamat datang di Safari Creative")
    print("Gratis tanpa bayaran kok")
    print("========================================")
    print("ketik 'login' jika anda sudah punya akun")
    print("ketik 'reg' jika anda belum punya akun")
    print("========================================")
    option = input("silahkan masukan (login/reg) : ")
    if(option!="login" and option!="reg"):
        begin()

begin()
access(option)