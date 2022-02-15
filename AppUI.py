from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import SIGNAL, Qt, QPoint
from PySide2.QtGui import QTextCursor

from ui import main
from SentimentHighlighter import SentimentHighlighter
from AddNewWordDialog import AddWordDialog


def print_to_console(text):
    print(text)


def proposalSelected(selected_word):
    print_to_console(selected_word)
    # self.textField.textCursor().insertText(fixed)


class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.menuOpen.triggered.connect(self.menu_open_action)
        self.buttonMarkup.clicked.connect(self.highlight)
        self.textField.customContextMenuRequested.connect(self.contextMenuEvent)

        self.add_new_word_dialog = AddWordDialog(self)
        self.menuAddNewWord.triggered.connect(self.menu_add_new_word_action)

    def contextMenuEvent(self, pos):
        #  menu = self.textField.createStandardContextMenu(pos)
        cursor = self.textField.cursorForPosition(pos)
        self.textField.setTextCursor(cursor)

        cursor.beginEditBlock()

        cursor.movePosition(QTextCursor.StartOfWord)
        cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor)

        cursor.endEditBlock()

        selected_word = cursor.selectedText()
        menu = self.textField.createStandardContextMenu()
        menu_item = menu.addAction("Изменить тональность")

        receiver = lambda prop=selected_word: proposalSelected(prop)
        self.connect(menu_item, QtCore.SIGNAL('triggered()'), receiver)
        text_field_pos = QPoint(pos.x() + self.geometry().x(), pos.y() + self.geometry().y())
        menu.popup(text_field_pos)

    def menu_open_action(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', filter='*.txt')
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as file:
                text = file.read()
                self.textField.setText(text)

    def menu_add_new_word_action(self):
        self.add_new_word_dialog.newWordEdit.clear()
        self.add_new_word_dialog.newWordEdit.setFocus()
        self.add_new_word_dialog.radioButtonPSTV.setChecked(True)
        self.add_new_word_dialog.show()

    def highlight(self):
        doc = self.textField.document()
        highlighter = SentimentHighlighter(doc)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()