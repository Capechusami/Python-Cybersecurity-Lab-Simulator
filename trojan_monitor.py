#!/usr/bin/env python3
"""
===============================================================================
                TROJAN HORSE MONITORING INTERFACE
            REAL-TIME ATTACK VISUALIZATION DASHBOARD
            
Purpose: Display what happens behind the scenes when Trojan runs
         Visualize stolen data, infected files, and system impact
===============================================================================
"""

import os
import sys
import time
import json
from datetime import datetime
import threading
import queue
import random

# ==================== COLORS AND STYLING ====================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_BLUE = '\033[44m'
    BG_PURPLE = '\033[45m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def animate_text(text, color=Colors.CYAN, delay=0.03):
    """Animate text printing"""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_monitor_header():
    """Display monitoring dashboard header"""
    header = f"""
{Colors.RED}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║  ████████╗██████╗  ██████╗      ██╗ █████╗ ███╗   ██╗                       ║
    ║  ╚══██╔══╝██╔══██╗██╔═══██╗     ██║██╔══██╗████╗  ██║                       ║
    ║     ██║   ██████╔╝██║   ██║     ██║███████║██╔██╗ ██║                       ║
    ║     ██║   ██╔══██╗██║   ██║██   ██║██╔══██║██║╚██╗██║                       ║
    ║     ██║   ██║  ██║╚██████╔╝╚█████╔╝██║  ██║██║ ╚████║                       ║
    ║     ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝                       ║
    ║                                                                              ║
    ║                 MONITORING DASHBOARD - BEHIND THE SCENES                     ║
    ║                 REAL-TIME ATTACK VISUALIZATION                              ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.END}
"""
    print(header)

class TrojanMonitor:
    def __init__(self):
        self.stolen_files = []
        self.infected_files = []
        self.system_changes = []
        self.attack_log = []
        self.event_queue = queue.Queue()
        self.monitoring_active = False
        
    def log_event(self, event_type, description, severity="INFO"):
        """Log an event with timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        event = {
            'time': timestamp,
            'type': event_type,
            'description': description,
            'severity': severity
        }
        self.attack_log.append(event)
        self.event_queue.put(event)
        return event
    
    def simulate_file_theft(self, filename, source_path):
        """Simulate file theft animation"""
        self.log_event("FILE_THEFT", f"Stealing: {filename}", "HIGH")
        self.stolen_files.append({
            'filename': filename,
            'source': source_path,
            'destination': f"stolen_data/{filename}",
            'timestamp': datetime.now().isoformat(),
            'size': random.randint(1024, 1048576)  # Random size between 1KB-1MB
        })
    
    def simulate_file_infection(self, filename):
        """Simulate file infection"""
        self.log_event("FILE_INFECTION", f"Infecting: {filename}", "CRITICAL")
        self.infected_files.append({
            'filename': filename,
            'infection_type': 'Trojan Marker',
            'timestamp': datetime.now().isoformat(),
            'status': 'COMPROMISED'
        })
    
    def simulate_system_change(self, change_type, details):
        """Simulate system changes"""
        self.log_event("SYSTEM_CHANGE", details, "MEDIUM")
        self.system_changes.append({
            'type': change_type,
            'details': details,
            'timestamp': datetime.now().isoformat()
        })
    
    def display_dashboard(self):
        """Display real-time monitoring dashboard"""
        clear_screen()
        print_monitor_header()
        
        # Dashboard layout
        dashboard = f"""
{Colors.CYAN}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════════════════╗
    ║                    REAL-TIME MONITORING DASHBOARD                ║
    ╠══════════════════════════════════════════════════════════════════╣
    ║                                                                  ║
    ║  📊 ATTACK STATISTICS:                                           ║
    ║     • Files Stolen:      {len(self.stolen_files):3d}                    ║
    ║     • Files Infected:    {len(self.infected_files):3d}                    ║
    ║     • System Changes:    {len(self.system_changes):3d}                    ║
    ║     • Total Events:      {len(self.attack_log):3d}                    ║
    ║                                                                  ║
    ╠══════════════════════════════════════════════════════════════════╣
    ║                                                                  ║
    ║  🔥 LIVE ATTACK ACTIVITY:                                        ║
    ║                                                                  ║
"""
        print(dashboard)
        
        # Show last 5 events
        recent_events = self.attack_log[-5:] if len(self.attack_log) >= 5 else self.attack_log
        for event in recent_events:
            color = Colors.GREEN if event['severity'] == 'INFO' else \
                   Colors.YELLOW if event['severity'] == 'MEDIUM' else \
                   Colors.RED if event['severity'] == 'HIGH' else Colors.PURPLE
            
            print(f"    {color}[{event['time']}] {event['description']}{Colors.END}")
        
        # Show stolen files
        if self.stolen_files:
            print(f"\n    {Colors.RED}📁 STOLEN FILES:{Colors.END}")
            for i, file in enumerate(self.stolen_files[-3:]):  # Show last 3
                print(f"      • {file['filename']} ({file['size']:,} bytes)")
        
        # Show infected files
        if self.infected_files:
            print(f"\n    {Colors.PURPLE}⚠️  INFECTED FILES:{Colors.END}")
            for i, file in enumerate(self.infected_files[-3:]):
                print(f"      • {file['filename']} - {file['status']}")
        
        print(f"\n{Colors.CYAN}    ╚══════════════════════════════════════════════════════════════════╝{Colors.END}")
    
    def run_demo_attack(self):
        """Run a simulated attack demo"""
        self.monitoring_active = True
        
        # Phase 1: Reconnaissance
        self.log_event("RECON", "Scanning for target files...", "INFO")
        time.sleep(1)
        
        # Phase 2: Data Exfiltration
        demo_files = ["document1.txt", "document2.txt", "config.cfg", "financial.xlsx", "passwords.db"]
        for file in demo_files:
            self.simulate_file_theft(file, f"test_files/{file}")
            time.sleep(0.5)
            self.display_dashboard()
            time.sleep(0.3)
        
        # Phase 3: File Infection
        self.log_event("INFECTION", "Injecting malicious payload...", "HIGH")
        time.sleep(1)
        
        target_files = ["system32.dll", "boot.ini", "document1.txt"]
        for file in target_files:
            self.simulate_file_infection(file)
            time.sleep(0.7)
            self.display_dashboard()
            time.sleep(0.3)
        
        # Phase 4: System Modification
        self.simulate_system_change("REGISTRY", "Adding persistence key: HKLM\\Software\\Trojan")
        time.sleep(0.5)
        self.simulate_system_change("SCHEDULED_TASK", "Creating scheduled task: DailyBackup")
        time.sleep(0.5)
        self.simulate_system_change("NETWORK", "Opening backdoor on port 4444")
        
        # Final display
        self.display_dashboard()
        
        return True
    
    def show_attack_summary(self):
        """Display comprehensive attack summary"""
        clear_screen()
        
        summary = f"""
{Colors.RED}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════════════════╗
    ║                   ATTACK SUMMARY REPORT                          ║
    ╠══════════════════════════════════════════════════════════════════╣
    ║                                                                  ║
    ║  📈 ATTACK TIMELINE                                              ║
    ║                                                                  ║
"""
        print(summary)
        
        # Show timeline
        for event in self.attack_log:
            icon = "🔍" if "RECON" in event['type'] else \
                  "📁" if "FILE" in event['type'] else \
                  "⚠️" if "INFECTION" in event['type'] else \
                  "⚙️" if "SYSTEM" in event['type'] else "📝"
            
            color = Colors.GREEN if event['severity'] == 'INFO' else \
                   Colors.YELLOW if event['severity'] == 'MEDIUM' else \
                   Colors.RED if event['severity'] == 'HIGH' else Colors.PURPLE
            
            print(f"    {icon} {color}[{event['time']}] {event['description']}{Colors.END}")
        
        # Detailed statistics
        stats = f"""
    ║                                                                  ║
    ╠══════════════════════════════════════════════════════════════════╣
    ║                                                                  ║
    ║  📊 DETAILED STATISTICS                                          ║
    ║                                                                  ║
    ║  {Colors.CYAN}Stolen Files:{Colors.END}                                        ║
"""
        print(stats)
        
        total_stolen_size = sum(f['size'] for f in self.stolen_files)
        for file in self.stolen_files:
            print(f"    • {file['filename']:20} {file['size']:10,} bytes")
        
        print(f"""
    ║     {Colors.YELLOW}Total: {len(self.stolen_files)} files, {total_stolen_size:,} bytes{Colors.END}             ║
    ║                                                                  ║
    ║  {Colors.PURPLE}Infected Files:{Colors.END}                                     ║
""")
        
        for file in self.infected_files:
            status_color = Colors.RED if file['status'] == 'COMPROMISED' else Colors.YELLOW
            print(f"    • {file['filename']:20} {status_color}{file['status']}{Colors.END}")
        
        # Impact assessment
        impact = f"""
    ║                                                                  ║
    ╠══════════════════════════════════════════════════════════════════╣
    ║                                                                  ║
    ║  ⚠️  IMPACT ASSESSMENT                                           ║
    ║                                                                  ║
    ║  Security Level:   {Colors.RED}CRITICALLY COMPROMISED{Colors.END}               ║
    ║  Data Exposure:    {Colors.RED}HIGH{Colors.END} (Sensitive files stolen)        ║
    ║  System Integrity: {Colors.RED}LOW{Colors.END} (Multiple infections)           ║
    ║  Detection Risk:   {Colors.YELLOW}MEDIUM{Colors.END} (Stealth techniques used)  ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
"""
        print(impact)

def show_animated_attack():
    """Show animated attack visualization"""
    monitor = TrojanMonitor()
    
    # Initial animation
    clear_screen()
    print(f"{Colors.RED}{Colors.BOLD}")
    animate_text("🚀 INITIATING TROJAN ATTACK VISUALIZATION...", Colors.RED, 0.05)
    time.sleep(1)
    
    print(f"\n{Colors.YELLOW}[*] Loading attack simulation modules...{Colors.END}")
    for i in range(20):
        print(f"{Colors.RED}▉{Colors.END}" if i % 2 == 0 else f"{Colors.YELLOW}▉{Colors.END}", end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    
    # Run the demo attack
    print(f"\n{Colors.GREEN}[+] Attack simulation ready!{Colors.END}")
    time.sleep(1)
    
    monitor.run_demo_attack()
    
    # Show summary
    input(f"\n{Colors.YELLOW}Press Enter to view detailed attack summary...{Colors.END}")
    monitor.show_attack_summary()
    
    # Educational insights
    input(f"\n{Colors.YELLOW}Press Enter for educational insights...{Colors.END}")
    show_educational_insights()

def show_educational_insights():
    """Show what we learned from the attack"""
    clear_screen()
    
    insights = f"""
{Colors.CYAN}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════════════════╗
    ║                   EDUCATIONAL INSIGHTS                           ║
    ╠══════════════════════════════════════════════════════════════════╣
    ║                                                                  ║
    ║  🔍 WHAT WE OBSERVED IN THIS SIMULATION:                        ║
    ║                                                                  ║
    ║  1. {Colors.GREEN}Stealth Operation:{Colors.END}                                      ║
    ║     • Trojan appears as legitimate software                     ║
    ║     • Malicious activities run silently in background           ║
    ║     • User sees normal calculator interface                     ║
    ║                                                                  ║
    ║  2. {Colors.YELLOW}Data Exfiltration:{Colors.END}                                     ║
    ║     • Files copied without user knowledge                       ║
    ║     • Sensitive data collected to external location             ║
    ║     • Logs created to track stolen items                        ║
    ║                                                                  ║
    ║  3. {Colors.RED}System Compromise:{Colors.END}                                       ║
    ║     • Files modified/infected with malicious markers            ║
    ║     • System settings potentially altered                       ║
    ║     • Persistence mechanisms established                        ║
    ║                                                                  ║
    ║  4. {Colors.PURPLE}Detection Evasion:{Colors.END}                                     ║
    ║     • Operations timed to avoid suspicion                       ║
    ║     • Legitimate-looking processes used as cover                ║
    ║     • Minimal resource usage to avoid detection                 ║
    ║                                                                  ║
    ╠══════════════════════════════════════════════════════════════════╣
    ║                                                                  ║
    ║  🛡️  HOW TO PROTECT AGAINST SUCH ATTACKS:                       ║
    ║                                                                  ║
    ║  • {Colors.GREEN}Use reputable antivirus software{Colors.END}                           ║
    ║  • {Colors.GREEN}Download software only from official sources{Colors.END}               ║
    ║  • {Colors.GREEN}Regularly monitor system for unusual activity{Colors.END}              ║
    ║  • {Colors.GREEN}Keep systems and software updated{Colors.END}                          ║
    ║  • {Colors.GREEN}Use firewalls and network monitoring{Colors.END}                       ║
    ║  • {Colors.GREEN}Educate users about social engineering{Colors.END}                     ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
{Colors.END}
"""
    print(insights)

def real_time_monitor():
    """Monitor actual Trojan execution in real-time"""
    clear_screen()
    
    print(f"{Colors.BLUE}{Colors.BOLD}")
    animate_text("🔄 STARTING REAL-TIME TROJAN MONITOR...", Colors.BLUE, 0.04)
    print(f"{Colors.END}")
    
    monitor = TrojanMonitor()
    
    # Monitor stolen_data directory
    stolen_dir = "stolen_data"
    test_dir = "test_files"
    
    print(f"\n{Colors.YELLOW}[*] Monitoring directories:{Colors.END}")
    print(f"    • {test_dir}/")
    print(f"    • {stolen_dir}/")
    print(f"    • Current directory")
    
    print(f"\n{Colors.GREEN}[+] Monitoring active. Watching for Trojan activity...{Colors.END}")
    print(f"{Colors.YELLOW}[*] Start the Trojan calculator in another terminal to see real-time effects{Colors.END}")
    
    try:
        # Initial state
        initial_files = set()
        if os.path.exists(test_dir):
            initial_files = set(os.listdir(test_dir))
        
        print(f"\n{Colors.CYAN}Initial state captured. Waiting for activity...{Colors.END}")
        print(f"{Colors.YELLOW}Press Ctrl+C to stop monitoring{Colors.END}")
        
        last_stolen_count = 0
        last_display = time.time()
        
        while True:
            # Check for new stolen files
            if os.path.exists(stolen_dir):
                stolen_files = os.listdir(stolen_dir)
                new_files = [f for f in stolen_files if f not in monitor.stolen_files]
                
                for file in new_files:
                    monitor.simulate_file_theft(file.replace("stolen_", ""), f"{test_dir}/{file.replace('stolen_', '')}")
            
            # Check for infected files in test_files
            if os.path.exists(test_dir):
                for file in os.listdir(test_dir):
                    filepath = os.path.join(test_dir, file)
                    if os.path.isfile(filepath):
                        try:
                            with open(filepath, 'r', errors='ignore') as f:
                                content = f.read()
                                if "INFECTED BY TROJAN" in content:
                                    if file not in [f['filename'] for f in monitor.infected_files]:
                                        monitor.simulate_file_infection(file)
                        except:
                            pass
            
            # Update display every 2 seconds
            current_time = time.time()
            if current_time - last_display >= 2:
                monitor.display_dashboard()
                last_display = current_time
            
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}[*] Monitoring stopped by user{Colors.END}")
        
        if monitor.attack_log:
            action = input(f"\n{Colors.CYAN}View attack summary? (y/n): {Colors.END}")
            if action.lower() == 'y':
                monitor.show_attack_summary()
        
        return monitor

def main_menu():
    """Main menu for the monitoring interface"""
    while True:
        clear_screen()
        
        menu = f"""
{Colors.CYAN}{Colors.BOLD}
    ╔══════════════════════════════════════════════════╗
    ║        TROJAN ATTACK MONITORING SYSTEM           ║
    ╠══════════════════════════════════════════════════╣
    ║                                                  ║
    ║  1. 🎬 View Attack Simulation Demo               ║
    ║  2. 🔍 Real-time Trojan Activity Monitor         ║
    ║  3. 📊 View Previous Attack Logs                 ║
    ║  4. 📚 Educational Insights                      ║
    ║  5. ⏹️  Exit Monitoring System                  ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
{Colors.END}
"""
        print(menu)
        
        choice = input(f"\n{Colors.WHITE}Enter choice (1-5): {Colors.END}")
        
        if choice == '1':
            show_animated_attack()
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            
        elif choice == '2':
            monitor = real_time_monitor()
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            
        elif choice == '3':
            clear_screen()
            print(f"\n{Colors.CYAN}{Colors.BOLD}📁 ATTACK LOGS:{Colors.END}")
            
            # Check for existing logs
            if os.path.exists("stolen_data/theft_log.txt"):
                print(f"\n{Colors.YELLOW}Recent theft activity:{Colors.END}")
                with open("stolen_data/theft_log.txt", 'r') as f:
                    lines = f.readlines()[-10:]  # Last 10 lines
                    for line in lines:
                        print(f"  {line.strip()}")
            else:
                print(f"{Colors.YELLOW}No theft logs found.{Colors.END}")
            
            # Check for infected files
            infected_files = []
            if os.path.exists("test_files"):
                for file in os.listdir("test_files"):
                    filepath = os.path.join("test_files", file)
                    if os.path.isfile(filepath):
                        try:
                            with open(filepath, 'r', errors='ignore') as f:
                                if "INFECTED BY TROJAN" in f.read():
                                    infected_files.append(file)
                        except:
                            continue
            
            if infected_files:
                print(f"\n{Colors.RED}Infected files detected:{Colors.END}")
                for file in infected_files:
                    print(f"  • {file}")
            else:
                print(f"\n{Colors.GREEN}No infected files detected.{Colors.END}")
            
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            
        elif choice == '4':
            show_educational_insights()
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            
        elif choice == '5':
            print(f"\n{Colors.GREEN}Exiting Trojan Monitoring System...{Colors.END}")
            print(f"{Colors.GREEN}Remember: This was for educational purposes only!{Colors.END}")
            time.sleep(2)
            break
            
        else:
            print(f"\n{Colors.RED}Invalid choice! Please enter 1-5.{Colors.END}")
            time.sleep(1)

def main():
    """Main function"""
    try:
        clear_screen()
        print_monitor_header()
        time.sleep(2)
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Monitoring system terminated by user{Colors.END}")
        sys.exit(0)

if __name__ == "__main__":
    main()
