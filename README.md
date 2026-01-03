# 🌐 Phishing URL Detector

A rule-based **Phishing URL Detection tool** built using Python.  
This tool analyzes URLs and classifies them as **SAFE**, **SUSPICIOUS**, or **PHISHING** using common cybersecurity indicators.

🔥 **HACK WITH ARIF**  
📢 Subscribe on YouTube: **Hack With Arif**  

⚠️ Educational & Defensive Security Tool Only

---

## 🚀 Features
- Detects **IP-based URLs**
- Checks for **HTTPS**
- Finds **suspicious keywords** (login, verify, free, etc.)
- Detects **fake / suspicious domain structures**
- Works on **Windows, Linux, and Termux**

---

## 🧰 Technologies Used
- Python 3
- re
- urllib
- socket  

(No external libraries required)

---

## 📂 Project Structure
```
phishing-url-detector/
│
├── detector.py
├── rules.py
├── banner.py
├── README.md
└── requirements.txt
```

---

## 📱 Installation & Usage (Termux)

### 1️⃣ Update Termux

pkg update && pkg upgrade


### 2️⃣ Install Python & Git

pkg install python git


### 3️⃣ Clone Repositor
git clone https://github.com/arifshaikh0462/Phishing-URL-Detector.git
cd phishing-url-detector


### 4️⃣ Run Tool

python detector.py




## 🐧 Installation & Usage (Linux)

### Debian / Ubuntu

sudo apt update
sudo apt install python3 git -y

### Clone & Run

git clone https://github.com/arifshaikh0462/Phishing-URL-Detector.git
cd phishing-url-detector
python3 detector.py


---

## 🪟 Installation & Usage (Windows)

### 1️⃣ Install Python
Download from https://www.python.org  
✔ Check **Add Python to PATH**

### 2️⃣ Clone or Download ZIP
git clone https://github.com/arifshaikh0462/Phishing-URL-Detector.git
cd phishing-url-detector


### 3️⃣ Run

python detector.py


## 🧪 Example Output
```
HACK WITH ARIF
Subscribe on YouTube: Hack With Arif

Enter URL to analyze: http://free-login-verify.com

Verdict : 🚨 PHISHING (High Risk)
Risk Score : 4
Reasons:
- HTTPS missing
- Suspicious keywords found
- Suspicious domain structure
```

---

## 📢 YouTube Channel
🎥 **Hack With Arif**  
Cybersecurity • Ethical Hacking • Awareness

---

## ⚠️ Disclaimer
This project is created **only for educational and awareness purposes**.  
Do NOT use this tool for illegal activities.

---

⭐ If you like this project, don’t forget to **star the repository**!
