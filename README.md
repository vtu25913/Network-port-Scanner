# Network-port-Scanner

A fast, multi-threaded network port scanner with a modern GUI, built using Python. This tool allows you to scan ports, detect open services, and grab banners in real-time.

✨ Features
⚡ High-speed multi-threaded scanning
🎯 Scan custom port ranges
🌐 Resolve domain names to IP
🔍 Identify common services (HTTP, SSH, FTP, etc.)
🧠 Banner grabbing for service insights
📊 Real-time progress bar
🖥️ Clean dark-themed GUI
⏹️ Stop scans anytime
💾 Export results to .txt
🛠️ Tech Stack
Python 3
socket – network communication
threading + concurrent.futures – parallel execution
tkinter – GUI
queue – thread-safe messaging
📂 Project Structure
.
├── Networkscanner.py   # Main application
└── README.md           # Project documentation
📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/advanced-port-scanner.git
cd advanced-port-scanner
2️⃣ Run the Application
python Networkscanner.py

✅ No external dependencies required

🧑‍💻 Usage
Enter a target (IP or domain)
Set:
Start Port (default: 1)
End Port (default: 1024)
Click ▶ Start
View:
Open ports
Services
Banners
Optional:
⏹ Stop scan
💾 Save results
📊 Example Output
🎯 Target: example.com (93.184.216.34)

[+] 80 (HTTP)
➡ Apache/2.4.41 (Ubuntu)

[+] 22 (SSH)
➡ OpenSSH 7.6p1 Ubuntu
🧠 How It Works
Uses TCP connect_ex() to check open ports
Runs scans concurrently using ThreadPoolExecutor
Communicates results via a thread-safe queue
Updates GUI dynamically with progress
Attempts banner grabbing from open sockets
⚠️ Disclaimer

🚨 This tool is for educational and authorized use only

Do NOT scan systems without permission
Unauthorized scanning may be illegal
🔮 Roadmap / Future Improvements
🔐 OS fingerprinting
📡 UDP scanning
📁 Export to CSV/JSON
🌍 Multi-host scanning
🎨 UI enhancements
🤝 Contributing

Contributions are welcome!

Fork the repo
Create a new branch
Commit your changes
Open a Pull Request
