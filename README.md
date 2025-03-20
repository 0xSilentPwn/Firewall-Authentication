# 🔐 Internet Authentication Page  

A simple authentication page for controlling network access, built using **HTML, CSS, and JavaScript** with a **Python Flask backend**. This project is a simple sets up an authentication page for internet access within a local network. The authentication page is hosted using a Python-based web server and automatically starts on system boot 

## 🚀 Features  

✔️ User authentication page hosted on a **specific IP**.  
✔️ **Python Flask server** to handle login requests.  
✔️ **Automatically starts on system boot** via `start_auth_server.bat`.  
✔️ Securely restricts access based on network configurations.  

## 📂 Folder Structure  

```
/--- Firewall Authentication (GitHub Repository)
  |-- /static
      |-- styles.css (Styling for the authentication page)
      |-- script.js (Client-side functionality)
  |-- /templates
      |-- login.html (Authentication page)
  |-- auth_server.py (Main Python server)
  |-- start_auth_server.bat (Startup script for Windows)
  |-- README.md              (Documentation file)
```

## 🔧 Installation & Setup  

### 1️⃣ Install Dependencies  
Ensure Python is installed, then run:  
```bash
pip install flask
```

### 2️⃣ Run the Authentication Server  
```bash
python auth_server.py
```
The server will be accessible on your configured IP.

### 3️⃣ Auto-Start on Boot (Windows)  
Place `start_auth_server.bat` in `shell:startup` to launch the server at system boot. 

---

### ⚠️ Important  
Ensure that the **correct path** to `auth_server.py` is set in the `start_auth_server.bat` file. Update the `.bat` file with the absolute path to `auth_server.py`, like this:  

```bat
@echo off
cd /d "C:\Path\To\Your\Project\Folder"
python auth_server.py
```

Replace `"C:\Path\To\Your\Project\Folder"` with the actual directory where your `auth_server.py` is located.  

## 🌐 Hosting on a Specific IP  

Modify `auth_server.py` to bind the server to a particular IP:  
```python
app.run(host='192.168.1.1', port=5000)
```
Ensure the firewall allows access to the selected IP.

---

## 🔐 Authentication Details  

To log in to the authentication page, use the following credentials:  

```plaintext
Username: admin  
Password: pass123  
```

Ensure these credentials are correctly configured in your `auth_server.py` or database if modified. 

## ⚠️ Disadvantage

Currently, when the server starts using start_auth_server.bat, it prompts for admin approval (UAC prompt). This can be inconvenient as it requires manual confirmation each time the system boots.

🔧 Future Improvement: In upcoming sessions, we will work on a method to bypass the admin prompt securely while maintaining system integrity.

## Future Enhancements  

🚀 **Database Integration** – Store login credentials securely.  
🔑 **Multi-Factor Authentication (MFA)** – Enhance security.  
📊 **Admin Panel** – Monitor and manage connected users.  
🔗 **Custom Captive Portal** – Redirect unauthenticated users automatically.  
