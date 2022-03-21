from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QPoint
from PySide2.QtGui import QTextCursor
from PySide2.QtWidgets import QMenu, QMdiSubWindow, QMainWindow
from bs4 import BeautifulSoup

from AddNewWordDialog import AddNewWordDialog
from ChangeWordSentimentDialog import ChangeWordSentimentDialog
from SentimentHighlighter import Highlighter
from SingleSentenceSentimentTree import SingleSentenceSentimentTree
from dictionaries.DictionaryKartaSlovSent import DictionaryKartaSlovSent
from ui import main


class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.dictionary = DictionaryKartaSlovSent()  # Словарь!
        self.highlighter = Highlighter(self.textField.document(), QTextCursor(self.textField.document()),
                                       self.textField, self.dictionary)

        # -----------------------------Объявление дочерних форм-----------------------------
        self.add_new_word_dialog = None
        self.change_word_sentiment_dialog = None
        self.single_sentence_sentiment_tree__dialog = None

        # -----------------------------Привязка методов к кнопкам---------------------------
        self.menuOpen.triggered.connect(self.menu_open)
        self.menuSave.triggered.connect(self.menu_save)
        self.menuAddNewWord.triggered.connect(self.menu_add_new_word)
        self.menuChangeWordSentiment.triggered.connect(self.menu_change_word_sentiment)
        self.menuSingleSentence.triggered.connect(self.menu_single_sentence_sentiment_tree)
        self.buttonMarkup.clicked.connect(self.highlight_text)

        self.textField.customContextMenuRequested.connect(self.contextMenuEvent)  # Привязка метода контекстного меню

    def highlight_text(self):
        self.highlighter.highlight_text()

    def highlight_single_word(self, start, length, sentiment):
        self.highlighter.highlight_single_word(start, length, sentiment)

    def contextMenuEvent(self, pos):
        # TODO: Переделать на клёвое контекстное меню
        cursor = self.textField.cursorForPosition(pos)

        cursor.beginEditBlock()

        cursor.movePosition(QTextCursor.StartOfWord)
        start = cursor.position()
        cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor)
        length = cursor.position() - start

        cursor.endEditBlock()

        selected_word = cursor.selectedText()
        menu = self.textField.createStandardContextMenu()

        sub = QMenu(menu)
        sub.setTitle('Изменить тональность')
        menu_PSTV = sub.addAction("Положительная")
        menu_NGTV = sub.addAction("Отрицательная")
        menu_NEUT = sub.addAction("Нейтральная")
        menu.addMenu(sub)
        # if self.highlighter.document() is None:
        #     menu_item.setDisabled(True)

        receiver_PSTV = lambda prop=selected_word, start=start, length=length: self.highlight_single_word(selected_word,
                                                                                                          start, length,
                                                                                                          'PSTV')
        receiver_NGTV = lambda prop=selected_word, start=start, length=length: self.highlight_single_word(selected_word,
                                                                                                          start, length,
                                                                                                          'NGTV')
        receiver_NEUT = lambda prop=selected_word, start=start, length=length: self.highlight_single_word(selected_word,
                                                                                                          start, length,
                                                                                                          'NEUT')

        self.connect(menu_PSTV, QtCore.SIGNAL('triggered()'), receiver_PSTV)
        self.connect(menu_NGTV, QtCore.SIGNAL('triggered()'), receiver_NGTV)
        self.connect(menu_NEUT, QtCore.SIGNAL('triggered()'), receiver_NEUT)

        text_field_pos = QPoint(pos.x() + self.geometry().x(), pos.y() + self.geometry().y())
        menu.popup(text_field_pos)

    # -----------------------------Методы меню-----------------------------
    def menu_open(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', filter='*.txt')
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as file:
                text = file.read()
                self.textField.setText(text)

    def menu_save(self):
        cursor = QTextCursor(self.textField.document())
        html = cursor.document().toHtml()
        soup = BeautifulSoup(html, features="html.parser")
        soup.find('meta')['charset'] = 'utf-8'
        with open('texts_data\\test.html', 'w', encoding='UTF-8') as f:
            f.write(str(soup))

    def menu_add_new_word(self):
        self.add_new_word_dialog = AddNewWordDialog(self.dictionary, parent=self)
        self.add_new_word_dialog.labelError.clear()
        self.add_new_word_dialog.newWordEdit.clear()
        self.add_new_word_dialog.newWordEdit.setFocus()
        self.add_new_word_dialog.radioButtonPSTV.setChecked(True)
        self.add_new_word_dialog.show()

    def menu_change_word_sentiment(self):
        self.change_word_sentiment_dialog = ChangeWordSentimentDialog(self.dictionary, parent=self)
        self.change_word_sentiment_dialog.labelError.clear()
        self.change_word_sentiment_dialog.wordEdit.clear()
        self.change_word_sentiment_dialog.wordEdit.setFocus()
        self.change_word_sentiment_dialog.radioButtonPSTV.setChecked(True)
        self.change_word_sentiment_dialog.show()

    def menu_single_sentence_sentiment_tree(self):
        self.single_sentence_sentiment_tree__dialog = SingleSentenceSentimentTree(self.dictionary, parent=self)
        self.single_sentence_sentiment_tree__dialog.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
