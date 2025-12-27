#!/usr/bin/env python3
"""
===============================================================================
                    EDUCATIONAL ANTIVIRUS SYSTEM
              TROJAN HORSE DETECTION AND REMOVAL TOOL
              
Purpose: Detect and quarantine the educational trojan horse
         Demonstrate antivirus principles in cybersecurity
===============================================================================
"""

import os
import sys
import time
import hashlib
import shutil
import json
from datetime import datetime

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

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def animate_text(text, color=Colors.CYAN, delay=0.02):
    """Animate text printing"""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_antivirus_intro():
    """Display antivirus introduction animation"""
    clear_screen()
    
    # Animated banner
    banner = f"""
{Colors.BLUE}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║   █████╗ ███╗   ██╗████████╗██╗██╗   ██╗██╗   ██╗██╗███████╗██╗   ██╗       ║
    ║  ██╔══██╗████╗  ██║╚══██╔══╝██║██║   ██║██║   ██║██║██╔════╝██║   ██║       ║
    ║  ███████║██╔██╗ ██║   ██║   ██║██║   ██║██║   ██║██║███████╗██║   ██║       ║
    ║  ██╔══██║██║╚██╗██║   ██║   ██║██║   ██║╚██╗ ██╔╝██║╚════██║██║   ██║       ║
    ║  ██║  ██║██║ ╚████║   ██║   ██║╚██████╔╝ ╚████╔╝ ██║███████║╚██████╔╝       ║
    ║  ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚══════╝ ╚═════╝        ║
    ║                                                                              ║
    ║                     EDUCATIONAL DEFENSE SYSTEM                               ║
    ║                     TROJAN HORSE DETECTOR                                    ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.END}
"""
    print(banner)
    time.sleep(1)
    
    # Security scan animation
    print(f"\n{Colors.GREEN}[*] Initializing security protocols...{Colors.END}")
    for i in range(5):
        print(f"{Colors.BLUE}🔒{Colors.END}", end='')
        sys.stdout.flush()
        time.sleep(0.3)
    print()
    
    print(f"{Colors.GREEN}[+] Security systems: ONLINE{Colors.END}")
    time.sleep(1)

def calculate_file_hash(filepath):
    """Calculate MD5 hash of a file"""
    try:
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except:
        return None

def detect_trojan():
    """Detect the educational trojan horse"""
    print(f"\n{Colors.YELLOW}{'='*60}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}🔍 SCANNING FOR TROJAN HORSE MALWARE 🔍{Colors.END}")
    print(f"{Colors.YELLOW}{'='*60}{Colors.END}")
    
    detected_files = []
    signatures = []
    
    # Known signatures of our educational trojan
    trojan_signatures = [
        "EDUCATIONAL TROJAN HORSE DEMONSTRATION",
        "stealth_operation",
        "stolen_data",
        "Background stealth operations"
    ]
    
    # Check for trojan_calculator.py
    if os.path.exists("trojan_calculator.py"):
        print(f"\n{Colors.YELLOW}[*] Analyzing: trojan_calculator.py{Colors.END}")
        
        try:
            with open("trojan_calculator.py", "r", encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
                # Check for signatures
                for sig in trojan_signatures:
                    if sig in content:
                        signatures.append(sig)
                
                if signatures:
                    detected_files.append({
                        'file': 'trojan_calculator.py',
                        'type': 'Trojan Horse',
                        'severity': 'HIGH',
                        'signatures': signatures,
                        'path': os.path.abspath('trojan_calculator.py'),
                        'hash': calculate_file_hash('trojan_calculator.py')
                    })
                    print(f"{Colors.RED}[!] DETECTED: Trojan Horse Calculator{Colors.END}")
                    print(f"{Colors.RED}    Severity: HIGH{Colors.END}")
                    print(f"{Colors.RED}    Signatures found: {len(signatures)}{Colors.END}")
                else:
                    print(f"{Colors.GREEN}[✓] File appears clean{Colors.END}")
        except Exception as e:
            print(f"{Colors.YELLOW}[*] Could not analyze file: {e}{Colors.END}")
    
    # Check for stolen_data directory
    if os.path.exists("stolen_data"):
        print(f"\n{Colors.YELLOW}[*] Analyzing: stolen_data/ directory{Colors.END}")
        
        stolen_files = []
        try:
            for root, dirs, files in os.walk("stolen_data"):
                for file in files:
                    stolen_files.append(os.path.join(root, file))
            
            if stolen_files:
                detected_files.append({
                    'file': 'stolen_data/',
                    'type': 'Stolen Data Repository',
                    'severity': 'MEDIUM',
                    'items': len(stolen_files),
                    'path': os.path.abspath('stolen_data')
                })
                print(f"{Colors.RED}[!] DETECTED: Stolen data repository{Colors.END}")
                print(f"{Colors.RED}    Files found: {len(stolen_files)}{Colors.END}")
                for f in stolen_files[:3]:  # Show first 3 files
                    print(f"{Colors.YELLOW}      • {os.path.basename(f)}{Colors.END}")
                if len(stolen_files) > 3:
                    print(f"{Colors.YELLOW}      ... and {len(stolen_files)-3} more{Colors.END}")
        except Exception as e:
            print(f"{Colors.YELLOW}[*] Could not analyze directory: {e}{Colors.END}")
    
    # Check infected files
    print(f"\n{Colors.YELLOW}[*] Scanning for infected files...{Colors.END}")
    test_files_dir = "test_files"
    if os.path.exists(test_files_dir):
        for file in os.listdir(test_files_dir):
            filepath = os.path.join(test_files_dir, file)
            if os.path.isfile(filepath):
                try:
                    with open(filepath, 'r', errors='ignore') as f:
                        content = f.read()
                        if "INFECTED BY TROJAN" in content:
                            detected_files.append({
                                'file': file,
                                'type': 'Infected File',
                                'severity': 'MEDIUM',
                                'path': filepath,
                                'infection': 'Trojan Marker Found'
                            })
                            print(f"{Colors.RED}[!] INFECTED: {file}{Colors.END}")
                except:
                    continue
    
    return detected_files

def quarantine_malware(detected_items):
    """Quarantine detected malware"""
    print(f"\n{Colors.YELLOW}{'='*60}{Colors.END}")
    print(f"{Colors.PURPLE}{Colors.BOLD}🚫 QUARANTINE OPERATIONS 🚫{Colors.END}")
    print(f"{Colors.YELLOW}{'='*60}{Colors.END}")
    
    # Create quarantine directory if it doesn't exist
    if not os.path.exists("quarantine"):
        os.makedirs("quarantine")
    
    quarantine_log = []
    quarantined_count = 0
    
    for item in detected_items:
        filename = item['file']
        original_path = item.get('path', '')
        
        print(f"\n{Colors.YELLOW}[*] Processing: {filename}{Colors.END}")
        
        try:
            if os.path.exists(original_path):
                # Generate quarantine filename with timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                quarantine_name = f"Q_{timestamp}_{filename}"
                quarantine_path = os.path.join("quarantine", quarantine_name)
                
                # Move to quarantine
                shutil.move(original_path, quarantine_path)
                
                # Log the quarantine
                quarantine_log.append({
                    'timestamp': datetime.now().isoformat(),
                    'original_name': filename,
                    'original_path': original_path,
                    'quarantine_path': quarantine_path,
                    'type': item['type'],
                    'severity': item['severity']
                })
                
                quarantined_count += 1
                print(f"{Colors.GREEN}[✓] Quarantined: {filename}{Colors.END}")
                print(f"{Colors.GREEN}    Moved to: {quarantine_path}{Colors.END}")
                
                # For directories, create a marker file
                if item['type'] == 'Stolen Data Repository':
                    marker_path = os.path.join("stolen_data", "QUARANTINED.txt")
                    with open(marker_path, 'w') as f:
                        f.write(f"This directory was quarantined at {datetime.now()}\n")
            else:
                print(f"{Colors.YELLOW}[*] File not found: {filename}{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[!] Failed to quarantine {filename}: {e}{Colors.END}")
    
    # Save quarantine log
    if quarantine_log:
        log_file = f"scan_reports/quarantine_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        if not os.path.exists("scan_reports"):
            os.makedirs("scan_reports")
        
        with open(log_file, 'w') as f:
            json.dump(quarantine_log, f, indent=2)
    
    return quarantined_count

def generate_report(detected_items, quarantined_count):
    """Generate scan report"""
    print(f"\n{Colors.YELLOW}{'='*60}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}📊 SCAN REPORT 📊{Colors.END}")
    print(f"{Colors.YELLOW}{'='*60}{Colors.END}")
    
    report = {
        'scan_time': datetime.now().isoformat(),
        'total_detected': len(detected_items),
        'quarantined': quarantined_count,
        'detections': detected_items,
        'system_status': 'Secure' if quarantined_count == len(detected_items) else 'At Risk'
    }
    
    print(f"\n{Colors.WHITE}Scan Summary:{Colors.END}")
    print(f"{Colors.GREEN}  Scan Time: {report['scan_time']}{Colors.END}")
    print(f"{Colors.YELLOW}  Total Threats Detected: {report['total_detected']}{Colors.END}")
    print(f"{Colors.BLUE}  Successfully Quarantined: {report['quarantined']}{Colors.END}")
    
    if report['quarantined'] == report['total_detected']:
        print(f"\n{Colors.GREEN}{Colors.BOLD}[✓] ALL THREATS NEUTRALIZED{Colors.END}")
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}[!] SOME THREATS REMAIN{Colors.END}")
    
    print(f"\n{Colors.WHITE}System Status: {Colors.END}", end='')
    if report['system_status'] == 'Secure':
        print(f"{Colors.GREEN}{Colors.BOLD}SECURE{Colors.END}")
    else:
        print(f"{Colors.RED}{Colors.Bold}AT RISK{Colors.END}")
    
    # Save report
    if not os.path.exists("scan_reports"):
        os.makedirs("scan_reports")
    
    report_file = f"scan_reports/scan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n{Colors.CYAN}[*] Detailed report saved to: {report_file}{Colors.END}")
    
    return report

def show_protection_animation():
    """Show system protection animation"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.GREEN}{Colors.BOLD}🛡️  ACTIVATING SYSTEM PROTECTION 🛡️{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")
    
    shields = ["🛡️", "🔒", "🔄", "⚡", "🔍", "🚫"]
    
    for i in range(3):
        for shield in shields:
            print(f"\r{Colors.GREEN}Activating protection {shield} {Colors.END}", end='')
            sys.stdout.flush()
            time.sleep(0.2)
    
    print(f"\n\n{Colors.GREEN}{Colors.BOLD}[✓] SYSTEM PROTECTION ACTIVE{Colors.END}")
    print(f"{Colors.GREEN}[✓] Real-time monitoring enabled{Colors.END}")
    print(f"{Colors.GREEN}[✓] Automatic updates configured{Colors.END}")

def main_menu():
    """Display main menu"""
    while True:
        clear_screen()
        
        menu = f"""
{Colors.CYAN}{Colors.BOLD}
    ╔══════════════════════════════════════════════════╗
    ║           EDUCATIONAL ANTIVIRUS MENU             ║
    ╠══════════════════════════════════════════════════╣
    ║                                                  ║
    ║  1. 🔍 Quick Scan for Trojan Horse               ║
    ║  2. 🚫 Full Scan & Quarantine                    ║
    ║  3. 📊 View Scan Reports                         ║
    ║  4. 🛡️  System Protection Status                 ║
    ║  5. ❌ Exit Antivirus                            ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
{Colors.END}
"""
        print(menu)
        
        choice = input(f"\n{Colors.WHITE}Enter choice (1-5): {Colors.END}")
        
        if choice == '1':
            clear_screen()
            show_antivirus_intro()
            detected = detect_trojan()
            
            if detected:
                print(f"\n{Colors.RED}[!] Threats detected: {len(detected)}{Colors.END}")
                for item in detected:
                    print(f"    • {item['file']} - {item['type']} ({item['severity']})")
            else:
                print(f"\n{Colors.GREEN}[✓] No threats detected!{Colors.END}")
            
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            
        elif choice == '2':
            clear_screen()
            show_antivirus_intro()
            detected = detect_trojan()
            
            if detected:
                action = input(f"\n{Colors.RED}[!] {len(detected)} threats detected! Quarantine? (y/n): {Colors.END}")
                if action.lower() == 'y':
                    quarantined = quarantine_malware(detected)
                    generate_report(detected, quarantined)
                    show_protection_animation()
            else:
                print(f"\n{Colors.GREEN}[✓] No threats detected!{Colors.END}")
            
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            
        elif choice == '3':
            clear_screen()
            print(f"\n{Colors.CYAN}{Colors.BOLD}📁 SCAN REPORTS:{Colors.END}")
            
            if os.path.exists("scan_reports"):
                reports = [f for f in os.listdir("scan_reports") if f.endswith('.json')]
                if reports:
                    for report in sorted(reports)[-5:]:  # Show last 5 reports
                        print(f"\n{Colors.YELLOW}• {report}{Colors.END}")
                        try:
                            with open(os.path.join("scan_reports", report), 'r') as f:
                                data = json.load(f)
                                print(f"  Scan Time: {data.get('scan_time', 'N/A')}")
                                print(f"  Threats: {data.get('total_detected', 0)}")
                                print(f"  Status: {data.get('system_status', 'N/A')}")
                        except:
                            print(f"  Could not read report")
                else:
                    print(f"{Colors.YELLOW}No scan reports found.{Colors.END}")
            else:
                print(f"{Colors.YELLOW}No scan reports directory found.{Colors.END}")
            
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            
        elif choice == '4':
            clear_screen()
            show_protection_animation()
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            
        elif choice == '5':
            print(f"\n{Colors.GREEN}Exiting Educational Antivirus...{Colors.END}")
            print(f"{Colors.GREEN}Stay secure!{Colors.END}")
            time.sleep(2)
            break
            
        else:
            print(f"\n{Colors.RED}Invalid choice! Please enter 1-5.{Colors.END}")
            time.sleep(1)

def main():
    """Main antivirus program"""
    try:
        clear_screen()
        show_antivirus_intro()
        time.sleep(2)
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Antivirus terminated by user{Colors.END}")
        sys.exit(0)

if __name__ == "__main__":
    main()
