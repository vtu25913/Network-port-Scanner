# 🔍 Network Port Scanner

> A fast, multi-threaded network port scanner with a modern GUI, built using Python. This tool allows you to scan ports, detect open services, and grab banners in real-time.

---

## ✨ Features

- ⚡ High-speed multi-threaded scanning
- 🎯 Scan custom port ranges
- 🌐 Resolve domain names to IP
- 🔎 Identify common services (HTTP, SSH, FTP, etc.)
- 🧠 Banner grabbing for service insights
- 📊 Real-time progress bar
- 🖥️ Clean dark-themed GUI
- ⏹️ Stop scans anytime
- 💾 Export results to `.txt`

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3 |
| Networking | `socket` |
| Concurrency | `threading` + `concurrent.futures` |
| GUI | `tkinter` |
| Messaging | `queue` (thread-safe) |

---

## 📁 Project Structure

```
.
├── Networkscanner.py   # Main application
└── README.md           # Project documentation
```

---

## 📦 Installation

> ✅ No external dependencies required

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/advanced-port-scanner.git
cd advanced-port-scanner
```

### 2️⃣ Run the Application

```bash
python Networkscanner.py
```

---

## 🚀 Usage

1. Enter a **target** (IP address or domain name)
2. Set **Start Port** *(default: 1)*
3. Set **End Port** *(default: 1024)*
4. Click ▶️ **Start** to begin scanning
5. View: Open ports · Services · Banners

**Optional controls:**
- ⏹️ Stop scan at any time
- 💾 Save results to file

---

## 📋 Example Output

```
Target: example.com (93.184.216.34)

[+] 80  (HTTP) ➡  Apache/2.4.41 (Ubuntu)
[+] 22  (SSH)  ➡  OpenSSH 7.6p1 Ubuntu
```

---

## ⚙️ How It Works

1. Uses **TCP `connect_ex()`** to check open ports
2. Runs scans concurrently using **`ThreadPoolExecutor`**
3. Communicates results via a **thread-safe queue**
4. Updates GUI dynamically with progress
5. Attempts **banner grabbing** from open sockets

---

## ⚠️ Disclaimer

> 🚨 **This tool is for educational and authorized use only.**
>
> ❌ Do **NOT** scan systems without explicit permission.
> Unauthorized scanning may be **illegal** in your jurisdiction.

---

## 🗺️ Roadmap / Future Improvements

- [ ] 🔒 OS fingerprinting
- [ ] 📡 UDP scanning
- [ ] 📁 Export to CSV/JSON
- [ ] 🌍 Multi-host scanning
- [ ] 🎨 UI enhancements

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source. Use responsibly.
