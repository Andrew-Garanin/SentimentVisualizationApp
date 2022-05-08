from ui.changeWordSentimentForm import changeWordSentimentForm
import spacy
from PySide2 import QtWidgets
from PySide2.QtWidgets import QCompleter
from SentimentType import SentimentType


def convert_sentiment(sentiment):
    if sentiment == SentimentType.POSITIVE.value:
        return 'положительная'
    if sentiment == SentimentType.NEGATIVE.value:
        return 'отрицательная'
    if sentiment == SentimentType.NEUTRAL.value:
        return 'нейтральная'


class ChangeWordSentimentForm(changeWordSentimentForm.Ui_changeWordSentimentForm, QtWidgets.QMainWindow):
    def __init__(self, dictionary):
        """
        Форма для изменения тональности слова из словаря.
        :param dictionary: тональный словарь
        """
        super(ChangeWordSentimentForm, self).__init__()
        self.setupUi(self)
        self.dictionary = dictionary
        self.nlp = spacy.load("ru_core_news_lg")
        self.text_edit_original_style_sheet = self.wordEdit.styleSheet()  # original saved

        # -----------------------------Привязка методов к кнопкам---------------------------
        self.buttonChange.clicked.connect(self.change_word_sentiment)
        self.wordEdit.textChanged.connect(self.word_edit_text_changed_event)

        # -----------------------------Подсказка для поля выбора слов-----------------------
        words = self.dictionary.get_words()
        completer = QCompleter(words)
        self.wordEdit.setCompleter(completer)

    def word_edit_text_changed_event(self):
        word = self.wordEdit.text()

        doc = self.nlp(word)
        root = None
        for sentence in doc.sents:
            root = sentence.root

        if not self.dictionary.is_word_exist(root.text):
            self.currentWordSentimentLabel.setText('Тональность текущего слова: неизвестно')
            return
        self.currentWordSentimentLabel.setText(f'Тональность текущего слова: {convert_sentiment(self.dictionary.get_word_tag(root))}')

    def change_word_sentiment(self):
        """
        Изменяет тональность слова
        """
        word = self.wordEdit.text().lower().strip()

        doc = self.nlp(word)
        root = None
        for sentence in doc.sents:
            root = sentence.root

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

        if self.dictionary.get_word_tag(root) == sentiment:
            self.wordEdit.setStyleSheet(self.text_edit_original_style_sheet)  # back to original
            self.labelError.setStyleSheet("color: rgb(255, 165, 0);")  # changed
            self.labelError.setText('У введённого слова уже установлена такая тональность')
            return

        self.wordEdit.setStyleSheet(self.text_edit_original_style_sheet)  # back to original
        self.labelError.setText('')
        self.dictionary.change_word_sentiment(root.text, sentiment)
        self.currentWordSentimentLabel.setText(f'Тональность текущего слова: {convert_sentiment(self.dictionary.get_word_tag(root))}')
