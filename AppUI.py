from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import SIGNAL, Qt, QPoint
from PySide2.QtGui import QTextCursor, QTextCharFormat, QBrush
from PySide2.QtWidgets import QMenu

from ui import main
from SentimentHighlighter import Highlighter
from AddNewWordDialog import AddNewWordDialog
from ChangeWordSentimentDialog import ChangeWordSentimentDialog
from dictionaries.DictionaryKartaSlovSent import DictionaryKartaSlovSent
from bs4 import BeautifulSoup


class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)

        self.menuOpen.triggered.connect(self.menu_open_action)
        self.buttonMarkup.clicked.connect(self.highlight_text)
        self.textField.customContextMenuRequested.connect(self.contextMenuEvent)

        self.dictionary = DictionaryKartaSlovSent()

        self.add_new_word_dialog = AddNewWordDialog(self.dictionary, parent=self)
        self.menuAddNewWord.triggered.connect(self.menu_add_new_word_action)

        self.change_word_sentiment_dialog = ChangeWordSentimentDialog(self.dictionary, parent=self)
        self.menuChangeWordSentiment.triggered.connect(self.menu_change_word_sentiment)

        self.highlighter = Highlighter(self.textField.document(), QTextCursor(self.textField.document()), self.textField)

        self.menuSave.triggered.connect(self.menu_save)

    def menu_save(self):
        cursor = QTextCursor(self.textField.document())
        html = cursor.document().toHtml()
        soup = BeautifulSoup(html, features="html.parser")
        soup.find('meta')['charset'] = 'utf-8'
        with open('texts_data\\test.html', 'w', encoding='UTF-8') as f:
            f.write(str(soup))

    def highlight_text(self):
        self.highlighter.highlight_text()

    def highlight_single_word(self, selected_word, start, length, sentiment):
        print(selected_word, start, length)
        self.highlighter.highlight_single_word(start, length, sentiment)

    def contextMenuEvent(self, pos):
        cursor = self.textField.cursorForPosition(pos)
        #self.textField.setTextCursor(cursor)

        cursor.beginEditBlock()

        cursor.movePosition(QTextCursor.StartOfWord)
        start = cursor.position()
        cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor)
        length = cursor.position() - start

        cursor.endEditBlock()

        selected_word = cursor.selectedText()
        menu = self.textField.createStandardContextMenu()
        #menu_item = menu.addAction("Изменить тональность")

        sub = QMenu(menu)
        sub.setTitle('Изменить тональность')
        menu_PSTV = sub.addAction("Положительная")
        menu_NGTV = sub.addAction("Отрицательная")
        menu_NEUT = sub.addAction("Нейтральная")
        menu.addMenu(sub)
        # if self.highlighter.document() is None:
        #     menu_item.setDisabled(True)

        receiver_PSTV = lambda prop=selected_word, start=start, length=length: self.highlight_single_word(selected_word, start, length, 'PSTV')
        receiver_NGTV = lambda prop=selected_word, start=start, length=length: self.highlight_single_word(selected_word, start, length, 'NGTV')
        receiver_NEUT = lambda prop=selected_word, start=start, length=length: self.highlight_single_word(selected_word, start, length, 'NEUT')

        self.connect(menu_PSTV, QtCore.SIGNAL('triggered()'), receiver_PSTV)
        self.connect(menu_NGTV, QtCore.SIGNAL('triggered()'), receiver_NGTV)
        self.connect(menu_NEUT, QtCore.SIGNAL('triggered()'), receiver_NEUT)

        text_field_pos = QPoint(pos.x() + self.geometry().x(), pos.y() + self.geometry().y())
        menu.popup(text_field_pos)

    def menu_open_action(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', filter='*.txt')
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as file:
                text = file.read()
                self.textField.setText(text)

    def menu_add_new_word_action(self):
        self.add_new_word_dialog.labelError.clear()
        self.add_new_word_dialog.newWordEdit.clear()
        self.add_new_word_dialog.newWordEdit.setFocus()
        self.add_new_word_dialog.radioButtonPSTV.setChecked(True)
        self.add_new_word_dialog.show()

    def menu_change_word_sentiment(self):
        self.change_word_sentiment_dialog.labelError.clear()
        self.change_word_sentiment_dialog.wordEdit.clear()
        self.change_word_sentiment_dialog.wordEdit.setFocus()
        self.change_word_sentiment_dialog.radioButtonPSTV.setChecked(True)
        self.change_word_sentiment_dialog.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
