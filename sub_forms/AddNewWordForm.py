from ui.addNewWordForm import addNewWordForm
from PySide2 import QtWidgets
from SentimentType import SentimentType


class AddNewWordForm(addNewWordForm.Ui_addNewWordForm, QtWidgets.QMainWindow):
    def __init__(self, dictionary):
        """
        Форма для добавления нового слова в словарь.
        :param dictionary: тональный словарь
        """
        super(AddNewWordForm, self).__init__()
        self.setupUi(self)
        self.dictionary = dictionary
        self.text_edit_original_style_sheet = self.newWordEdit.styleSheet()  # дефолтный стиль строки ввода слова

        # -----------------------------Привязка методов к кнопкам---------------------------
        self.buttonAdd.clicked.connect(self.add_new_word_to_dictionary)
        self.buttonCancel.clicked.connect(self.cancel)

    def add_new_word_to_dictionary(self):
        """
        Добавляет новое слово в словарь.
        """
        sentiment = ''
        text = self.newWordEdit.text().lower().strip()
        if self.radioButtonPSTV.isChecked():
            sentiment = SentimentType.POSITIVE.value
        if self.radioButtonNGTV.isChecked():
            sentiment = SentimentType.NEGATIVE.value
        if self.radioButtonNEUT.isChecked():
            sentiment = SentimentType.NEUTRAL.value
        if text == '':
            self.newWordEdit.setStyleSheet("border: 1px solid red;")  # changed
            self.labelError.setText('Введите слово')
            self.newWordEdit.setText('')
            return
        if self.dictionary.is_word_exist(text):
            self.newWordEdit.setStyleSheet("border: 1px solid red;")  # changed
            self.labelError.setText('Введённое слово уже есть в словаре')
            return

        # Если не существует, то добавить слово в словарь, в алфавитном порядке
        self.newWordEdit.setStyleSheet(self.text_edit_original_style_sheet)  # back to original
        self.labelError.setText('')
        self.dictionary.add_new_word(text, sentiment)

    def cancel(self):
        pass
