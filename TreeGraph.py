from graphviz import Digraph
from tempfile import mkstemp
import pathlib
import tempfile
import os
import uuid


class TreeGraph(Digraph):
    def __init__(self, json_tree: list[dict]):
        super().__init__()
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
        self.node(str(element['id']), f"{element['text']}\\n{element['pos']}", shape='ellipse', style='filled')
        self.set_color(str(element['id']), element['sentiment'])
        if element['dependency'] != 'ROOT':
            self.edge(str(parent_index), str(element['id']), label=element['dependency'])  # стрелочка
        self._create(element['children'], element['id'])

    def _create_leaf(self, element: dict, parent_index: int):
        """Creates a leaf of graph."""
        self.node(str(element['id']), f"{element['text']}\\n{element['pos']}", shape='ellipse', style='filled')
        self.edge(str(parent_index), str(element['id']), label=element['dependency'])  # стрелочка
        self.set_color(str(element['id']), element['sentiment'])

    def set_color(self, identifier: str, sentiment: str):
        """Set the node's color depends from sentiment."""
        if identifier == '-1':  # абстрактный узел - представляет тональность всего предложения целиком
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
