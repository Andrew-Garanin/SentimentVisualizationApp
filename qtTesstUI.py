from PyQt5.QtGui import QTextDocument
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import SIGNAL, Qt, QPoint
from PySide2.QtGui import QTextCursor
from PySide2.QtWidgets import QMenu

from ui import main
from highlighter import MyHighlighter


def print_to_console(text):
    print(text)


def proposalSelected(selectedWord):
    fixed = print_to_console(selectedWord)
    # self.textField.textCursor().insertText(fixed)


class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.menu_open.triggered.connect(self.menu_open_action)
        self.submit_btn.clicked.connect(self.highlight)

        self.textField.customContextMenuRequested.connect(self.contextMenuEvent)

    def contextMenuEvent(self, pos):
        #  menu = self.textField.createStandardContextMenu(pos)
        cursor = self.textField.cursorForPosition(pos)
        self.textField.setTextCursor(cursor)

        cursor.beginEditBlock()

        cursor.movePosition(QTextCursor.StartOfWord)
        cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor)

        cursor.endEditBlock()

        selectedword = cursor.selectedText()
        menu = self.textField.createStandardContextMenu()
        menuItem = menu.addAction("Test Action")

        receiver = lambda prop=selectedword: proposalSelected(prop)
        self.connect(menuItem, QtCore.SIGNAL('triggered()'), receiver)
        text_field_pos = QPoint(pos.x() + self.geometry().x(), pos.y() + self.geometry().y())
        menu.popup(text_field_pos)

    def menu_open_action(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', filter='*.txt')
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as file:
                text = file.read()
                self.textField.setText(text)

    def highlight(self):
        doc = self.textField.document()
        highlighter = MyHighlighter(doc)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
