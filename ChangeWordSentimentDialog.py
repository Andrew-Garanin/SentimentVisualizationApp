from PySide2.QtWidgets import QCompleter

from ui import changeWordSentimentDialog
from PySide2 import QtWidgets


class ChangeWordSentimentDialog(changeWordSentimentDialog.Ui_changeWordSentimentDialog, QtWidgets.QDialog):
    def __init__(self, dictionary, parent=None):
        super(ChangeWordSentimentDialog, self).__init__(parent)
        self.setupUi(self)
        self.dictionary = dictionary
        self.buttonChange.clicked.connect(self.change_word_sentiment)
        self.buttonCancel.clicked.connect(self.close_dialog)
        self.ss = self.wordEdit.styleSheet()  # original saved

        words = self.dictionary.get_words()
        completer = QCompleter(words)
        self.wordEdit.setCompleter(completer)

    def change_word_sentiment(self):
        pass

    def close_dialog(self):
        self.close()
