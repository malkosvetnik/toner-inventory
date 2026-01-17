# -*- coding: utf-8 -*-
"""
Translations for Toner Inventory Management System
Serbian (sr) and English (en)
"""

class T:
    """Translation helper class"""
    
    # All translations
    STRINGS = {
        # ===== MAIN WINDOW =====
        'app_title': {'sr': 'Evidencija tonera i štampača', 'en': 'Toner Inventory System'},
        'menu_language': {'sr': 'Jezik', 'en': 'Language'},
        'menu_serbian': {'sr': 'Srpski', 'en': 'Serbian'},
        'menu_english': {'sr': 'Engleski', 'en': 'English'},
        'search_label': {'sr': 'Pretraga:', 'en': 'Search:'},
        'search_placeholder': {'sr': 'Pretraži po bilo čemu...', 'en': 'Search anything...'},
        
        # ===== TABS =====
        'tab_toneri': {'sr': 'Toneri', 'en': 'Toners'},
        'tab_stampaci': {'sr': 'Štampači', 'en': 'Printers'},
        'tab_radnici': {'sr': 'Radnici', 'en': 'Employees'},
        'tab_pregled': {'sr': '📊 PREGLED', 'en': '📊 OVERVIEW'},
        'tab_statistika': {'sr': '📈 STATISTIKA', 'en': '📈 STATISTICS'},
        'tab_istorija': {'sr': '📜 ISTORIJA', 'en': '📜 HISTORY'},
        'tab_backup': {'sr': '💾 BACKUP', 'en': '💾 BACKUP'},
        
        # ===== BUTTONS - COMMON =====
        'btn_add': {'sr': 'Dodaj', 'en': 'Add'},
        'btn_edit': {'sr': 'Izmeni', 'en': 'Edit'},
        'btn_delete': {'sr': 'Obriši', 'en': 'Delete'},
        'btn_close': {'sr': 'Zatvori', 'en': 'Close'},
        'btn_save': {'sr': 'Sačuvaj', 'en': 'Save'},
        'btn_cancel': {'sr': 'Odustani', 'en': 'Cancel'},
        'btn_refresh': {'sr': '🔄 Osveži', 'en': '🔄 Refresh'},
        
        # ===== BUTTONS - SPECIFIC =====
        'btn_add_toner': {'sr': 'Dodaj toner', 'en': 'Add Toner'},
        'btn_edit_toner': {'sr': 'Izmeni toner', 'en': 'Edit Toner'},
        'btn_delete_toner': {'sr': 'Obriši toner', 'en': 'Delete Toner'},
        'btn_record_consumption': {'sr': 'Evidentira potrošnju', 'en': 'Record Consumption'},
        'btn_order_list': {'sr': '📋 NARUDŽBINA', 'en': '📋 ORDER LIST'},
        
        'btn_add_printer': {'sr': 'Dodaj štampač', 'en': 'Add Printer'},
        'btn_edit_printer': {'sr': 'Izmeni štampač', 'en': 'Edit Printer'},
        'btn_delete_printer': {'sr': 'Obriši štampač', 'en': 'Delete Printer'},
        
        'btn_add_employee': {'sr': 'Dodaj radnika', 'en': 'Add Employee'},
        'btn_edit_employee': {'sr': 'Izmeni radnika', 'en': 'Edit Employee'},
        'btn_delete_employee': {'sr': 'Obriši radnika', 'en': 'Delete Employee'},
        
        'btn_preview_print': {'sr': '👁️ Prikaži i štampaj', 'en': '👁️ Preview & Print'},
        'btn_excel_export': {'sr': '📥 Excel export', 'en': '📥 Excel Export'},
        'btn_add_to_history': {'sr': '📜 Dodaj u istoriju', 'en': '📜 Add to History'},
        
        'btn_create_backup': {'sr': '💾 Kreiraj backup sada', 'en': '💾 Create Backup Now'},
        'btn_restore_backup': {'sr': '📥 Restore iz backup-a', 'en': '📥 Restore from Backup'},
        'btn_refresh_stats': {'sr': '🔄 Osveži statistiku', 'en': '🔄 Refresh Statistics'},
        'btn_add_order': {'sr': '➕ Dodaj narudžbinu', 'en': '➕ Add Order'},
        
        # ===== TABLE HEADERS =====
        'col_id': {'sr': 'ID', 'en': 'ID'},
        'col_model': {'sr': 'Model', 'en': 'Model'},
        'col_min_qty': {'sr': 'Min. količina', 'en': 'Min. Qty'},
        'col_stock': {'sr': 'Stanje', 'en': 'Stock'},
        'col_current_stock': {'sr': 'Trenutno stanje', 'en': 'Current Stock'},
        'col_driver_link': {'sr': 'Driver link', 'en': 'Driver Link'},
        'col_for_order': {'sr': 'Za naručivanje', 'en': 'To Order'},
        
        'col_status': {'sr': 'Status', 'en': 'Status'},
        'col_note': {'sr': 'Napomena', 'en': 'Note'},
        
        'col_first_name': {'sr': 'Ime', 'en': 'First Name'},
        'col_last_name': {'sr': 'Prezime', 'en': 'Last Name'},
        
        'col_employee': {'sr': 'Radnik', 'en': 'Employee'},
        'col_printer': {'sr': 'Štampač', 'en': 'Printer'},
        'col_toners': {'sr': 'Toneri', 'en': 'Toners'},
        
        'col_date': {'sr': 'Datum', 'en': 'Date'},
        'col_toner': {'sr': 'Toner', 'en': 'Toner'},
        'col_toner_model': {'sr': 'Model tonera', 'en': 'Toner Model'},
        'col_quantity': {'sr': 'Količina', 'en': 'Quantity'},
        'col_assigned': {'sr': 'Dodeljeno', 'en': 'Assigned'},
        'col_available': {'sr': 'Slobodno', 'en': 'Available'},
        'col_notes': {'sr': 'Napomena', 'en': 'Notes'},
        
        # ===== STATUS VALUES =====
        'status_active': {'sr': 'Aktivan', 'en': 'Active'},
        'status_in_service': {'sr': 'Na servisu', 'en': 'In Service'},
        'status_for_disposal': {'sr': 'Za rashod', 'en': 'For Disposal'},
        'status_all': {'sr': 'Svi', 'en': 'All'},
        
        # ===== FILTER =====
        'filter_label': {'sr': 'Filter:', 'en': 'Filter:'},
        
        # ===== DIALOG TITLES =====
        'dialog_add_toner': {'sr': 'Dodaj toner', 'en': 'Add Toner'},
        'dialog_edit_toner': {'sr': 'Izmeni toner', 'en': 'Edit Toner'},
        'dialog_add_printer': {'sr': 'Dodaj štampač', 'en': 'Add Printer'},
        'dialog_edit_printer': {'sr': 'Izmeni štampač', 'en': 'Edit Printer'},
        'dialog_add_employee': {'sr': 'Dodaj radnika', 'en': 'Add Employee'},
        'dialog_edit_employee': {'sr': 'Izmeni radnika', 'en': 'Edit Employee'},
        
        # ===== LABELS =====
        'label_toner_model': {'sr': 'Model tonera:', 'en': 'Toner Model:'},
        'label_description': {'sr': 'Opis:', 'en': 'Description:'},
        'label_min_qty': {'sr': 'Minimalna količina:', 'en': 'Minimum Quantity:'},
        'label_current_stock': {'sr': 'Trenutno stanje:', 'en': 'Current Stock:'},
        'label_driver_link': {'sr': 'Driver link:', 'en': 'Driver Link:'},
        
        'label_printer_model': {'sr': 'Model štampača:', 'en': 'Printer Model:'},
        'label_serial_number': {'sr': 'Serijski broj:', 'en': 'Serial Number:'},
        'label_quantity': {'sr': 'Količina:', 'en': 'Quantity:'},
        'label_status': {'sr': 'Status:', 'en': 'Status:'},
        'label_note': {'sr': 'Napomena:', 'en': 'Note:'},
        'label_toners_used': {'sr': 'Toneri koje ovaj štampač koristi:', 'en': 'Toners this printer uses:'},
        
        'label_first_name': {'sr': 'Ime', 'en': 'First Name'},
        'label_last_name': {'sr': 'Prezime', 'en': 'Last Name'},
        'label_department': {'sr': 'Odeljenje', 'en': 'Department'},
        'label_printers': {'sr': 'Štampači koje ovaj radnik ima:', 'en': 'Printers this employee has:'},
        'label_printers_employee_has': {'sr': 'Štampači koje ovaj radnik ima:', 'en': 'Printers this employee has:'},
        'col_printer_model': {'sr': 'Model štampača', 'en': 'Printer Model'},
        
        # ===== STATISTICS =====
        'stats_title': {'sr': '📈 STATISTIKA POTROŠNJE TONERA', 'en': '📈 TONER CONSUMPTION STATISTICS'},
        'stats_select_period': {'sr': 'Izaberi period:', 'en': 'Select Period:'},
        'stats_year': {'sr': 'Godina:', 'en': 'Year:'},
        'stats_month': {'sr': 'Mesec:', 'en': 'Month:'},
        'stats_all_time': {'sr': 'Sve vreme', 'en': 'All Time'},
        'stats_click_refresh': {'sr': 'Klikni \'Osveži statistiku\' za prikaz', 'en': 'Click \'Refresh Statistics\' to display'},
        
        'stats_general': {'sr': 'Opšte informacije:', 'en': 'General Information:'},
        'stats_total_toners': {'sr': 'Ukupno tonera u sistemu:', 'en': 'Total toners in system:'},
        'stats_below_min': {'sr': 'Tonera ispod minimalne količine:', 'en': 'Toners below minimum:'},
        'stats_total_stock': {'sr': 'Ukupno tonera na stanju:', 'en': 'Total toner stock:'},
        'stats_consumption': {'sr': 'Potrošnja u periodu:', 'en': 'Consumption in period:'},
        'stats_consumption_30d': {'sr': 'Potrošnja u poslednjih 30 dana:', 'en': 'Consumption in last 30 days:'},
        'stats_top5': {'sr': 'Top 5 tonera po stanju:', 'en': 'Top 5 toners by stock:'},
        'stats_pieces': {'sr': 'komada', 'en': 'pieces'},
        'stats_pcs': {'sr': 'kom', 'en': 'pc'},
        
        # Month names
        'month_1': {'sr': 'Januar', 'en': 'January'},
        'month_2': {'sr': 'Februar', 'en': 'February'},
        'month_3': {'sr': 'Mart', 'en': 'March'},
        'month_4': {'sr': 'April', 'en': 'April'},
        'month_5': {'sr': 'Maj', 'en': 'May'},
        'month_6': {'sr': 'Jun', 'en': 'June'},
        'month_7': {'sr': 'Jul', 'en': 'July'},
        'month_8': {'sr': 'Avgust', 'en': 'August'},
        'month_9': {'sr': 'Septembar', 'en': 'September'},
        'month_10': {'sr': 'Oktobar', 'en': 'October'},
        'month_11': {'sr': 'Novembar', 'en': 'November'},
        'month_12': {'sr': 'Decembar', 'en': 'December'},
        
        # ===== HISTORY =====
        'history_title': {'sr': '📜 ISTORIJA NARUDŽBINA', 'en': '📜 ORDER HISTORY'},
        
        # ===== BACKUP =====
        'backup_title': {'sr': '💾 BACKUP I RESTORE', 'en': '💾 BACKUP & RESTORE'},
        'backup_manual': {'sr': 'Manuelni backup:', 'en': 'Manual Backup:'},
        'backup_auto': {'sr': 'Automatski backup:', 'en': 'Automatic Backup:'},
        'backup_enable': {'sr': 'Omogući automatski backup', 'en': 'Enable Automatic Backup'},
        'backup_day': {'sr': 'Dan u mesecu za backup:', 'en': 'Day of month for backup:'},
        'backup_last': {'sr': 'Poslednji backup:', 'en': 'Last backup:'},
        'backup_never': {'sr': 'Nikada', 'en': 'Never'},
        'backup_select_file': {'sr': 'Izaberi backup fajl', 'en': 'Select backup file'},
        
        # ===== OVERVIEW =====
        'overview_info': {'sr': 'Kompletna slika: ko ima koje štampače i koje tonere', 'en': 'Complete overview: who has which printers and toners'},
        
        # ===== MESSAGES - SUCCESS =====
        'success': {'sr': 'Uspeh', 'en': 'Success'},
        'msg_toner_added': {'sr': 'Toner je dodat!', 'en': 'Toner added!'},
        'msg_toner_edited': {'sr': 'Toner je izmenjen!', 'en': 'Toner updated!'},
        'msg_printer_added': {'sr': 'Štampač je dodat!', 'en': 'Printer added!'},
        'msg_printer_edited': {'sr': 'Štampač je izmenjen!', 'en': 'Printer updated!'},
        'msg_status_changed': {'sr': 'Status promenjen!', 'en': 'Status changed!'},
        'msg_employee_added': {'sr': 'Radnik je dodat!', 'en': 'Employee added!'},
        'msg_employee_edited': {'sr': 'Radnik je izmenjen!', 'en': 'Employee updated!'},
        'msg_consumption_recorded': {'sr': 'Potrošnja evidentirana!', 'en': 'Consumption recorded!'},
        'msg_sent_to_printer': {'sr': 'Dokument poslat na štampač!', 'en': 'Document sent to printer!'},
        'msg_excel_created': {'sr': 'Excel kreiran!', 'en': 'Excel created!'},
        'msg_file': {'sr': 'Fajl:', 'en': 'File:'},
        'msg_location': {'sr': 'Lokacija:', 'en': 'Location:'},
        'msg_backup_created': {'sr': 'Backup kreiran!', 'en': 'Backup created!'},
        'msg_db_restored': {'sr': 'Baza je restorована!\n\nZatvori i ponovo pokreni aplikaciju.', 'en': 'Database restored!\n\nPlease close and restart the application.'},
        'msg_added_to_history': {'sr': 'Dodato {} stavki u istoriju!', 'en': 'Added {} items to history!'},
        
        # ===== MESSAGES - ERRORS =====
        'error': {'sr': 'Greška', 'en': 'Error'},
        'error_select_toner': {'sr': 'Izaberi toner za izmenu!', 'en': 'Select a toner to edit!'},
        'error_select_toner_delete': {'sr': 'Izaberi toner za brisanje!', 'en': 'Select a toner to delete!'},
        'error_select_toner_consumption': {'sr': 'Izaberi toner čija se potrošnja evidentira!', 'en': 'Select a toner to record consumption!'},
        'error_model_required': {'sr': 'Model tonera je obavezan!', 'en': 'Toner model is required!'},
        'error_model_exists': {'sr': 'Toner sa ovim modelom već postoji!', 'en': 'Toner with this model already exists!'},
        
        'error_select_printer': {'sr': 'Izaberi štampač za izmenu!', 'en': 'Select a printer to edit!'},
        'error_select_printer_delete': {'sr': 'Izaberi štampač za brisanje!', 'en': 'Select a printer to delete!'},
        'error_printer_model_required': {'sr': 'Model štampača je obavezan!', 'en': 'Printer model is required!'},
        
        'error_select_employee': {'sr': 'Izaberi radnika za izmenu!', 'en': 'Select an employee to edit!'},
        'error_select_employee_delete': {'sr': 'Izaberi radnika za brisanje!', 'en': 'Select an employee to delete!'},
        'error_name_required': {'sr': 'Ime i prezime su obavezni!', 'en': 'First and last name are required!'},
        
        'error_no_stock': {'sr': 'Nema tonera na stanju!', 'en': 'No toner in stock!'},
        'error_negative_qty': {'sr': 'Količina ne može biti negativna!', 'en': 'Quantity cannot be negative!'},
        'error_must_be_number': {'sr': 'Količina mora biti broj!', 'en': 'Quantity must be a number!'},
        'error_cannot_open_link': {'sr': 'Ne mogu otvoriti link:', 'en': 'Cannot open link:'},
        'error_install_openpyxl': {'sr': 'Instaliraj openpyxl:\npip install openpyxl --break-system-packages', 'en': 'Install openpyxl:\npip install openpyxl'},
        'error_no_data': {'sr': 'Nema podataka za prikaz!', 'en': 'No data to display!'},
        'error_no_export_data': {'sr': 'Nema podataka za export!', 'en': 'No data to export!'},
        'error_db_not_found': {'sr': 'Baza podataka ne postoji!', 'en': 'Database not found!'},
        
        # ===== MESSAGES - CONFIRMATIONS =====
        'confirm': {'sr': 'Potvrda', 'en': 'Confirm'},
        'confirm_delete_toner': {'sr': 'Da li si siguran da želiš da obrišeš ovaj toner?', 'en': 'Are you sure you want to delete this toner?'},
        'confirm_delete_printer': {'sr': 'Da li si siguran da želiš da obrišeš ovaj štampač?', 'en': 'Are you sure you want to delete this printer?'},
        'confirm_delete_employee': {'sr': 'Da li si siguran da želiš da obrišeš ovog radnika?', 'en': 'Are you sure you want to delete this employee?'},
        'confirm_change_status': {'sr': 'Promeni status u \'{}\'?', 'en': 'Change status to \'{}\'?'},
        'confirm_reduce_stock': {'sr': 'Trenutno stanje: {}\n\nSmanji stanje za 1?', 'en': 'Current stock: {}\n\nReduce stock by 1?'},
        'confirm_restore': {'sr': 'UPOZORENJE: Ovo će zameniti trenutnu bazu!\n\nDa li si siguran?', 'en': 'WARNING: This will replace the current database!\n\nAre you sure?'},
        
        # Quantity reduction dialogs
        'unassign_question_title': {'sr': 'Razduži radnika?', 'en': 'Unassign Employee?'},
        'unassign_dialog_title': {'sr': 'Razduži štampač', 'en': 'Unassign Printer'},
        'reducing_quantity': {'sr': 'Smanjuješ količinu sa {} na {}.', 'en': 'Reducing quantity from {} to {}.'},
        'currently_assigned': {'sr': 'Trenutno dodeljeno radnicima ({}):' , 'en': 'Currently assigned to employees ({}):'},
        'want_to_unassign': {'sr': 'Da li želiš da razduziš nekog radnika?', 'en': 'Do you want to unassign any employee?'},
        'must_unassign': {'sr': 'OBAVEZNO je razdužiti {} radnik(a).', 'en': 'MUST unassign {} employee(s).'},
        'choose_employees': {'sr': 'Izaberi koje radnike:', 'en': 'Choose which employees:'},
        'choose_to_unassign': {'sr': 'Izaberi koje radnike da razduziš\n(možeš izabrati od 1 do {}):', 'en': 'Choose which employees to unassign\n(you can select from 1 to {}):'},
        'btn_unassign': {'sr': 'Razduži', 'en': 'Unassign'},
        'must_select_exactly': {'sr': 'Moraš izabrati tačno {} radnik(a)!', 'en': 'You must select exactly {} employee(s)!'},
        'must_select_at_least_one': {'sr': 'Moraš izabrati bar jednog radnika!', 'en': 'You must select at least one employee!'},
        
        # Printer deletion with assignments
        'printer_assigned_to': {'sr': 'Štampač \'{}\' je dodeljen radnicima:', 'en': 'Printer \'{}\' is assigned to employees:'},
        'delete_will_unassign': {'sr': 'Brisanjem štampača će se ukloniti sa svih radnika.', 'en': 'Deleting the printer will unassign it from all employees.'},
        'printer_deleted': {'sr': 'Štampač je obrisan!', 'en': 'Printer deleted!'},
        
        # Toner deletion with links
        'toner_linked_to': {'sr': 'Toner \'{}\' je povezan sa štampačima:', 'en': 'Toner \'{}\' is linked to printers:'},
        'delete_will_unlink': {'sr': 'Brisanjem tonera će se ukloniti sa svih štampača.', 'en': 'Deleting the toner will unlink it from all printers.'},
        'toner_deleted': {'sr': 'Toner je obrisan!', 'en': 'Toner deleted!'},
        
        # ===== INFO MESSAGES =====
        'info': {'sr': 'Info', 'en': 'Info'},
        'info_no_orders': {'sr': 'Nema tonera za naručivanje!', 'en': 'No toners to order!'},
        'info_all_above_min': {'sr': 'Nema tonera za naručivanje!\n\nSvi toneri su iznad minimalne količine.', 'en': 'No toners to order!\n\nAll toners are above minimum quantity.'},
        
        # ===== ORDER LIST =====
        'order_title': {'sr': 'Narudžbina - DEBUG', 'en': 'Order - DEBUG'},
        'order_list_title': {'sr': 'LISTA ZA NARUČIVANJE TONERA', 'en': 'TONER ORDER LIST'},
        'order_no_toners': {'sr': 'Nema tonera za naručivanje!', 'en': 'No toners to order!'},
        'order_debug_info': {'sr': 'DEBUG INFO:', 'en': 'DEBUG INFO:'},
        'order_date': {'sr': 'Datum:', 'en': 'Date:'},
        'order_found': {'sr': '📋 Pronađeno {} toner(a) za naručivanje:', 'en': '📋 Found {} toner(s) to order:'},
        'order_total': {'sr': 'Ukupno stavki za naručivanje: {}', 'en': 'Total items to order: {}'},
        'order_file': {'sr': 'Fajl:', 'en': 'File:'},
        'order_location': {'sr': 'Lokacija:', 'en': 'Location:'},
        
        # ===== PREVIEW =====
        'preview_overview_title': {'sr': 'PREGLED ŠTAMPAČA I TONERA PO RADNICIMA', 'en': 'PRINTER AND TONER OVERVIEW BY EMPLOYEE'},
        'preview_total': {'sr': 'Ukupno zapisa: {}', 'en': 'Total records: {}'},
        'preview_print_btn': {'sr': '🖨️ Štampaj (Ctrl+P)', 'en': '🖨️ Print (Ctrl+P)'},
        
        # ===== TOOLTIPS =====
        'tooltip_click_link': {'sr': 'Klikni da otvoriš link', 'en': 'Click to open link'},
        
        # ===== NOTES =====
        'auto_order_note': {'sr': 'Automatska narudžbina', 'en': 'Automatic order'},
        'manual_order_note': {'sr': 'Narudžbina', 'en': 'Manual order'},
    }
    
    @staticmethod
    def get(key, lang='sr'):
        """Get translated text"""
        return T.STRINGS.get(key, {}).get(lang, key)

# Helper function for easier access
def _(key, lang='sr'):
    """Shortcut for T.get()"""
    return T.get(key, lang)

print("✅ Translations module loaded")
