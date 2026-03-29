# 🔍 Mini Recon & OSINT Toolkit

A Python-based reconnaissance tool that performs:

- 🌐 Website data extraction using requests
- 🧠 Email, link, and phone extraction using regex
- 🛰 Port scanning using Nmap
- 📡 Traffic analysis using Wireshark
- 🧪 Request interception using Burp Suite

## 🚀 Features

- Extract emails, links, and phone numbers
- Identify open ports and running services
- Generate structured recon report
- Works with local vulnerable apps like OWASP Juice Shop

## 🛠 Tech Stack

- Python
- Requests
- Regex
- Nmap
- Wireshark
- Burp Suite
- 
## ▶️ How to Run
```bash
git clone <your-repo-link>
cd mini_recon_tool

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python3 main.py
