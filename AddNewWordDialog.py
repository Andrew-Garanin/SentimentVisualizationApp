from ui import addWordDialog
from PySide2 import QtWidgets


class AddWordDialog(addWordDialog.Ui_addNewWordDialog, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddWordDialog, self).__init__(parent)
        self.setupUi(self)

        self.buttonAdd.clicked.connect(self.add_new_word_to_dictionary)
        self.buttonCancel.clicked.connect(self.close_dialog)

    def add_new_word_to_dictionary(self):
        pass
        # Проверить существует ли слово в словаре
        # Если не существует, то добавить слово в словарь, в алфавитном порядке
        # Если существует, то не добавлять и выделить поле красным цветом,
        # и подписать его снизу: введёное слово уже есть в словаре

    def close_dialog(self):
        self.close()
