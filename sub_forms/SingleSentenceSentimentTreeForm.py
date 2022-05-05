import PySide2

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
        self.dependency_tree = SentenceDependencyTree(self.dictionary)
        # -----------------------------Привязка методов к кнопкам---------------------------
        self.generateTreeButton.clicked.connect(self.generate_tree)
        self.clearButton.clicked.connect(self.clear)
        self.unknownWordsButton.clicked.connect(self.showUnknownWords)

    def generate_tree(self):
        self.foundRulesListWidget.clear()
        text = self.textEditSentense.toPlainText()
        #self.dependency_tree = SentenceDependencyTree(self.dictionary)
        self.dependency_tree.build_trees(text)

        graph1 = TreeGraph(self.dependency_tree.sentiment_by_dictionary['tokens'])
        scene1 = QGraphicsScene()
        scene1.addPixmap(graph1.render_image())
        self.graphicsViewFirstTree.setScene(scene1)
        graph1.clear_files()

        graph2 = TreeGraph(self.dependency_tree.sentiment_by_rules['tokens'])
        scene2 = QGraphicsScene()
        scene2.addPixmap(graph2.render_image())
        self.graphicsViewSecondTree.setScene(scene2)
        graph2.clear_files()

        self.foundRulesListWidget.addItems(self.dependency_tree.found_rules)
        self.labelFinalSentiment.setText(f"Итоговая тональность: {self.dependency_tree.get_sentence_sentiment()}")

    def showUnknownWords(self):
        self.dependency_tree.show_unknown_words()

    def clear(self):
        self.labelFinalSentiment.setText('') # Итоговая тональность:
        self.textEditSentense.setText('')
        self.graphicsViewFirstTree.setScene(None)
        self.graphicsViewSecondTree.setScene(None)
        self.foundRulesListWidget.clear()

    # def closeEvent(self, event):
    #     self.dictionary.clear_unknown_words()
