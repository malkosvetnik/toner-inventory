#!/usr/bin/env python3
"""
Build script for Toner Inventory System
Creates standalone EXE for Windows
"""

import os
import sys

print("=" * 60)
print("TONER INVENTORY - EXE BUILDER")
print("=" * 60)

# Check if PyInstaller is installed
try:
    import PyInstaller
    print("✅ PyInstaller found")
except ImportError:
    print("❌ PyInstaller not found!")
    print("Installing PyInstaller...")
    os.system(f"{sys.executable} -m pip install pyinstaller --break-system-packages")

# Create PyInstaller command
cmd = f"""pyinstaller --onefile --windowed \
    --name "TonerInventory" \
    --icon toner_app.ico \
    --add-data "translations.py:." \
    --noconsole \
    --clean \
    toner_app_multilang.py
"""

print("\n📦 Building EXE...")
print(f"Command: {cmd}")
print()

result = os.system(cmd)

if result == 0:
    print("\n" + "=" * 60)
    print("✅ BUILD SUCCESSFUL!")
    print("=" * 60)
    print("\n📁 EXE lokacija: dist/TonerInventory.exe")
    print("📦 Veličina: ~50-80 MB (sadrži Python + PyQt5)")
    print("\n🚀 Testiranje:")
    print("   cd dist")
    print("   ./TonerInventory.exe")
else:
    print("\n❌ Build failed!")
    sys.exit(1)

