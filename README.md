# Network-port-Scanner
A fast, multi-threaded network port scanner with a modern GUI, built using Python. This tool allows users to scan a range of ports on a target host, detect open services, and retrieve banner information.

✨ Features
⚡ Multi-threaded scanning (fast performance)
🎯 Scan custom port ranges
🌐 Hostname → IP resolution
🔍 Detect common services (HTTP, SSH, FTP, etc.)
🧠 Banner grabbing for deeper inspection
📊 Real-time progress tracking
🖥️ Modern dark-themed GUI (Tkinter)
⏹️ Start/Stop scanning anytime
💾 Save scan results to a file
🛠️ Technologies Used
Python 3
socket (network communication)
threading & concurrent.futures (parallel scanning)
tkinter (GUI)
queue (thread-safe communication)
📦 Installation
Clone or download the project
Make sure Python 3 is installed
No external dependencies required 🎉

Run the program:

python Networkscanner.py
🧑‍💻 Usage
Enter a target (IP address or domain name)
Specify:
Start Port (default: 1)
End Port (default: 1024)
Click ▶ Start
Watch results in real-time:
Open ports
Detected service
Banner (if available)
Click ⏹ Stop to halt scanning
Click 💾 Save to export results
📊 Example Output
🎯 Target: example.com (93.184.216.34)

[+] 80 (HTTP)
➡ Apache/2.4.41 (Ubuntu)

[+] 22 (SSH)
➡ OpenSSH 7.6p1 Ubuntu
🧠 How It Works
Uses TCP connect_ex() to check if ports are open
Runs scans concurrently using a ThreadPoolExecutor
Uses a queue system to safely update the GUI
Attempts to grab banners from open ports
Tracks progress and updates UI dynamically
⚠️ Disclaimer

This tool is intended for educational and authorized testing purposes only.

Do NOT scan networks or systems without permission.

Unauthorized scanning may be illegal.

🔮 Future Improvements
🔐 OS detection (fingerprinting)
📡 UDP scanning support
📁 Export to CSV/JSON
🌍 Network-wide scanning
🎨 Enhanced UI/UX
