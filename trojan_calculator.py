#!/usr/bin/env python3
"""
===============================================================================
                        EDUCATIONAL TROJAN HORSE DEMONSTRATION
                     FOR SECURITY EDUCATION PURPOSES ONLY
                     
WARNING: This is a simulated malware for educational use in controlled environments
         Never run this on production systems or without proper authorization
         
         ADAMA SCIENCE AND TECHNOLOGY UNIVERSITY 
                 COMPUTER SYSTEM SECURITY 
                      SECTION 2
===============================================================================
"""

import os
import sys
import time
import shutil
import hashlib
import json
from datetime import datetime
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
    BG_YELLOW = '\033[43m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def animate_text(text, color=Colors.CYAN, delay=0.02):
    """Animate text printing"""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    """Display animated banner"""
    banner = f"""
{Colors.RED}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║  ████████╗██████╗  ██████╗      ██╗   █████╗ ███╗   ██╗              ║
    ║  ╚══██╔══╝██╔══██╗██╔═══██╗     ██║   ██╔══██╗████╗  ██║              ║
    ║     ██║   ██████╔╝██║   ██║     ██║   ███████║██╔██╗ ██║              ║
    ║     ██║   ██╔══██╗██║   ██║██   ██║   ██╔══██║██║╚██╗██║              ║
    ║     ██║   ██║  ██║╚██████╔╝╚█████╔╝ ╚ ██   ██ ██║  ████║           ║
    ║     ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚════╝   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝              ║
    ║                                                                              ║
    ║                        HORSE ATTACK SIMULATION                               ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.END}
"""
    print(banner)
    time.sleep(1)

def warning_message():
    """Display warning message"""
    warning = f"""
{Colors.RED}{Colors.BG_YELLOW}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════════╗
║                           ⚠️  W A R N I N G  ⚠️                                  ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║  THIS IS AN EDUCATIONAL DEMONSTRATION TOOL FOR CYBERSECURITY LEARNING           ║
║                                                                                  ║
║  Purpose: Demonstrate how Trojan Horse malware works in a controlled environment ║
║                                                                                  ║
║  ⚠️  DO NOT USE THIS ON ANY PRODUCTION SYSTEM OR WITHOUT PROPER AUTHORIZATION   ║
║                                                                                  ║
║  ⚠️  FOR EDUCATIONAL USE IN CONTROLLED LAB ENVIRONMENTS ONLY                   ║
║                                                                                  ║
║  NEW FEATURE: Run 'python3 trojan_monitor.py' to see behind-the-scenes activity ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
{Colors.END}
"""
    print(warning)
    time.sleep(3)

def create_attack_log():
    """Create a log file that the monitor can read"""
    log_data = {
        "trojan_started": datetime.now().isoformat(),
        "process_id": os.getpid(),
        "username": os.getenv('USER', 'unknown'),
        "hostname": os.uname().nodename if hasattr(os, 'uname') else 'unknown'
    }
    
    log_file = "trojan_attack_log.json"
    with open(log_file, 'w') as f:
        json.dump(log_data, f, indent=2)
    
    return log_file

def stealth_operation():
    """Simulated malicious operation in background"""
    try:
        # Create attack log
        create_attack_log()
        
        # Create stolen_data directory if it doesn't exist
        if not os.path.exists("stolen_data"):
            os.makedirs("stolen_data")
        
        # Create monitoring marker
        with open("stolen_data/.monitoring_active", 'w') as f:
            f.write("Trojan activity can be monitored with trojan_monitor.py\n")
        
        # Simulate stealing files from test_files
        test_dir = "test_files"
        if os.path.exists(test_dir):
            files = os.listdir(test_dir)
            stolen_count = 0
            
            for file in files:
                src = os.path.join(test_dir, file)
                if os.path.isfile(src):
                    dst = os.path.join("stolen_data", f"stolen_{file}")
                    
                    # Copy file to stolen_data
                    shutil.copy2(src, dst)
                    stolen_count += 1
                    
                    # Create a detailed log of stolen files
                    with open("stolen_data/theft_log.txt", "a") as log:
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        file_size = os.path.getsize(src) if os.path.exists(src) else 0
                        log.write(f"[{timestamp}] STOLEN: {file} ({file_size} bytes) -> {dst}\n")
                    
                    # Create JSON log for monitor
                    json_log = {
                        "event": "file_theft",
                        "timestamp": datetime.now().isoformat(),
                        "filename": file,
                        "source": src,
                        "destination": dst,
                        "size": file_size,
                        "status": "success"
                    }
                    
                    json_log_file = f"stolen_data/theft_{file}_{datetime.now().strftime('%H%M%S')}.json"
                    with open(json_log_file, 'w') as f:
                        json.dump(json_log, f, indent=2)
            
            # Infect a specific file (simulated infection)
            target_file = "test_files/document1.txt"
            if os.path.exists(target_file):
                with open(target_file, "a") as f:
                    infection_marker = f"""
[INFECTED BY TROJAN] 
Timestamp: {datetime.now()}
Process ID: {os.getpid()}
Warning: This file has been compromised by educational trojan
This demonstrates how trojans can modify files without user knowledge
"""
                    f.write(infection_marker)
                
                # Log the infection
                with open("stolen_data/infection_log.txt", "a") as log:
                    log.write(f"[{datetime.now()}] INFECTED: {target_file}\n")
        
        return True
    except Exception as e:
        # Log the error
        with open("stolen_data/error_log.txt", "a") as log:
            log.write(f"[{datetime.now()}] ERROR: {str(e)}\n")
        return False

def calculator_interface():
    """Frontend calculator interface (Trojan's disguise)"""
    clear_screen()
    
    calc_banner = f"""
{Colors.GREEN}{Colors.BOLD}
    ╔══════════════════════════════════════════════════╗
    ║              🧮 CALCULATOR INTERFACE 🧮          ║
    ║               (Trojan Horse - Educational)       ║
    ║        ADAMA SCIENCE AND TECHNOLOGY UNIVERSITY   ║
    ║           COMPUTER SYSTEMS SECURITY(CSEg4205)    ║
    ║                  SECTION 2                       ║
    ╚══════════════════════════════════════════════════╝
{Colors.END}
"""
    print(calc_banner)
    
    # Hint about monitoring
    print(f"\n{Colors.CYAN}[Tip]{Colors.END} {Colors.YELLOW}Open another terminal and run:{Colors.END}")
    print(f"{Colors.WHITE}    python3 trojan_monitor.py{Colors.END}")
    print(f"{Colors.YELLOW}    to see what happens behind the scenes!{Colors.END}\n")
    
    while True:
        print(f"\n{Colors.CYAN}Select operation:{Colors.END}")
        print(f"{Colors.YELLOW}1. Addition{Colors.END}")
        print(f"{Colors.YELLOW}2. Subtraction{Colors.END}")
        print(f"{Colors.YELLOW}3. Multiplication{Colors.END}")
        print(f"{Colors.YELLOW}4. Division{Colors.END}")
        print(f"{Colors.RED}5. Exit Calculator{Colors.END}")
        
        choice = input(f"\n{Colors.WHITE}Enter choice (1-5): {Colors.END}")
        
        if choice == '5':
            print(f"\n{Colors.GREEN}Thank you for using the calculator!{Colors.END}")
            time.sleep(2)
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input(f"{Colors.WHITE}Enter first number: {Colors.END}"))
                num2 = float(input(f"{Colors.WHITE}Enter second number: {Colors.END}"))
                
                if choice == '1':
                    result = num1 + num2
                    operation = "➕ Addition"
                    color = Colors.GREEN
                elif choice == '2':
                    result = num1 - num2
                    operation = "➖ Subtraction"
                    color = Colors.BLUE
                elif choice == '3':
                    result = num1 * num2
                    operation = "✖️ Multiplication"
                    color = Colors.YELLOW
                elif choice == '4':
                    if num2 == 0:
                        print(f"{Colors.RED}Error: Division by zero!{Colors.END}")
                        continue
                    result = num1 / num2
                    operation = "➗ Division"
                    color = Colors.PURPLE
                
                print(f"\n{color}{Colors.BOLD}{operation} Result: {num1} and {num2} = {result}{Colors.END}")
                
                # Show "processing" animation that actually does stealth operations
                print(f"\n{Colors.YELLOW}[System]: Processing calculation...{Colors.END}", end='')
                for i in range(3):
                    print(f"{Colors.RED}.{Colors.END}", end='')
                    sys.stdout.flush()
                    
                    # Do small stealth operations during "processing"
                    if i == 1:
                        # Log this operation
                        with open("stolen_data/activity_log.txt", "a") as f:
                            f.write(f"[{datetime.now()}] Calculator operation: {operation} = {result}\n")
                    
                    time.sleep(0.5)
                print()
                
                # Occasionally show a "hint" about monitoring
                if random.random() < 0.3:  # 30% chance
                    print(f"\n{Colors.CYAN}[Did you know?]{Colors.END}")
                    print(f"{Colors.YELLOW}Trojans often hide their activities during 'normal' operations.{Colors.END}")
                    print(f"{Colors.YELLOW}Run the monitor to see what's really happening!{Colors.END}")
                
            except ValueError:
                print(f"{Colors.RED}Invalid input! Please enter numbers only.{Colors.END}")
        else:
            print(f"{Colors.RED}Invalid choice! Please select 1-5.{Colors.END}")

def main():
    """Main Trojan Horse execution"""
    clear_screen()
    
    # Animated intro sequence
    print(f"{Colors.RED}{Colors.BOLD}")
    animate_text("Initializing Trojan Horse Simulation...", Colors.RED, 0.05)
    time.sleep(1)
    
    print_banner()
    time.sleep(1)
    
    warning_message()
    time.sleep(2)
    
    # Show loading animation
    print(f"\n{Colors.YELLOW}[*] Loading malicious payload (simulated)...{Colors.END}")
    for i in range(10):
        print(f"{Colors.RED}█{Colors.END}", end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    
    print(f"{Colors.GREEN}[+] Payload loaded successfully!{Colors.END}")
    time.sleep(1)
    
    # Show monitoring hint
    print(f"\n{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}💡 MONITORING FEATURE AVAILABLE 💡{Colors.END}")
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.WHITE}To see behind-the-scenes Trojan activity:{Colors.END}")
    print(f"{Colors.YELLOW}1. Open a NEW terminal window/tab{Colors.END}")
    print(f"{Colors.YELLOW}2. Navigate to this directory: {os.getcwd()}{Colors.END}")
    print(f"{Colors.YELLOW}3. Run: {Colors.WHITE}python3 trojan_monitor.py{Colors.END}")
    print(f"{Colors.YELLOW}4. Select option 2: 'Real-time Trojan Activity Monitor'{Colors.END}")
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")
    time.sleep(3)
    
    # Execute stealth operation in background
    print(f"\n{Colors.YELLOW}[*] Starting background operations...{Colors.END}")
    if stealth_operation():
        print(f"{Colors.RED}[!] Stealth operation completed{Colors.END}")
        print(f"{Colors.RED}[!] Files have been copied to stolen_data/{Colors.END}")
        print(f"{Colors.RED}[!] Target file infected for demonstration{Colors.END}")
    else:
        print(f"{Colors.YELLOW}[*] Stealth operation failed or no files to process{Colors.END}")
    
    time.sleep(2)
    
    # Launch the calculator frontend
    calculator_interface()
    
    # Final message
    clear_screen()
    final_msg = f"""
{Colors.CYAN}{Colors.BOLD}
    ╔══════════════════════════════════════════════════╗
    ║            EDUCATIONAL DEMONSTRATION ENDED       ║
    ╠══════════════════════════════════════════════════╣
    ║                                                  ║
    ║  📊 What happened during this simulation:       ║
    ║                                                  ║
    ║  1. Calculator frontend was displayed            ║
    ║  2. Background stealth operations executed       ║
    ║  3. Files copied to stolen_data/ directory       ║
    ║  4. Target file was "infected" for demonstration ║
    ║  5. Logs created for monitoring analysis         ║
    ║                                                  ║
    ║  🔍 Check these locations:                       ║
    ║     • stolen_data/ - Contains stolen files       ║
    ║     • test_files/ - Contains infected files      ║
    ║     • Various log files created                  ║
    ║                                                  ║
    ║  📈 For detailed analysis:                       ║
    ║     Run: python3 trojan_monitor.py              ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════════╝
    
    {Colors.RED}REMEMBER: This was for educational purposes only!
    Never run unknown software on your systems!{Colors.END}
"""
    print(final_msg)
    
    # Show summary of what was created
    print(f"\n{Colors.YELLOW}📁 Generated files and directories:{Colors.END}")
    items = []
    
    if os.path.exists("stolen_data"):
        items.append("stolen_data/ - Contains exfiltrated data")
        try:
            stolen_files = os.listdir("stolen_data")
            items.append(f"  Contains {len(stolen_files)} files")
        except:
            pass
    
    if os.path.exists("trojan_attack_log.json"):
        items.append("trojan_attack_log.json - Trojan execution log")
    
    if os.path.exists("test_files/document1.txt"):
        # Check if it's infected
        with open("test_files/document1.txt", 'r') as f:
            if "INFECTED BY TROJAN" in f.read():
                items.append("test_files/document1.txt - Infected file")
    
    for item in items:
        print(f"  • {item}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Program terminated by user{Colors.END}")
        sys.exit(0)
