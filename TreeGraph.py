from collections import Counter

from graphviz import Digraph
from tempfile import mkstemp
import pathlib
import tempfile
from termcolor import colored
import os
import uuid


class TreeGraph(Digraph):

    def __init__(self, json_tree: list[dict], dictionary):
        super().__init__()
        self.main_dep = ['nsubj', 'nsubj:pass', 'obj', 'iobj', 'obl', 'obl:agent', 'nmod', 'amod', 'det', 'advmod']  #Зависимости пар слов, за которыми следим
        self.dictionary = dictionary
        self._create(json_tree, json_tree[0]['id'])
        self._files_to_delete = []

    def _create(self, json_tree: list[dict], parent_index):
        """Creates a graph."""
        for element in json_tree:
            if element['children']:
                self._create_node(element, parent_index)
            else:
                self._create_leaf(element, parent_index)

    def _create_node(self, element: dict, parent_index: int):
        """Creates a node of graph."""
        self.node(str(element['id']), f"{element['id']}\\n{element['text']}\\n{element['pos']}", shape='ellipse', style='filled')
        sentiment = self.dictionary.get_word_tag(element['lemma'])
        self.set_color(str(element['id']), sentiment)
        element['sentiment'] = sentiment
        if element['dependency'] != 'ROOT':
            self.edge(str(parent_index), str(element['id']), label=element['dependency'])  # стрелочка
        self._create(element['children'], element['id'])

    def _create_leaf(self, element: dict, parent_index: int):
        """Creates a leaf of graph."""
        self.node(str(element['id']), f"{element['id']}\\n{element['text']}\\n{element['pos']}", shape='ellipse', style='filled')
        self.edge(str(parent_index), str(element['id']), label=element['dependency'])
        sentiment = self.dictionary.get_word_tag(element['lemma'])
        self.set_color(str(element['id']), sentiment)
        element['sentiment'] = sentiment

    def set_color(self, identifier: str, sentiment: str):
        """Set the node's color depends from sentiment."""
        if identifier == '-1':
            return
        if sentiment == 'PSTV':
            color = 'green'
        elif sentiment == 'NGTV':
            color = 'red'
        else:
            color = 'gray'
        self.node(identifier, shape='ellipse', style='filled', fillcolor=color)

    def show(self):
        """Shows the tree graph after script executing."""
        self.view(mkstemp('.gv')[1])

    def render_image(self):
        a = self.render(filename=str(uuid.uuid4()), directory=tempfile.gettempdir(), format='svg')
        self._files_to_delete.append(a)
        return a

    def clear_files(self):
        for el in self._files_to_delete:
            os.remove(el)

    def save_source(self, save_path: pathlib.Path):
        """Saves .gz file."""
        with open(save_path, 'w') as gz_file:
            gz_file.write(self.source)

    def save_image(self, save_path: pathlib.Path, fmt: str):
        """Saves .pdf, .png or .svg file."""
        if save_path.suffix == fmt:
            save_path = pathlib.Path(str(save_path).rstrip(fmt))
        self.render(save_path, format=fmt.lstrip('.'), cleanup=True)

    def seacrch_dep(self, json_tree: list[dict], parent):
        dep_array = []
        for element in json_tree:
            if element['children']:
                element = self.seacrch_dep(element['children'], element)
                # if element['dependency'] in self.main_dep:
                #     print(colored(f"{element['parent_id']}-{element['id']} {element['text']} {parent_text} | ПРАВИЛО: {self.get_sentiment_type(element['dependency'])} | DEP: {element['dependency']} | POS: {element['pos']}", 'green'))
            #else:
            if element['dependency'] in self.main_dep:
                dep_array.append(self.calculate_sentiment_by_rules(parent, element))
                #dep_array.append(f"{element['text']} {parent['text']}")
                #print(colored(f"{element['parent_id']}-{element['id']} {element['text']} {parent['text']} | ПРАВИЛО: {self.get_sentiment_type(element['dependency'])} | DEP: {element['dependency']} | POS: {element['pos']}", 'green'))
            else:
                dep_array.append(element['sentiment'])
        print(f"{parent['id']}:{dep_array}")
        parent['sentiment'] = self.calculate_node_sentiment_recoloring(dep_array)
        self.set_color(str(parent['id']), parent['sentiment'])
        #print(f"{parent['id']}:{parent['dependency']}")
        return parent

    def get_sentiment_type(self, dependency):
        if dependency in ['nsubj', 'nsubj:pass']:
            return 'Подлежащее - сказуемое'
        if dependency in ['obj', 'iobj']:
            return 'Дополнение - дополняемое действие'
        if dependency in ['obl', 'obl:agent', 'advmod']:#advmod &&&
            return 'Обстоятельство - действие'
        if dependency in ['nmod']:
            return 'Дополнение - дополняемый предмет'
        if dependency in ['amod', 'det']:
            return 'Определение - определяемое'

    def calculate_sentiment_by_rules(self, parent, child):
        positive = 'PSTV'
        negative = 'NGTV'
        neutral = 'NEUT'
        if child['dependency'] in ['nsubj', 'nsubj:pass']:  # Подлежащее - сказуемое
            if child['sentiment'] == positive:
                if parent['sentiment'] == positive:
                    return positive
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return positive
            if child['sentiment'] == negative:
                if parent['sentiment'] == positive:
                    return neutral
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return negative
            if child['sentiment'] == neutral:
                if parent['sentiment'] == positive:
                    return positive
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return neutral

        if child['dependency'] in ['amod', 'det']:  # Определение - определяемое
            if child['sentiment'] == negative:
                if parent['sentiment'] == positive:
                    return negative
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return negative # было neutral
            if child['sentiment'] == positive:
                if parent['sentiment'] == positive:
                    return positive
                if parent['sentiment'] == negative:
                    return neutral
                if parent['sentiment'] == neutral:
                    return positive
            if child['sentiment'] == neutral:
                if parent['sentiment'] == positive:
                    if parent['dependency'] in ['nsubj', 'nsubj:pass', 'ROOT']:  # Положительный, если определяется подлежащее ROOT????
                        return positive
                    if parent['dependency'] in ['obj', 'iobj', 'nmod']:  # нейтральный, если определяется дополнение
                        return neutral
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return neutral

        if child['dependency'] in ['nmod']:  # Дополнение - дополняемый предмет
            if child['sentiment'] == negative:
                if parent['sentiment'] == positive:
                    return neutral
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return negative
            if child['sentiment'] == positive:
                if parent['sentiment'] == positive:
                    return positive
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return positive
            if child['sentiment'] == neutral:
                if parent['sentiment'] == positive:
                    return positive
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return neutral

        if child['dependency'] in ['obj', 'iobj']:  # Дополнение - дополняемое действие
            if child['sentiment'] == negative:
                if parent['sentiment'] == positive:
                    return negative
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return negative
            if child['sentiment'] == positive:
                if parent['sentiment'] == positive:
                    return positive
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return neutral

            if child['sentiment'] == neutral:
                if parent['sentiment'] == positive:
                    return positive
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return neutral

        if child['dependency'] in ['obl', 'obl:agent', 'advmod']:  # Действие - обстоятельство advmod ???
            if child['sentiment'] == negative:
                if parent['sentiment'] == positive:
                    return negative
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return neutral
            if child['sentiment'] == positive:
                if parent['sentiment'] == positive:
                    return positive
                if parent['sentiment'] == negative:
                    return neutral
                if parent['sentiment'] == neutral:
                    return positive
            if child['sentiment'] == neutral:
                if parent['sentiment'] == positive:
                    return positive
                if parent['sentiment'] == negative:
                    return negative
                if parent['sentiment'] == neutral:
                    return neutral

    def calculate_node_sentiment_recoloring(self, sentiments: [str]):
        c = Counter(sentiments)
        if len(c) == 1 and 'NEUT' in c:
            return 'NEUT'
        if 'NEUT' in c:
            c.pop('NEUT', None)
        max_val = max(c.values())
        final_dict = {k: v for k, v in c.items() if v == max_val}
        if len(final_dict) == 1:
            return list(final_dict.keys())[0]
        else:
            if len(final_dict) == 2:
                return 'NEUT'
            else:
                return list(final_dict.keys())[0]
