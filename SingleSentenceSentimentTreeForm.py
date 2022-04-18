from ui.singleSentenceSentimentTreeForm import singleSentenceSentimentTreeForm

from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QGraphicsScene
from SentenceDependencyTree import SentenceDependencyTree
from TreeGraph import TreeGraph


class SingleSentenceSentimentTreeForm(singleSentenceSentimentTreeForm.Ui_singleSentenceSentimentTreeForm, QtWidgets.QMainWindow):
    def __init__(self, dictionary):
        super(SingleSentenceSentimentTreeForm, self).__init__()
        self.setupUi(self)
        self.dictionary = dictionary
        # -----------------------------Привязка методов к кнопкам---------------------------
        self.generateTreeButton.clicked.connect(self.generate_tree)
        self.clearButton.clicked.connect(self.clear)

    def generate_tree(self):
        text = self.textEditSentense.toPlainText()
        dependency_tree = SentenceDependencyTree(self.dictionary)
        dependency_tree.generate_tree(text)

        graph1 = TreeGraph([dependency_tree.sentiment_by_dictionary['tokens']])
        scene1 = QGraphicsScene()
        scene1.addPixmap(graph1.render_image())
        self.graphicsViewFirstTree.setScene(scene1)
        graph1.clear_files()

        graph2 = TreeGraph([dependency_tree.sentiment_by_rules['tokens']])
        scene2 = QGraphicsScene()
        scene2.addPixmap(graph2.render_image())
        self.graphicsViewSecondTree.setScene(scene2)
        graph2.clear_files()

        self.foundRulesListWidget.addItems(dependency_tree.found_rules)
        self.labelFinalSentiment.setText(f"Итоговая тональность: {dependency_tree.sentence_sentiment}")

    def clear(self):
        self.labelFinalSentiment.setText('') # Итоговая тональность:
        self.textEditSentense.setText('')
        self.graphicsViewFirstTree.setScene(None)
        self.graphicsViewSecondTree.setScene(None)
