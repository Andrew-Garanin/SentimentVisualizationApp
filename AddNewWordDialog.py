from ui import addNewWordDialog
from PySide2 import QtWidgets


class AddNewWordDialog(addNewWordDialog.Ui_addNewWordDialog, QtWidgets.QDialog):
    def __init__(self, dictionary, parent=None):
        super(AddNewWordDialog, self).__init__(parent)
        self.setupUi(self)
        self.dictionary = dictionary
        self.text_edit_original_style_sheet = self.newWordEdit.styleSheet()

        # -----------------------------Привязка методов к кнопкам---------------------------
        self.buttonAdd.clicked.connect(self.add_new_word_to_dictionary)
        self.buttonCancel.clicked.connect(self.close_dialog)

    def add_new_word_to_dictionary(self):
        sentiment = ''
        text = self.newWordEdit.text()
        if self.radioButtonPSTV.isChecked():
            sentiment = 'PSTV'
        if self.radioButtonNGTV.isChecked():
            sentiment = 'NGTV'
        if self.radioButtonNEUT.isChecked():
            sentiment = 'NEUT'
        if text.strip() == '':
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

    def close_dialog(self):
        self.close()
