from flask import Flask, render_template, request, redirect
import os
import ctypes
import threading
import time

app = Flask(__name__)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def block_internet():
    os.system("netsh advfirewall set allprofiles state on")
    os.system("netsh advfirewall firewall add rule name=BlockInternet dir=out action=block protocol=any profile=any")

def unblock_internet():
    os.system("netsh advfirewall firewall delete rule name=BlockInternet")
 
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == "admin" and password == "pass123":
            unblock_internet()
            threading.Thread(target=shutdown_server, daemon=True).start()
            return redirect("https://www.google.com")
        else:
            return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html', error=None)

# Function to stop the Flask server
def shutdown_server():
    time.sleep(2)  # Optional: Small delay before shutdown
    os._exit(0)  # Immediately exit the script

if __name__ == "__main__":
    if not is_admin():
        print("This script must be run as administrator!")
    else:
        print("Blocking internet access...")
        block_internet()
        app.run(host='0.0.0.0', port=5000, debug=True)