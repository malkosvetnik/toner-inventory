# 📦 GitHub Upload Uputstva - Verzija 2.0

## 📁 Fajlovi za upload

Ovo su SVI fajlovi koje treba da upload-uješ na GitHub:

### Obavezni fajlovi (MORA):
1. ✅ `toner_app_multilang.py` - glavna aplikacija
2. ✅ `translations.py` - prevodi
3. ✅ `README.md` - dokumentacija
4. ✅ `CHANGELOG.md` - lista promena
5. ✅ `requirements.txt` - Python zavisnosti
6. ✅ `LICENSE` - MIT licenca
7. ✅ `.gitignore` - šta ne treba u git

### Opcionalni fajlovi (DOBRO JE):
8. ✅ `CONTRIBUTING.md` - kako kontribuirati
9. ✅ `RELEASE_NOTES.md` - za GitHub Release

### Fajlovi koje NE treba upload-ovati:
❌ `toneri.db` - baza podataka (user data)
❌ `app_config.json` - user config
❌ `*.pyc` - compiled Python fajlovi
❌ `__pycache__/` - cache folder
❌ `venv/` - virtual environment

---

## 🚀 Koraci za GitHub Update

### 1️⃣ Priprema (Local)

```bash
# Proveri da li imaš git instaliran
git --version

# Ako nemaš git, skini sa: https://git-scm.com/
```

### 2️⃣ Kloniraj svoj postojeći repo (ako već imaš)

```bash
cd C:\Projects  # ili gde god držiš projekte
git clone https://github.com/malkosvetnik/toner-inventory.git
cd toner-inventory
```

### 3️⃣ Dodaj nove fajlove

Kopiraj sve fajlove iz `outputs/` foldera u tvoj git folder:
- toner_app_multilang.py
- translations.py
- README.md
- CHANGELOG.md
- requirements.txt
- LICENSE
- .gitignore
- CONTRIBUTING.md

### 4️⃣ Commit i Push

```bash
# Dodaj sve nove fajlove
git add .

# Commit sa verzijom
git commit -m "Release v2.0.0 - Major feature update"

# Push na GitHub
git push origin main
```

### 5️⃣ Napravi GitHub Release

1. **Idi na svoj GitHub repo**
   - https://github.com/malkosvetnik/toner-inventory

2. **Klikni "Releases"** (desna strana)

3. **Klikni "Create a new release"**

4. **Popuni:**
   - Tag version: `v2.0.0`
   - Release title: `v2.0.0 - Major Feature Update`
   - Description: Copy-paste iz `RELEASE_NOTES.md`

5. **Upload EXE fajla:**
   - U "Attach binaries" sekciji
   - Upload `toner_app_v2.0.exe` (tvoj kompajlirani exe)

6. **Klikni "Publish release"**

---

## 📸 Screenshots (Opcionalno ali PREPORUČUJEM)

Napravi `screenshots/` folder u repo-u i dodaj:
- `toneri_tab.png` - Toneri tab screenshot
- `stampaci_tab.png` - Štampači tab screenshot
- `pregled_tab.png` - Pregled tab screenshot
- `narucivanje.png` - Naručivanje dialog

**Kako napraviti screenshot:**
1. Pokreni aplikaciju
2. Windows: `Windows + Shift + S` (Snipping Tool)
3. Screenshot-uj svaki tab
4. Sačuvaj u `screenshots/` folder
5. Git add i push

---

## 🎯 Checklist pre upload-a

Pre nego što pushneš na GitHub, proveri:

- [ ] **README.md** ima tačan link ka tvojim screenshots-ima
- [ ] **README.md** ima malkosvetnik
- [ ] **LICENSE** ima tvoje ime i 2026 godinu
- [ ] **EXE fajl** je build-ovan i testiran
- [ ] **Database fajl** (`toneri.db`) NIJE u git-u (proveri .gitignore)
- [ ] **Verzija** je 2.0.0 svuda (README, CHANGELOG, Release)

---

## 🔄 Kako ažurirati README sa pravim username-om

Otvori `README.md` i zameni:
- `yourusername` → malkosvetnik
- `[@yourusername]` → tvoj pravi username

**Primer:**
```markdown
# Pre
- GitHub: [@yourusername](https://github.com/yourusername)

# Posle
- GitHub: [@malkosvetnik](https://github.com/malkosvetnik)
```

---

## 📧 Šta dalje?

Nakon što uploaduješ:

1. **Share link** - Podeli link na LinkedIn/Facebook
2. **README badge** - Dodaj cool badges (već ima u README)
3. **Star tvoj repo** - Daj sebi prvu zvezdicu! ⭐
4. **Watch repo** - Prati ko daje stars

---

## 🆘 Pomoć

Ako zaglavljuješ negde:
- GitHub Desktop app: https://desktop.github.com/ (lakši od command line)
- GitHub docs: https://docs.github.com/
- Meni se javi ako zatreba help!

---

## 🎉 Gotovo!

Kada sve ovo završiš, imaćeš:
- ✅ Profesionalan GitHub repo
- ✅ Dokumentovan projekat
- ✅ Release sa EXE download-om
- ✅ Open source projekt koji ljudi mogu koristiti

**Good luck!** 🚀
