from ui.changeWordSentimentForm import changeWordSentimentForm

from PySide2 import QtWidgets
from PySide2.QtWidgets import QCompleter
from SentimentType import SentimentType


class ChangeWordSentimentForm(changeWordSentimentForm.Ui_changeWordSentimentForm, QtWidgets.QMainWindow):
    def __init__(self, dictionary):
        """
        Форма для изменения тональности слова из словаря.
        :param dictionary: тональный словарь
        """
        super(ChangeWordSentimentForm, self).__init__()
        self.setupUi(self)
        self.dictionary = dictionary
        self.text_edit_original_style_sheet = self.wordEdit.styleSheet()  # original saved

        # -----------------------------Привязка методов к кнопкам---------------------------
        self.buttonChange.clicked.connect(self.change_word_sentiment)

        # -----------------------------Подсказка для поля выбора слов-----------------------
        words = self.dictionary.get_words()
        completer = QCompleter(words)
        self.wordEdit.setCompleter(completer)

    def change_word_sentiment(self):
        """
        Изменяет тональность слова
        """
        word = self.wordEdit.text().lower().strip()
        sentiment = ''
        if self.radioButtonPSTV.isChecked():
            sentiment = SentimentType.POSITIVE.value
        if self.radioButtonNGTV.isChecked():
            sentiment = SentimentType.NEGATIVE.value
        if self.radioButtonNEUT.isChecked():
            sentiment = SentimentType.NEUTRAL.value

        words = self.dictionary.get_words()
        if word not in words:
            self.wordEdit.setStyleSheet("border: 1px solid red;")  # changed
            self.labelError.setStyleSheet("color: rgb(255, 0, 0);")  # changed
            self.labelError.setText('Такого слова нет в словаре')
            return

        if self.dictionary.get_word_tag(word) == sentiment:
            self.wordEdit.setStyleSheet(self.text_edit_original_style_sheet)  # back to original
            self.labelError.setStyleSheet("color: rgb(255, 165, 0);")  # changed
            self.labelError.setText('У введённого слова уже установлена такая тональность')
            return

        self.wordEdit.setStyleSheet(self.text_edit_original_style_sheet)  # back to original
        self.labelError.setText('')
        self.dictionary.change_word_sentiment(word, sentiment)
