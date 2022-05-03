from collections import Counter
import json
from SentimentType import SentimentType
import autoit
import spacy


def get_sentiment_type(dependency: str) -> str:
    """
    Определяет строковое представление 
    :param dependency:
    :return:
    """
    if dependency in ['nsubj', 'nsubj:pass']:
        return 'Подлежащее - сказуемое'
    if dependency in ['obj', 'iobj']:
        return 'Дополнение - дополняемое действие'
    if dependency in ['obl', 'obl:agent', 'advmod']:  # advmod ???
        return 'Обстоятельство - действие'
    if dependency in ['nmod']:
        return 'Дополнение - дополняемый предмет'
    if dependency in ['amod', 'det']:
        return 'Определение - определяемое'


class SentenceDependencyTree:
    def __init__(self, dictionary):
        """
        Реализует дерево зависимостей слов в предложении в формате json. Каждый элемент дерева
        содержит информацию о соответствующем слове: зависимость от других слов, pos-тег,
        лемму слова и его эмоциональную окраску.
        :param dictionary: Тональный словарь
        """
        self.dictionary = dictionary
        self.main_dep = ['nsubj', 'nsubj:pass', 'obj', 'iobj', 'obl', 'obl:agent', 'nmod', 'amod', 'det',
                         'advmod']  # Зависимости пар слов, за которыми следим
        self.sentiment_by_dictionary = None  # Дерево зависимостей с тональностью слов, определенной по тональному словарю
        self.sentiment_by_rules = None  # Дерево зависимостей с тональностью слов, определенной по правилам
        self.sentence_sentiment = None  # Итоговая тональность предложения TODO: поменять на метод get_sentence_sentiment
        self.found_rules = []  # Найденные в предложении правила
        self.unknown_words = []  # Неизвестные слова
        self.nlp = spacy.load("ru_core_news_lg")

    def refresh_data(self) -> None:
        """
        Сбрасывает информацию по предложению.
        """
        self.found_rules = []
        self.unknown_words = []
        self.sentiment_by_dictionary = None
        self.sentiment_by_rules = None
        self.sentence_sentiment = None

    def _create_node(self, parents_children: [], id: int, parent_id: int, text: str,
                     dependency: str, pos: str, lemma: str, sentiment: str) -> int:
        """
        Создаёт вершину дерева.
        :param parents_children: массив исходящих вершин родителя
        :param id: уникальный, в пределах дерева, идентификатор вершины
        :param parent_id: идентификатор родителя
        :param text: строковое представление слова
        :param dependency: зависимость слова от его родителя
        :param pos: pos-тег слова
        :param lemma: лемма слова
        :param sentiment: тональность слова
        :return: индекс слова в массиве исходящих вершин родителя
        """
        parents_children.append(
            {'id': id, 'parent_id': parent_id, 'text': text, 'dependency': dependency, 'pos': pos, 'lemma': lemma,
             'sentiment': sentiment, 'children': []})
        return len(parents_children) - 1

    def _create_tree(self, token, parents_children: []) -> None:
        """
        Рекурсивно создает дерево в корне со значением token.
        :param token: корень создаваемого дерева
        :param parents_children: массив исходящих вершин родителя
        :return:
        """
        for child in token:
            if not [child_ for child_ in child.children]:
                if child.is_punct:
                    continue
                if not self.dictionary.is_word_exist(child.lemma_):
                    self.unknown_words.append(child.lemma_)
                self._create_node(parents_children, child.i, child.head.i,
                                  child.text, child.dep_, child.pos_, child.lemma_,
                                  self.dictionary.get_word_tag(child))
            else:
                if not self.dictionary.is_word_exist(child.lemma_):
                    self.unknown_words.append(child.lemma_)
                i = self._create_node(parents_children, child.i, child.head.i,
                                      child.text, child.dep_, child.pos_, child.lemma_,
                                      self.dictionary.get_word_tag(child))
                self._create_tree(child.children, parents_children[i]['children'])

    def generate_tree(self, text):
        """
        Создаёт два дерева: на основе тонального словаря и на основе правил, а так же делает вывод о тональности всего предложения
        :param text: исходный текст предложения
        """
        self.refresh_data()
        doc = self.nlp(text)
        self.sentiment_by_dictionary = dict()
        self.sentiment_by_dictionary['text'] = doc.text

        root = None
        for sent in doc.sents:
            root = sent.root
        if not self.dictionary.is_word_exist(root.lemma_):
            self.unknown_words.append(root.lemma_)
        self.sentiment_by_dictionary['tokens'] = dict()
        self.sentiment_by_dictionary['tokens']['id'] = root.i
        self.sentiment_by_dictionary['tokens']['text'] = root.text
        self.sentiment_by_dictionary['tokens']['dependency'] = root.dep_
        self.sentiment_by_dictionary['tokens']['pos'] = root.pos_
        self.sentiment_by_dictionary['tokens']['lemma'] = root.lemma_
        self.sentiment_by_dictionary['tokens']['sentiment'] = self.dictionary.get_word_tag(root)
        self.sentiment_by_dictionary['tokens']['children'] = []

        self._create_tree(root.children, self.sentiment_by_dictionary['tokens']['children'])

        self.sentiment_by_rules = json.loads(json.dumps(self.sentiment_by_dictionary.copy()))

        aboba = self.search_dep([self.sentiment_by_rules['tokens']], dict({'id': -1, 'children': [root]}))  # Поиск правил

        # print(json.dumps(self.sentiment_by_dictionary, ensure_ascii=False, indent=4))
        # print(json.dumps(self.sentiment_by_rules, ensure_ascii=False, indent=4))

        self.sentence_sentiment = aboba['sentiment']

    def is_parent_has_main_dep(self, parent) -> bool:
        for child in parent['children']:
            if child['dependency'] in self.main_dep:
                return True
        return False

    def show_unknown_words(self) -> None:
        """
        Открывает блокнот и записывает в него неизвестные слова конкретного предложения.
        """
        self.unknown_words = list(set(self.unknown_words))  # only unique

        autoit.run("notepad.exe")
        autoit.win_wait_active("[CLASS:Notepad]", 3)
        for element in self.unknown_words:
            autoit.control_send("[CLASS:Notepad]", "Edit1", element + "\n")

    def search_dep(self, json_tree: list[dict], parent):
        dep_array = []
        for element in json_tree:
            if element['children']:
                element = self.search_dep(element['children'], element)
            if element['dependency'] in self.main_dep:
                dep_array.append(self.calculate_sentiment_by_rules(parent, element))
                self.found_rules.append(
                    f"{element['text']} {parent['text']} | ПРАВИЛО: {get_sentiment_type(element['dependency'])} | DEP: {element['dependency']} | POS: {element['pos']}")

            elif (len(parent['children']) == 1) or (len(parent['children']) > 1 and element['sentiment'] != SentimentType.NEUTRAL.value) or not self.is_parent_has_main_dep(parent):
                if element['dependency'] == 'ROOT':
                    dep_array.append(element['sentiment'])
                elif parent['sentiment'] == element['sentiment']:
                    dep_array.append(element['sentiment'])
                elif parent['sentiment'] == SentimentType.NEGATIVE.value and element['sentiment'] == SentimentType.POSITIVE.value:
                    dep_array.append(SentimentType.NEUTRAL.value)
                elif element['sentiment'] == SentimentType.NEGATIVE.value and parent['sentiment'] == SentimentType.POSITIVE.value:
                    dep_array.append(SentimentType.NEUTRAL.value)
                elif parent['sentiment'] == SentimentType.POSITIVE.value and element['sentiment'] == SentimentType.NEUTRAL.value:
                    dep_array.append(SentimentType.POSITIVE.value)
                elif element['sentiment'] == SentimentType.POSITIVE.value and parent['sentiment'] == SentimentType.NEUTRAL.value:
                    dep_array.append(SentimentType.POSITIVE.value)
                elif parent['sentiment'] == SentimentType.NEGATIVE.value and element['sentiment'] == SentimentType.NEUTRAL.value:
                    dep_array.append(SentimentType.NEGATIVE.value)
                elif element['sentiment'] == SentimentType.NEGATIVE.value and parent['sentiment'] == SentimentType.NEUTRAL.value:
                    dep_array.append(SentimentType.NEGATIVE.value)
            elif len(parent['children']) > 1 and element['sentiment'] == SentimentType.NEUTRAL.value:
                continue

        parent['sentiment'] = self.calculate_node_sentiment_recoloring(dep_array)
        print(dep_array)
        return parent

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
                    return negative  # было neutral
            if child['sentiment'] == positive:
                if parent['sentiment'] == positive:
                    return positive
                if parent['sentiment'] == negative:
                    return neutral
                if parent['sentiment'] == neutral:
                    return positive
            if child['sentiment'] == neutral:
                if parent['sentiment'] == positive:
                    if parent['dependency'] in ['nsubj', 'nsubj:pass',
                                                'ROOT']:  # Положительный, если определяется подлежащее ROOT????
                        return positive
                    elif parent['dependency'] in ['obj', 'iobj', 'nmod']:  # нейтральный, если определяется дополнение
                        return neutral
                    else:
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
            if child['dependency'] == 'advmod' and child['text'].lower() == 'не':
                if parent['sentiment'] == positive:
                    return negative
                if parent['sentiment'] == negative:
                    return positive
                if parent['sentiment'] == neutral:
                    return neutral
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
