from ui import addNewWordDialog
from PySide2 import QtWidgets


class AddNewWordDialog(addNewWordDialog.Ui_addNewWordDialog, QtWidgets.QDialog):
    def __init__(self, dictionary, parent=None):
        super(AddNewWordDialog, self).__init__(parent)
        self.setupUi(self)
        self.dictionary = dictionary
        self.buttonAdd.clicked.connect(self.add_new_word_to_dictionary)
        self.buttonCancel.clicked.connect(self.close_dialog)
        self.ss = self.newWordEdit.styleSheet()  # original saved

    def add_new_word_to_dictionary(self):
        text = self.newWordEdit.text()
        if text.strip() == '':
            self.newWordEdit.setStyleSheet("border: 1px solid red;")  # changed
            self.labelError.setText('Введите слово')
            self.newWordEdit.setText('')
            return
        if self.dictionary.is_word_already_exist(text):
            self.newWordEdit.setStyleSheet("border: 1px solid red;")  # changed
            self.labelError.setText('Введённое слово уже есть в словаре')
            return

        self.newWordEdit.setStyleSheet(self.ss)  # back to original
        self.labelError.setText('')
        print("Добавляем!")
        self.dictionary.add_new_word(text, 'PSTV')

        # Если не существует, то добавить слово в словарь, в алфавитном порядке

    def close_dialog(self):
        self.close()
