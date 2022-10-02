import sys
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QLineEdit, QStyle, QToolButton
import controller as c

app = QApplication(sys.argv)
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("phonebook.db")

window = QMainWindow()
window.setMinimumSize(450, 600)
window.setMaximumSize(450, 600)
window.setWindowTitle('Контакты')
font = QtGui.QFont('Monotype Corsiva')
font.setPointSize(16)

window.toolbar = window.addToolBar("File")
window.toolbar.setMovable(False)
window.toolbar.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
window.toolbar.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea)
window.toolbar.setIconSize(QSize(25, 25))
window.toolbar.setStyleSheet("border: 0px; padding: 3px;")
window.setWindowIcon(window.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogListView))

import_icon = QtGui.QIcon("import")
import_btn = QToolButton(text="Импорт", icon=import_icon)
import_btn.clicked.connect(c.import_contacts)
import_btn.setStyleSheet("QToolButton:hover {background: #a5dcff;}")
import_btn.setToolTip("Загрузить файл")
window.toolbar.addWidget(import_btn)

export_icon = QtGui.QIcon("export")
export_btn = QToolButton(text="Экспорт", icon=export_icon)
export_btn.clicked.connect(c.export_contacts)
export_btn.setStyleSheet("QToolButton:hover {background: #a5dcff;}")
export_btn.setToolTip("Выгрузить файл")
window.toolbar.addWidget(export_btn)

delete_icon = QtGui.QIcon("trash")
delete_btn = QToolButton(text="Удалить", icon= delete_icon)
delete_btn.clicked.connect(c.delete_contact)
delete_btn.setStyleSheet("QToolButton:hover {background: #a5dcff;}")
delete_btn.setToolTip("Удалить контакт")
window.toolbar.addWidget(delete_btn)


window.search = QLineEdit()
window.search.setFont(font)
window.search.setGeometry(5, 25, 390, 30)
window.search.setPlaceholderText('Поиск')
window.search.returnPressed.connect(c.find_item)

font.setPointSize(13)

model = QSqlTableModel()
model.setTable("phonebook")
model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
model.setHeaderData(0, Qt.Orientation.Horizontal, "Фамилия")
model.setHeaderData(1, Qt.Orientation.Horizontal, "Имя")
model.setHeaderData(2, Qt.Orientation.Horizontal, "Телефон")
model.setSort(0, Qt.SortOrder.AscendingOrder)
model.select()

window.view_table = QTableView()
window.view_table.setModel(model)
[window.view_table.setColumnWidth(i, 128) for i in range(3)]
window.view_table.setColumnWidth(1, 146)
window.view_table.setColumnWidth(2, 149)
window.view_table.setFont(font)
window.view_table.verticalHeader().hide()

button_1 = QtWidgets.QPushButton()
add_new_icon = QtGui.QIcon("plus")
button_1.setIcon(add_new_icon)
button_1.setIconSize(QSize(30, 30))
button_1.setStyleSheet("border: none")
button_1.clicked.connect(c.add_row)

layout = QVBoxLayout()
layout.addWidget(window.toolbar)
layout.addWidget(window.search)
layout.addWidget(window.view_table)
layout.addWidget(button_1)

widget = QWidget()
widget.setLayout(layout)
window.setCentralWidget(widget)


def create_view(title, model):
    view = QTableView()
    view.verticalHeader().hide()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

