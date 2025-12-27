#!/bin/bash
# Educational Trojan Horse Lab Demo Script

echo "================================================"
echo "    EDUCATIONAL TROJAN HORSE LAB DEMO"
echo "    For Kali Linux - Educational Purposes Only"
echo "================================================"
echo ""

echo "Available components:"
echo "1. trojan_calculator.py    - The Trojan Horse"
echo "2. trojan_antivirus.py     - Antivirus Defense"
echo "3. trojan_monitor.py       - Attack Monitoring"
echo ""

echo "Step 1: Checking directory structure..."
ls -la
echo ""

echo "Step 2: Checking test files..."
ls -la test_files/
echo ""

echo "Step 3: IMPORTANT - Open TWO terminal windows"
echo "   Terminal 1: Run the Trojan (this script will do it)"
echo "   Terminal 2: Run the Monitor (you need to do this manually)"
echo ""
echo "In Terminal 2, run these commands:"
echo "   cd $(pwd)"
echo "   python3 trojan_monitor.py"
echo "   Then choose option 2 for real-time monitoring"
echo ""
read -p "Have you opened Terminal 2? Press Enter when ready..."

echo ""
echo "Step 4: Running Trojan Horse Calculator..."
echo "Note: The Trojan will run in this terminal"
echo "      The Monitor should run in Terminal 2"
read -p "Press Enter to start the Trojan..."

python3 trojan_calculator.py

echo ""
echo "Step 5: What to observe:"
echo "  - Terminal 1: Calculator interface (Trojan frontend)"
echo "  - Terminal 2: Real-time monitoring of attacks"
echo "  - Check stolen_data/ directory"
echo "  - Check test_files/ for infections"
echo ""

echo "Step 6: Now run the Antivirus..."
read -p "Press Enter to run antivirus (close other programs first)..."

python3 trojan_antivirus.py

echo ""
echo "Step 7: Final system check..."
echo ""
echo "Quarantine directory:"
ls -la quarantine/ 2>/dev/null || echo "No quarantine directory"

echo ""
echo "Scan reports:"
ls -la scan_reports/ 2>/dev/null || echo "No scan reports"

echo ""
echo "Attack logs:"
ls -la stolen_data/*.log 2>/dev/null | head -5 || echo "No log files"

echo ""
echo "================================================"
echo "         DEMONSTRATION COMPLETE"
echo "================================================"
echo ""
echo "For best learning experience:"
echo "1. Run trojan_calculator.py in one terminal"
echo "2. Run trojan_monitor.py in another terminal"
echo "3. Run trojan_antivirus.py to clean up"
echo "4. Check all generated logs and reports"
