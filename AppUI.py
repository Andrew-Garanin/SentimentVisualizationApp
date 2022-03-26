from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QPoint
from PySide2.QtGui import QTextCursor
from PySide2.QtWidgets import QMenu, QMdiSubWindow, QMainWindow
from bs4 import BeautifulSoup

from AddNewWordDialog import AddNewWordDialog
from AddNewWordForm import AddNewWordForm
from ChangeWordSentimentDialog import ChangeWordSentimentDialog
from ChangeWordSentimentForm import ChangeWordSentimentForm
from SentimentHighlighter import Highlighter
from SingleSentenceSentimentTree import SingleSentenceSentimentTree
from SingleSentenceSentimentTreeForm import SingleSentenceSentimentTreeForm
from dictionaries.DictionaryKartaSlovSent import DictionaryKartaSlovSent
from ui.mainMDIForm import mainMDIForm
from SentimentTextMarkupForm import SentimentTextMarkupForm


class MyQtApp(mainMDIForm.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.dictionary = DictionaryKartaSlovSent()  # Словарь!
        self.mdi = self.mdiArea

        # -----------------------------Объявление дочерних форм-----------------------------
        self.sentiment_text_markup_form = None
        self.add_new_word_form = None
        self.change_word_sentiment_form = None
        self.single_sentence_sentiment_tree_form = None

        # -----------------------------Привязка методов к кнопкам---------------------------

        self.menuSentimentTextMarkup.triggered.connect(self.menu_sentiment_text_markup)
        self.menuAddNewWord.triggered.connect(self.menu_add_new_word)
        self.menuChangeWordSentiment.triggered.connect(self.menu_change_word_sentiment)
        self.menuSingleSentence.triggered.connect(self.menu_single_sentence_sentiment_tree)

        self.menuWindowsCascade.triggered.connect(self.menu_windows_cascade)

    # -----------------------------Методы меню-----------------------------

    def menu_sentiment_text_markup(self):
        self.sentiment_text_markup_form = SentimentTextMarkupForm(self.dictionary)
        self.mdi.addSubWindow(self.sentiment_text_markup_form)
        self.sentiment_text_markup_form.show()

    def menu_add_new_word(self):
        self.add_new_word_form = AddNewWordForm(self.dictionary)
        self.add_new_word_form.labelError.clear()
        self.add_new_word_form.newWordEdit.clear()
        self.add_new_word_form.newWordEdit.setFocus()
        self.add_new_word_form.radioButtonPSTV.setChecked(True)
        self.mdi.addSubWindow(self.add_new_word_form)
        self.add_new_word_form.show()

    def menu_change_word_sentiment(self):
        self.change_word_sentiment_form = ChangeWordSentimentForm(self.dictionary)
        self.change_word_sentiment_form.labelError.clear()
        self.change_word_sentiment_form.wordEdit.clear()
        self.change_word_sentiment_form.wordEdit.setFocus()
        self.change_word_sentiment_form.radioButtonPSTV.setChecked(True)
        self.mdi.addSubWindow(self.change_word_sentiment_form)
        self.change_word_sentiment_form.show()

    def menu_single_sentence_sentiment_tree(self):
        self.single_sentence_sentiment_tree_form = SingleSentenceSentimentTreeForm(self.dictionary)
        self.mdi.addSubWindow(self.single_sentence_sentiment_tree_form)
        self.single_sentence_sentiment_tree_form.show()

    def menu_windows_cascade(self):
        self.mdi.cascadeSubWindows()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
