from PySide2 import QtWidgets
import csv
from ui.sentimentExperimentForm import sentimentExperimentForm
import pandas as pd
from SentenceDependencyTree import SentenceDependencyTree


class SentimentExperimentForm(sentimentExperimentForm.Ui_sentimentExperimentForm, QtWidgets.QMainWindow):
    def __init__(self, dictionary):
        super(SentimentExperimentForm, self).__init__()
        self.setupUi(self)
        self.dictionary = dictionary
        self.sentence_markup_file = None

        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setValue(0)
        self.statusbar.addPermanentWidget(self.progress_bar)
        # -----------------------------Привязка методов к кнопкам---------------------------
        self.filePathSelectButton.clicked.connect(self.menu_open)
        self.makeExperimentButton.clicked.connect(self.make_experiment)

    def menu_open(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file')
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as file:
                self.sentence_markup_file = pd.read_csv(file, quotechar='\"', sep=',')

    def make_experiment(self):
        count = 0
        n = 250
        self.initialize_progress_bar(n)
        for index, row in self.sentence_markup_file.head(n).iterrows():
            dependency_tree = SentenceDependencyTree(row['Sentence'], dictionary=self.dictionary)
            # print(dependency_tree.sentence_sentiment)
            # print(row['Sentence'])
            # print(row['Sentiment'])
            if self.convert_sentiment_tag(row['Sentiment']) == dependency_tree.sentence_sentiment:
                count += 1
            self.progress_bar.setValue(self.progress_bar.value()+1)
        print(count)
        self.progress_bar.setValue(0)

    def initialize_progress_bar(self, maximum):
        self.progress_bar.setRange(0, maximum)

    def closeEvent(self, event):
        self.sentence_markup_file = None
        print("close")

    def convert_sentiment_tag(self, tag):
        if tag == 'positive':
            return 'PSTV'
        elif tag == 'negative':
            return 'NGTV'
        else:
            return 'NEUT'