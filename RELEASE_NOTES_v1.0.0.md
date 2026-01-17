# 🎉 Toner Inventory System v1.0.0 - Initial Release

**First stable release!** Professional desktop application for managing printer toners, printers, and employee assignments.

---

## ✨ Highlights

- 📦 **Complete toner inventory management** - Track stock, automatic reordering alerts
- 🖨️ **Smart printer assignment system** - Quantity tracking (Total/Assigned/Available)
- 👥 **Employee management** - Track printer assignments with validation
- 📊 **Statistics & reports** - Monthly/yearly consumption analysis
- 🌐 **Dual language support** - Serbian and English (switchable)
- 💾 **Backup & restore** - Automatic scheduled + manual backups
- 📤 **Export functionality** - Excel and HTML export
- 🔍 **Smart search** - Real-time search with result highlighting

---

## 📥 Downloads

### 🪟 **Windows Users (Recommended)**

**[📦 Download TonerInventory.exe](https://drive.google.com/file/d/1XPa-cZBaTMDkuDslSpHb_tXVXytTnfDk/view?usp=drive_link)** (~50-80 MB)

- ✅ No installation required
- ✅ No Python needed
- ✅ Just download and run!
- ✅ Standalone executable

### 🐍 **Python Users (Cross-platform)**

Download source code (zip or tar.gz) below, then:

```bash
# Install dependencies
pip install PyQt5 openpyxl

# Run application
python toner_app_multilang.py
```

### 🔨 **Build Your Own**

Want to build the EXE yourself?

```bash
# Install PyInstaller
pip install pyinstaller

# Run build script
python build_exe.py

# Find EXE in dist/ folder
```

See [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md) for details.

---

## ✨ Features

### 📦 Toner Management
- Stock level tracking with minimum thresholds
- Automatic detection of toners below minimum
- Quick stock reduction (inline editing)
- Driver link storage for easy access
- Order list generation with multiple export options

### 🖨️ Printer Inventory
- **Quantity tracking** - Total, Assigned, Available columns
- **Smart validation** - Prevents over-assigning printers
- **Status management** - Active, In Service, For Disposal
- **Toner compatibility** - Link printers to compatible toners
- **Color-coded indicators** - Green (available) / Red (none available)

### 👥 Employee Management
- Assign multiple printers to employees
- Automatic validation (can't assign unavailable printers)
- Track all assignments per employee
- Easy printer reassignment

### 🛒 Smart Ordering
- Automatic detection of toners below minimum stock
- Order list dialog with preview
- Export to Excel or HTML
- Add orders directly to history
- Print-ready format

### 📊 Statistics & Reports
- **Monthly consumption** - Detailed breakdown by toner
- **Yearly consumption** - 12-month view with totals
- **Top toners** - By stock level
- **General stats** - Total stock, items below minimum
- Export to Excel or HTML

### 📜 Order History
- Track all toner orders with timestamps
- Filter by year and month
- Manual order entry
- Automatic cleanup (keeps 2 years of history)
- Notes for each order

### 💾 Backup & Restore
- **Automatic backups** - Schedule monthly backups
- **Manual backups** - Create backup anytime
- **Safe restore** - Pre-restore backup before restoring
- Configurable backup day

### 🔍 Search & Filter
- Real-time search across all tabs
- Highlighting of matching results
- Tab indicators for search matches
- Status-based filtering for printers

### 🌐 Language Support
- Complete Serbian (Српски) interface
- Complete English interface
- Instant language switching
- All dialogs, messages, and labels translated

---

## 🛡️ Data Protection Features

### Cascade Delete Protection
When deleting printers or toners, the system:
- Shows which employees/printers are affected
- Lists all connections that will be removed
- Requires explicit confirmation
- Automatically cleans up all relationships

### Smart Quantity Management
When reducing printer quantity:
- Checks if printers are assigned to employees
- Offers optional unassignment dialog
- Shows which employees would be affected
- Validates before allowing reduction

### Data Integrity
- SQLite database with proper foreign keys
- Transaction-based operations
- Validation at every input point
- Automatic database migrations

---

## 📖 Documentation

- [Quick Start Guide](QUICK_START.md) - Get started in 5 minutes
- [Build Instructions](BUILD_INSTRUCTIONS.md) - Create your own EXE
- [Contributing Guidelines](CONTRIBUTING.md) - How to contribute
- [Changelog](CHANGELOG.md) - Version history

---

## 🛠️ Tech Stack

- **Python 3.8+** - Core language
- **PyQt5** - Desktop GUI framework
- **SQLite** - Embedded database
- **openpyxl** - Excel file generation
- **PyInstaller** - EXE packaging

---

## 📦 Use Cases

Perfect for:
- 🏢 Small and medium businesses
- 🏫 Schools and universities
- 🏥 Hospitals and clinics
- 🏭 Manufacturing facilities
- 💼 IT support teams
- 📚 Libraries with print services

---

## 🐛 Known Limitations

- Single-user only (no login system)
- Desktop-only (no web/mobile version)
- No email notifications (yet)
- Windows EXE only (Linux/Mac users must run from source)

---

## 🔮 Future Plans

Considering for future releases:
- [ ] Dark mode theme
- [ ] Barcode/QR code scanning
- [ ] Cost tracking per toner
- [ ] Email notifications for low stock
- [ ] Multi-user support with roles
- [ ] Cloud backup integration

See [Roadmap in README](README.md#-roadmap) for more.

---

## 🙏 Acknowledgments

Thanks to:
- PyQt5 for the excellent GUI framework
- The Python community for amazing libraries
- All future contributors and users!

---

## 💬 Support

- 🐛 **Found a bug?** [Open an issue](../../issues/new)
- 💡 **Have a suggestion?** [Start a discussion](../../discussions)
- ⭐ **Like the project?** Give it a star!
- 🤝 **Want to contribute?** See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

**TL;DR:** Free to use, modify, and distribute!

---

## 🎯 Installation Instructions

### Windows (EXE)

1. **Download** `TonerInventory.exe` from the link above
2. **Run** the executable (no installation needed)
3. **First launch** creates `toneri.db` database automatically
4. **Start managing** your inventory!

**Note:** Windows may show "Windows protected your PC" warning. Click "More info" → "Run anyway" (this is normal for unsigned executables).

### From Source (All Platforms)

```bash
# 1. Clone or download source
git clone https://github.com/malkosvetnik/toner-inventory.git
cd toner-inventory

# 2. Install dependencies
pip install PyQt5 openpyxl

# 3. Run
python toner_app_multilang.py
```

---

## 📸 Screenshots

Check out the [README](README.md#-screenshots) for screenshots of all features!

---

## ⭐ Show Your Support

If this project helped you, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs you find
- 💡 Suggesting new features
- 🤝 Contributing code or translations
- 📢 Sharing with others who might need it

---

**Made with ❤️ for IT departments everywhere**

**Version:** 1.0.0  
**Release Date:** January 17, 2026  
**Author:** malkosvetnik
