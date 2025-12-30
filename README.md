# Python-Cybersecurity-Lab-Simulator

## 📌 Overview
Interactive, console-driven lab that demonstrates a Trojan horse attack and the matching defense workflow. Run the simulated malware, watch it in real time, then neutralize it with the antivirus. **Educational use only in an isolated lab. Do not run on production machines.**

⚠️ This simulation copies/modifies files only inside the repo folder (stolen_data/, test_files/). It does not self-spread, but treat it as malware and keep it in a sandbox or throwaway VM.

---

## 🧪 Project Structure
```
Python-Cybersecurity-Lab-Simulator/
├── trojan_calculator.py     # Trojan payload disguised as a calculator (steals sample files)
├── trojan_monitor.py        # Real-time attack visualization dashboard
├── trojan_antivirus.py      # Detection + quarantine + report generator
├── demo_lab.sh              # Guided demo for Linux/Kali
├── stolen_data/             # Holds exfiltrated files and logs (created during runs)
├── test_files/              # Sample files targeted by the Trojan
└── README.md
```

---

## 🦠 Trojan Simulator (trojan_calculator.py)
### ✔️ What it does
- Presents a calculator UI while silently copying files from test_files/ into stolen_data/.
- Appends an "infected" marker to test_files/document1.txt for demonstration.
- Writes theft and activity logs inside stolen_data/.
- Does not self-spread; stays inside this lab folder.

---

## 🧭 Attack Monitor (trojan_monitor.py)
### ✔️ What it does
- Live dashboard: shows stolen files, infected files, and system-change events.
- Option 2 starts real-time monitoring; also provides an attack summary view.

---

## 🛡️ Antivirus (trojan_antivirus.py)
### ✔️ What it does
- Detects the educational Trojan signatures and stolen_data/ artifacts.
- Quarantines detected items into quarantine/ and writes JSON scan reports to scan_reports/.
- Menu option 2 runs full scan + quarantine; option 1 runs quick scan.

---

## 🚀 How to Run (Windows or Linux)
1️⃣ Open two terminals in the repo folder.
- Terminal A: Monitor the attack.
- Terminal B: Run the Trojan, then the antivirus.

2️⃣ Terminal A — start monitor:
```bash
python3 trojan_monitor.py
# choose option 2: Real-time Trojan Activity Monitor
```

3️⃣ Terminal B — run Trojan simulator:
```bash
python3 trojan_calculator.py
```
- Use the calculator UI to trigger background theft/infection activity.

4️⃣ Terminal B — scan and clean:
```bash
python3 trojan_antivirus.py
# choose option 2 for full scan + quarantine
```

---

## 👀 What to Inspect
- Stolen artifacts: [stolen_data/](stolen_data/) (copied files, theft logs, infection logs).
- Infected sample files: [test_files/](test_files/) (document1.txt gets a Trojan marker appended).
- Scan outputs: [scan_reports/](scan_reports/) JSON reports from the antivirus.
- Quarantine results: [quarantine/](quarantine/) holds moved/deactivated artifacts.

---

## 🎛 Guided Demo (Linux/Kali)
Prefer a scripted flow? Run:
```bash
bash demo_lab.sh
```
Follow the prompts; it walks through Trojan -> Monitor -> Antivirus in order.

---

## 📘 Educational Use Only
- Purpose: practice malware concepts, signatures, detection logic, and defensive cleanup.
- Keep runs inside an isolated lab or throwaway VM. Do not point it at real data.

---

## Repo Status
- Current branch: main
- Remotes: origin -> https://github.com/Capechusami/Python-Cybersecurity-Lab-Simulator.git