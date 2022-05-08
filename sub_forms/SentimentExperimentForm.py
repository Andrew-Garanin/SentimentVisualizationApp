from PySide2 import QtWidgets

from ui.sentimentExperimentForm import sentimentExperimentForm
import pandas as pd
from SentimentExperiment import SentimentExperiment


class SentimentExperimentForm(sentimentExperimentForm.Ui_sentimentExperimentForm, QtWidgets.QMainWindow):
    def __init__(self, dictionary):
        """
        Форма для проведения эксперимента по разметке и анализу корпуса предложений из входного файла.
        :param dictionary: Тональный словарь
        """
        super(SentimentExperimentForm, self).__init__()
        self.setupUi(self)
        self.dictionary = dictionary
        self.sentence_markup_file = None
        self.progress_bar = QtWidgets.QProgressBar()

        # -----------------------------Привязка методов к кнопкам---------------------------
        self.filePathSelectButton.clicked.connect(self.menu_open)
        self.makeExperimentButton.clicked.connect(self.make_experiment)

    def menu_open(self) -> None:
        """
        Диалог выбора файла с размеченными предложениями.
        """
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', filter='*.csv')
        if file_path:
            self.filePathLineEdit.setText(file_path)

    def make_experiment(self):
        with open(self.filePathLineEdit.text(), 'r', encoding='UTF-8') as file:
            self.sentence_markup_file = pd.read_csv(file, quotechar='\"', sep=',')
        self._initialize_progress_bar(len(self.sentence_markup_file))
        experiment = SentimentExperiment(self.dictionary, self.sentence_markup_file, self.progress_bar)
        experiment.make_experiment()

    def _initialize_progress_bar(self, maximum: int) -> None:
        """
        Устанавливает параметры для элемента формы progress bar и добавляет его на форму.
        :param maximum: число предложений во входном файле
        """
        self.progress_bar.setRange(0, maximum)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedHeight(17)
        self.progress_bar.setFixedWidth(125)

        self.statusbar.addPermanentWidget(self.progress_bar)
        self.progress_bar.setVisible(True)
