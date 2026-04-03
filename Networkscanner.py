import socket
import threading
import time
import queue
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from concurrent.futures import ThreadPoolExecutor, as_completed

# ---------------------------
# Common Ports
# ---------------------------
COMMON_PORTS = {
    21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
    80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS',
    3306: 'MySQL', 3389: 'RDP', 5900: 'VNC', 8080: 'HTTP-Alt'
}

# ---------------------------
# Scanner Class
# ---------------------------
class PortScanner:
    def __init__(self, target, start_port, end_port, timeout=0.5, max_workers=200):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.timeout = timeout
        self.max_workers = max_workers

        self._stop_event = threading.Event()
        self.total_ports = max(0, end_port - start_port + 1)
        self.scanned_count = 0
        self.open_ports = []
        self._lock = threading.Lock()
        self.result_queue = queue.Queue()

    def stop(self):
        self._stop_event.set()

    def resolve_target(self):
        return socket.gethostbyname(self.target)

    def grab_banner(self, sock):
        try:
            sock.settimeout(0.3)
            banner = sock.recv(1024).decode(errors="ignore").strip()
            return banner if banner else "No banner"
        except:
            return "No banner"

    def scan_port(self, port):
        if self._stop_event.is_set():
            return

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                result = s.connect_ex((self.target, port))

                if result == 0:
                    banner = self.grab_banner(s)
                    service = COMMON_PORTS.get(port, 'Unknown')

                    with self._lock:
                        self.open_ports.append((port, service, banner))

                    self.result_queue.put(('open', port, service, banner))

        except Exception as e:
            self.result_queue.put(('error', port, str(e)))

        finally:
            with self._lock:
                self.scanned_count += 1
            self.result_queue.put(('progress', self.scanned_count, self.total_ports))

    def run(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []

            for port in range(self.start_port, self.end_port + 1):
                if self._stop_event.is_set():
                    break
                futures.append(executor.submit(self.scan_port, port))

            for future in as_completed(futures):
                if self._stop_event.is_set():
                    break

        self.result_queue.put(('done', None, None))


# ---------------------------
# GUI (Modern Dark UI)
# ---------------------------
class ScannerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("⚡ Advanced Port Scanner")
        self.geometry("900x600")
        self.configure(bg="#0f172a")

        self.scanner = None
        self.scanner_thread = None

        self._style()
        self._build_ui()

    def _style(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TFrame", background="#0f172a")
        style.configure("TLabel", background="#0f172a", foreground="white", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"))

    def _build_ui(self):
        # Title
        tk.Label(self, text="🚀 Network Port Scanner",
                 font=("Segoe UI", 20, "bold"),
                 bg="#0f172a", fg="#38bdf8").pack(pady=10)

        # Inputs
        frame = ttk.Frame(self)
        frame.pack(pady=10)

        ttk.Label(frame, text="Target").grid(row=0, column=0, padx=10)
        self.target_entry = ttk.Entry(frame, width=25)
        self.target_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Start Port").grid(row=0, column=2, padx=10)
        self.start_entry = ttk.Entry(frame, width=10)
        self.start_entry.insert(0, "1")
        self.start_entry.grid(row=0, column=3)

        ttk.Label(frame, text="End Port").grid(row=0, column=4, padx=10)
        self.end_entry = ttk.Entry(frame, width=10)
        self.end_entry.insert(0, "1024")
        self.end_entry.grid(row=0, column=5)

        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(btn_frame, text="▶ Start", bg="#22c55e",
                                   command=self.start_scan)
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = tk.Button(btn_frame, text="⏹ Stop", bg="#ef4444",
                                  fg="white", state="disabled",
                                  command=self.stop_scan)
        self.stop_btn.grid(row=0, column=1, padx=10)

        tk.Button(btn_frame, text="💾 Save", bg="#3b82f6",
                  fg="white", command=self.save).grid(row=0, column=2, padx=10)

        # Status
        self.status = tk.StringVar(value="Idle")
        tk.Label(self, textvariable=self.status,
                 bg="#0f172a", fg="#facc15").pack()

        # Progress
        self.progress = ttk.Progressbar(self, length=700)
        self.progress.pack(pady=10)

        # Output
        self.text = tk.Text(self, bg="#020617", fg="#22c55e",
                            insertbackground="white",
                            font=("Consolas", 10))
        self.text.pack(fill="both", expand=True, padx=10, pady=10)

    # ---------------------------
    # Logic
    # ---------------------------
    def start_scan(self):
        target = self.target_entry.get()
        start = int(self.start_entry.get())
        end = int(self.end_entry.get())

        self.scanner = PortScanner(target, start, end)

        try:
            ip = self.scanner.resolve_target()
            self.text.insert(tk.END, f"🎯 Target: {target} ({ip})\n\n")
        except:
            messagebox.showerror("Error", "Invalid target")
            return

        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.status.set("Scanning...")

        self.scanner_thread = threading.Thread(target=self.scanner.run)
        self.scanner_thread.start()

        self.after(50, self.update_ui)

    def stop_scan(self):
        if self.scanner:
            self.scanner.stop()
            self.status.set("Stopping...")

    def update_ui(self):
        try:
            while True:
                msg = self.scanner.result_queue.get_nowait()

                if msg[0] == 'open':
                    _, port, service, banner = msg
                    self.text.insert(tk.END, f"[+] {port} ({service})\n➡ {banner}\n\n")

                elif msg[0] == 'progress':
                    _, scanned, total = msg
                    self.progress['maximum'] = total
                    self.progress['value'] = scanned
                    self.status.set(f"Scanning {scanned}/{total}")

                elif msg[0] == 'done':
                    self.status.set("✅ Completed")
                    self.start_btn.config(state="normal")
                    self.stop_btn.config(state="disabled")
                    return

        except queue.Empty:
            pass

        self.after(50, self.update_ui)

    def save(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            with open(file, "w") as f:
                f.write(self.text.get("1.0", tk.END))


# ---------------------------
# Run
# ---------------------------
if __name__ == "__main__":
    app = ScannerGUI()
    app.mainloop()
