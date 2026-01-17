# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-17

### Added
- 📦 **Toner Management System**
  - Track stock levels with automatic reordering alerts
  - Inline editing for quick stock updates
  - Minimum quantity thresholds
  - Driver link storage

- 🖨️ **Printer Inventory**
  - Quantity tracking (Total, Assigned, Available)
  - Smart assignment validation
  - Status management (Active, In Service, For Disposal)
  - Color-coded availability indicators
  - Toner compatibility tracking

- 👥 **Employee Management**
  - Assign printers to employees
  - Automatic validation (prevents over-assignment)
  - Track assignments per employee

- 📊 **Statistics & Reports**
  - Monthly consumption reports
  - Yearly consumption trends
  - Top toners by stock/consumption
  - Excel and HTML export

- 📜 **Order History**
  - Track all toner orders with timestamps
  - Filter by year and month
  - Automatic cleanup (2-year retention)
  - Manual order entry

- 🛒 **Smart Ordering System**
  - Automatic detection of toners below minimum
  - Order list dialog with multiple export options
  - Preview and print functionality
  - Add to history directly from order list

- 💾 **Backup & Restore**
  - Automatic scheduled backups
  - Manual backup creation
  - Safe restore with pre-restore backup
  - Configurable backup schedule

- 🔍 **Search & Filter**
  - Real-time search across all tabs
  - Highlighting of matching results
  - Tab indicators for search matches
  - Status-based filtering

- 🌐 **Dual Language Support**
  - Complete Serbian interface
  - Complete English interface
  - Instant language switching
  - All dialogs and messages translated

- 🎨 **User Interface**
  - Clean, professional design
  - Custom application icon
  - Tab-based navigation
  - Inline editing
  - Color-coded indicators
  - Responsive layout

### Features Detail

#### Smart Quantity Management
- Prevent reducing printer quantity below assigned count
- Optional unassignment dialog when reducing quantity
- Shows which employees are affected
- Flexible: can choose to unassign or cancel

#### Cascade Delete Protection
- Warns before deleting printers assigned to employees
- Shows list of affected employees
- Warns before deleting toners linked to printers
- Shows list of affected printers
- Automatic cleanup of all relationships

#### Data Integrity
- SQLite database with proper foreign keys
- Automatic database migration for updates
- Transaction-based operations
- Validation at every input point

### Technical

#### Stack
- Python 3.8+
- PyQt5 for GUI
- SQLite for database
- openpyxl for Excel export
- PyInstaller for EXE packaging

#### Database Schema
- `toneri` - Toner records
- `stampaci` - Printer records
- `radnici` - Employee records
- `radnik_stampaci` - Employee-Printer assignments (M2M)
- `stampac_toneri` - Printer-Toner compatibility (M2M)
- `istorija_narudzbi` - Order history
- `backup_settings` - Backup configuration

### Build & Distribution
- Automated EXE build script
- PyInstaller configuration included
- Standalone executable (no Python required)
- ~50-80 MB final EXE size

---

## [Unreleased]

### Planned Features
- Dark mode theme
- Barcode/QR code scanning
- Cost tracking per toner
- Supplier management
- Email notifications for low stock
- Web API for integrations
- Multi-user support with roles
- Cloud backup integration

---

## Release Notes

### Version 1.0.0
First stable release! This version includes all core functionality for managing toner inventory, printer assignments, and generating reports. The application is production-ready and has been thoroughly tested.

**Highlights:**
- ✅ Complete dual-language support (SR/EN)
- ✅ Smart validation prevents data inconsistencies
- ✅ Cascade delete protection
- ✅ Automatic backup system
- ✅ Professional UI with custom icon
- ✅ Export to Excel and HTML
- ✅ Comprehensive documentation

**Known Limitations:**
- Single-user only (no login system)
- Desktop-only (no web/mobile version)
- No email notifications yet

---

[1.0.0]: https://github.com/malkosvetnik/toner-inventory/releases/tag/v1.0.0
