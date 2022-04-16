from PySide2 import QtWidgets
import csv
from ui.sentimentExperimentForm import sentimentExperimentForm
import pandas as pd


class SentimentExperimentForm(sentimentExperimentForm.Ui_sentimentExperimentForm, QtWidgets.QMainWindow):
    def __init__(self, dictionary):
        super(SentimentExperimentForm, self).__init__()
        self.setupUi(self)
        self.dictionary = dictionary
        self.sentence_markup_file = None
        # -----------------------------Привязка методов к кнопкам---------------------------
        self.filePathSelectButton.clicked.connect(self.menu_open)
        self.makeExperimentButton.clicked.connect(self.make_experiment)

    def menu_open(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file')
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as file:
                #self.sentence_markup_file = csv.reader(file, quotechar='"', delimiter=',', skipinitialspace=True)
                self.sentence_markup_file = pd.read_csv(file, quotechar='\"', sep=',')

    def make_experiment(self):
        for index, row in self.sentence_markup_file.iterrows():
            print(row['Sentence'])
            print(row['Sentiment'])

    def closeEvent(self, event):
        self.sentence_markup_file = None
        print("close")
