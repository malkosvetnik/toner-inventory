# Changelog

All notable changes to the Toner Inventory System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-01-26

### Added
- **Real-time Stock Counters**
  - Live counter for total toner quantity in Toners tab
  - Live counter for total printer quantity in Printers tab
  - Automatic updates on any change (add/delete/edit)
  - SQL-based calculations for accuracy

- **Print & Export for All Tabs**
  - Print preview (HTML) for Toners tab with browser print button
  - Print preview (HTML) for Printers tab with browser print button
  - Excel export for Toners tab with professional formatting
  - Excel export for Printers tab with professional formatting
  - Dual statistics in reports: different models + total pieces

- **Search Functionality in Dialogs**
  - Real-time search field in "Edit Printer" dialog for filtering toners
  - Real-time search field in "Edit Employee" dialog for filtering printers
  - Preserves checkbox states during filtering

- **Column Width Persistence**
  - All column widths are automatically saved on application close
  - Column widths restored on next application start
  - Powered by QSettings (Windows Registry / Linux config file)
  - Works across all tables: Toners, Printers, Employees, Overview, History

- **Enhanced Overview Tab**
  - Now displays ALL records (including unlinked items)
  - Red background indicators for missing/NULL relationships
  - Clear visibility of incomplete connections
  - Four separate SQL queries for comprehensive data display

### Fixed
- **Status Combobox Bug** - Can now change printer status unlimited times
  - Root cause: Signal not disconnected before table reload
  - Root cause: Wrong data (translated text) saved to database
  - Solution: Complete refactor using `activated` signal instead of `currentTextChanged`
  - Solution: Reverse mapping to convert display text back to Serbian before DB save
  - Added explicit widget cleanup to prevent duplicate comboboxes

- **Search Highlighting Inconsistency** - Red text in Employees tab
  - Changed to white text on green background (consistent with other tabs)
  - Refactored entire search logic for Employees table

- **Edit Toner Dialog Crash** - TypeError when clicking "Izmeni toner"
  - Root cause: Database NULL values in minimalna_kolicina or trenutno_stanje
  - Solution: Added None checks with default values in TonerDialog.__init__()

- **Zero Display Bug** - Empty field instead of "0" in order lists
  - Changed condition from `if value` to `if value is not None`
  - Now correctly displays "0" when stock is zero

- **Overview Tab Missing Records** - Only showed fully connected records
  - Completely rewrote load_pregled() with 4 separate queries
  - Query 1: Fully connected (employee + printer + toner)
  - Query 2: Employees WITHOUT printers
  - Query 3: Printers WITHOUT employees
  - Query 4: Toners WITHOUT printers

### Changed
- **Table Interaction**
  - Changed all tables from Stretch mode to Interactive mode
  - Users can now resize columns by dragging (like Excel)
  - Last column auto-stretches to fill available space

- **Export Report Format**
  - Reports now show both "Different models" count and "Total pieces" count
  - Example: "Različitih tonera: 17 | Ukupno komada: 143"
  - Applies to both Print preview and Excel export

### Technical Improvements
- Added QSettings integration for persistent UI state
- Improved SQL queries for real-time calculations
- Better error handling for NULL database values
- Consistent signal/slot handling across all tables
- Enhanced widget lifecycle management

## [1.0.0] - 2025-XX-XX

### Added
- Initial release
- Basic toner inventory management
- Printer tracking system
- Employee printer assignments
- Order list generation
- Consumption history tracking
- Backup and restore functionality
- Dual language support (Serbian/English)
- Search across all tables
- Excel export for order lists
- Statistics tab with history

### Core Features
- SQLite database backend
- PyQt5 GUI framework
- Multi-tab interface
- Relationship management (toners ↔ printers ↔ employees)
- Color-coded stock levels
- Driver link management
- Configurable settings

---

## Upgrade Notes

### Upgrading from v1.0 to v2.0

Your existing database will work with v2.0 without modifications. However, we recommend:

1. **Create a backup** before upgrading (use built-in Backup feature)
2. **Test the new version** with your existing data
3. **Review the new features** - especially Overview tab and real-time counters

No database migrations required - fully backwards compatible!

### Breaking Changes
None - v2.0 is fully compatible with v1.0 databases.

---

## Future Roadmap (v3.0+)

Planned features for future releases:
- 📊 Charts and statistics dashboard
- 📧 Email notifications for low stock
- 🔔 Desktop notifications
- 📱 QR code generation for quick scanning
- 🌐 Optional web version
- 📅 Printer service calendar
- 📈 Advanced analytics and reporting

---

For full documentation, visit the [Wiki](https://github.com/malkosvetnik/toner-inventory/wiki)
