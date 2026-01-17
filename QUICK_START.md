# 🚀 TONER INVENTORY - QUICK START

## 📦 Šta imaš u paketu:

### Glavni fajlovi:
- ✅ `toner_app_multilang.py` - Glavna aplikacija
- ✅ `translations.py` - Prevodi (Srpski/English)
- ✅ `toner_app.ico` - Ikonica aplikacije

### Build fajlovi:
- ✅ `build_exe.py` - Automatski pravi EXE
- ✅ `BUILD_INSTRUCTIONS.md` - Detaljne instrukcije

### Ikonice (različite veličine):
- ✅ `icon_256.png`, `icon_128.png`, `icon_64.png`, `icon_32.png`

---

## 🎯 BRZI START - 2 opcije:

### OPCIJA 1: Python verzija (instant)

```bash
# 1. Raspakuj ZIP
# 2. Otvori terminal u toner_final folderu
# 3. Pokreni:
python toner_app_multilang.py
```

**Potrebno:** Python 3 + PyQt5 + openpyxl

---

### OPCIJA 2: EXE verzija (preporučeno za distribuciju)

```bash
# 1. Raspakuj ZIP
# 2. Otvori terminal u toner_final folderu
# 3. Pokreni:
python build_exe.py

# 4. Sačekaj 2-3 minuta...
# 5. EXE je u: dist/TonerInventory.exe
```

**Benefit:** Radi NA BILO KOM Windows-u bez Python-a!

---

## 🎨 Ikonica

Aplikacija ima lepu ikonicu:
- 🖼️ Plavi štampač
- 🟢 Zeleni toner kartridž sa slovom "T"
- 📊 Progress bar za nivo tonera

Ikonica se automatski primenjuje na:
- Prozor aplikacije
- EXE fajl (Windows)
- Taskbar

---

## ✅ Funkcionalnosti:

- ✅ Dual language (Српски/English)
- ✅ Evidencija tonera, štampača, radnika
- ✅ Automatske narudžbine (kada je stanje ispod minimuma)
- ✅ Mesečna/godišnja statistika potrošnje
- ✅ Istorija narudžbina sa filterom
- ✅ Automatski backup (podešava se)
- ✅ Excel export
- ✅ Search highlighting (tamno zeleno)
- ✅ Čuva podatke u SQLite bazi

---

## 📁 Gde su podaci?

Aplikacija kreira ove fajlove/foldere:
- `toneri.db` - Glavna baza podataka (SQLite)
- `backups/` - Automatski backup-i
- `app_config.json` - Podešavanja (jezik)

**VAŽNO:** Čuvaj `toneri.db` fajl - to su svi tvoji podaci!

---

## 🔧 Instalacija zavisnosti (ako ne radiš EXE):

```bash
pip install PyQt5 openpyxl --break-system-packages
```

---

## 🚀 Distribucija drugima:

### Ako daješ Python verziju:
1. Daj im: `toner_app_multilang.py` + `translations.py`
2. Reci im da instaliraju: `pip install PyQt5 openpyxl`

### Ako daješ EXE verziju (BOLJE!):
1. Napravi EXE sa `python build_exe.py`
2. Daj im samo: `dist/TonerInventory.exe`
3. **To je sve!** Radi bez instalacije!

---

## 💡 Tips:

1. **Backup je bitan!** Podesi automatski backup u app-u
2. **Excel export** - možeš da izvezeš narudžbine u Excel
3. **Search** - koristi search polje (tamno zeleno highlighting)
4. **Filter istorije** - možeš da vidiš istoriju po mesecu/godini
5. **Jezik** - menja se u meniju: Jezik → English

---

## 🐛 Problem?

### Python verzija ne radi:
```bash
pip install PyQt5 openpyxl --break-system-packages
```

### EXE build ne radi:
```bash
pip install pyinstaller --break-system-packages
python build_exe.py
```

### Windows Defender blokira EXE:
- Klikni "More info" → "Run anyway"
- To je normalno za PyInstaller aplikacije

---

## 👨‍💻 Autor:
Igor Malkočević - 2026

---

## 📞 Za više info:
Pogledaj `BUILD_INSTRUCTIONS.md` za detaljne build instrukcije!

**UŽIVAJ U APLIKACIJI!** 🎉
