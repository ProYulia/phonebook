import view as m
import file_management as fm
from database import contact_list
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import Qt


def find_item():
    item = m.window.search.text()
    for el in range(m.window.view_table.model().columnCount()):
        indexes = m.window.view_table.model().match(m.window.view_table.model().index(0, el),
                        Qt.ItemDataRole.DisplayRole, item, -1, Qt.MatchFlag.MatchContains)
        for ix in indexes:
            m.window.view_table.selectRow(ix.row())

def add_row():
    m.model.insertRows(m.model.rowCount(), 1)

def delete_contact():
    m.model.removeRow(m.window.view_table.currentIndex().row())

def import_contacts():
    file_name = QFileDialog.getOpenFileName(m.widget,'Импорт контактов', 'Name.csv')[0]
    match file_name[-3:]:
        case 'txt':
            fm.file_read_txt(file_name)
        case 'csv':
            fm.file_read_csv(file_name)
        case '':
            return
        case _:
            error()

def export_contacts():
    file_name = QFileDialog.getOpenFileName(m.widget, 'Экспорт контактов', 'Name.csv')[0]
    match file_name[-3:]:
        case 'txt':
            fm.write_in_txt(file_name, contact_list())
        case 'csv':
            fm.write_in_csv(file_name, contact_list())
        case '':
            return
        case _:
            error()

def error():
    err = m.QMessageBox()
    err.setWindowTitle('Error')
    err.setText('Выбран не верный формат файла')
    err.exec()