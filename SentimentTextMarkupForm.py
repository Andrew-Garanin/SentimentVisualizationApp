from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QPoint
from PySide2.QtGui import QTextCursor
from PySide2.QtWidgets import QMenu
from bs4 import BeautifulSoup

from SentimentHighlighter import Highlighter
from ui.sentimentTextMarkupForm import sentimentTextMarkupForm


class SentimentTextMarkupForm(sentimentTextMarkupForm.Ui_sentimentTextMarkupForm, QtWidgets.QMainWindow):
    def __init__(self, dictionary):
        super(SentimentTextMarkupForm, self).__init__()
        self.setupUi(self)
        self.dictionary = dictionary
        self.highlighter = Highlighter(self.textField.document(), QTextCursor(self.textField.document()),
                                       self.textField, self.dictionary)

        # -----------------------------Привязка методов к кнопкам---------------------------
        self.menuOpen.triggered.connect(self.menu_open)
        self.menuSave.triggered.connect(self.menu_save)
        self.buttonMarkup.clicked.connect(self.highlight_text)

        self.textField.customContextMenuRequested.connect(self.contextMenuEvent)  # Привязка метода контекстного меню

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

        receiver_PSTV = lambda prop=selected_word, start=start, length=length: self.highlight_single_word(
                                                                                                          start, length,
                                                                                                          'PSTV')
        receiver_NGTV = lambda prop=selected_word, start=start, length=length: self.highlight_single_word(
                                                                                                          start, length,
                                                                                                          'NGTV')
        receiver_NEUT = lambda prop=selected_word, start=start, length=length: self.highlight_single_word(
                                                                                                          start, length,
                                                                                                          'NEUT')

        self.connect(menu_PSTV, QtCore.SIGNAL('triggered()'), receiver_PSTV)
        self.connect(menu_NGTV, QtCore.SIGNAL('triggered()'), receiver_NGTV)
        self.connect(menu_NEUT, QtCore.SIGNAL('triggered()'), receiver_NEUT)

        text_field_pos = QPoint(pos.x() + self.geometry().x(), pos.y() + self.geometry().y())
        menu.popup(text_field_pos)
