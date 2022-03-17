import json

from PySide2.QtWidgets import QGraphicsScene

from TreeGraph import TreeGraph
from ui import singleSentenceSentimentTree
from PySide2 import QtWidgets
from termcolor import colored


class SingleSentenceSentimentTree(singleSentenceSentimentTree.Ui_singleSentenceSentimentTree, QtWidgets.QDialog):
    def __init__(self, dictionary, parent=None):
        super(SingleSentenceSentimentTree, self).__init__(parent)
        self.setupUi(self)
        self.dictionary = dictionary

        # -----------------------------Привязка методов к кнопкам---------------------------
        self.generateTreeButton.clicked.connect(self.generate_tree)
        self.clearButton.clicked.connect(self.clear)

    def create_leaf(self, parent, id, parent_id, text, dependency, pos, lemma, sentiment):
        parent.append(
            {'id': id, 'parent_id': parent_id, 'text': text, 'dependency': dependency, 'pos': pos, 'lemma': lemma,
             'sentiment': sentiment, 'children': []})
        return len(parent) - 1

    def create_tree(self, token, parents_children):
        for child in token:
            if not [child_ for child_ in child.children]:
                if child.is_punct:
                    continue
                self.create_leaf(parents_children, child.i, child.head.i,
                            child.text, child.dep_, child.pos_, child.lemma_, '')
            else:
                i = self.create_leaf(parents_children, child.i, child.head.i,
                                child.text, child.dep_, child.pos_, child.lemma_, '')
                self.create_tree(child.children, parents_children[i]['children'])

    def generate_tree(self):
        text = self.textEditSentense.toPlainText()
        self.doc = self.dictionary.nlp(text)

        self.main_json = dict()
        self.main_json['text'] = self.doc.text

        self.root = None
        for sent in self.doc.sents:
            self.root = sent.root

        self.main_json['tokens'] = dict()
        self.main_json['tokens']['id'] = self.root.i
        self.main_json['tokens']['text'] = self.root.text
        self.main_json['tokens']['dependency'] = self.root.dep_
        self.main_json['tokens']['pos'] = self.root.pos_
        self.main_json['tokens']['lemma'] = self.root.lemma_
        self.main_json['tokens']['sentiment'] = ''
        self.main_json['tokens']['children'] = []

        self.create_tree(self.root.children, self.main_json['tokens']['children'])
        print(json.dumps(self.main_json, ensure_ascii=False, indent=4))

        graph = TreeGraph([self.main_json['tokens']], self.dictionary)
        #graph.attr(label=self.main_json['text'], labelloc="t")

        scene1 = QGraphicsScene()

        scene1.addPixmap(graph.render_image())
        self.graphicsViewFirstTree.setScene(scene1)


        print(colored('-----------------------Найденные правила для выведения тональности-----------------------',
                      'green'))
        aboba = graph.seacrch_dep([self.main_json['tokens']], dict({'id': -1}))  # Поиск правил
        print(colored('-----------------------------------------------------------------------------------------',
                      'green'))
        scene2 = QGraphicsScene()

        scene2.addPixmap(graph.render_image())
        self.graphicsViewSecondTree.setScene(scene2)
        self.labelFinalSentiment.setText(f"Итоговая тональность: {aboba['sentiment']}")
        graph.clear_files()

    def clear(self):
        self.labelFinalSentiment.setText('') # Итоговая тональность:
        self.textEditSentense.setText('')
        self.graphicsViewFirstTree.setScene(None)
        self.graphicsViewSecondTree.setScene(None)
