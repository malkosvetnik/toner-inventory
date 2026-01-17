# 📦 Kreiranje EXE fajla za Toner Inventory

## 🎯 Šta dobijaš:
- **TonerInventory.exe** - Standalone aplikacija
- **Veličina:** ~50-80 MB
- **Radi na Windows-u** bez instaliranog Python-a
- **Uključuje:** Python + PyQt5 + sve biblioteke

---

## 🛠️ Kako napraviti EXE:

### Metod 1: Automatski (Preporučeno)

```bash
# 1. Proveri da imaš sve fajlove:
#    - toner_app_multilang.py
#    - translations.py
#    - toner_app.ico
#    - build_exe.py

# 2. Pokreni build script:
python build_exe.py

# 3. Sačekaj 2-3 minuta...

# 4. EXE je u: dist/TonerInventory.exe
```

---

### Metod 2: Manuelno

```bash
# 1. Instaliraj PyInstaller
pip install pyinstaller --break-system-packages

# 2. Build EXE
pyinstaller --onefile --windowed \
    --name "TonerInventory" \
    --icon toner_app.ico \
    --add-data "translations.py:." \
    --noconsole \
    --clean \
    toner_app_multilang.py

# 3. EXE je u: dist/TonerInventory.exe
```

---

## 📁 Struktura nakon build-a:

```
/build/              (privremeni fajlovi - možeš obrisati)
/dist/
  └── TonerInventory.exe  ← OVO je tvoja aplikacija!
TonerInventory.spec   (build konfiguracija)
```

---

## 🚀 Testiranje EXE:

```bash
cd dist
./TonerInventory.exe
```

**Ili:** Duplim klikom na `TonerInventory.exe`

---

## 📤 Distribucija:

### Šta poslati drugima:
1. **TonerInventory.exe** (glavni fajl)
2. **toneri.db** (opciono - ako hoćeš da pošalješ sa podacima)

### Šta NE treba slati:
- ❌ build/ folder
- ❌ Python fajlove (.py)
- ❌ .spec fajl

---

## ⚠️ Napomene:

### Windows Defender Warning
Moguće je da Windows Defender prijavi upozorenje pri prvom pokretanju:
- **Razlog:** PyInstaller EXE fajlovi se često označavaju kao "nepoznati"
- **Rešenje:** Klikni "More info" → "Run anyway"

### Veličina EXE
EXE je ~50-80 MB jer uključuje:
- ✅ Python interpreter
- ✅ PyQt5 biblioteku
- ✅ SQLite
- ✅ Sve zavisnosti

**Benefit:** Radi na bilo kom Windows-u **bez instalacije!**

---

## 🎨 Ikonica

Aplikacija koristi custom ikonicu:
- **Dizajn:** Plavi štampač sa zelenim toner kartridžom
- **Format:** .ico (Windows standard)
- **Veličine:** 16x16, 32x32, 64x64, 128x128, 256x256

---

## 🐛 Troubleshooting

### "PyInstaller not found"
```bash
pip install pyinstaller --break-system-packages
```

### "ModuleNotFoundError: translations"
Proveri da je `translations.py` u istom folderu kao `toner_app_multilang.py`

### EXE se ne pokreće
1. Proveri da imaš Windows 10/11
2. Pokušaj build sa `--debug all` flagom
3. Pokreni iz CMD/PowerShell da vidiš error poruku

---

## ✅ Checklist pre distribucije:

- [ ] EXE se pokreće
- [ ] Testiran Add/Edit/Delete
- [ ] Testirana promena jezika
- [ ] Testiran backup/restore
- [ ] Ikonica se prikazuje
- [ ] Nema error poruka

---

## 📞 Podrška

Igor Malkočević - 2026
