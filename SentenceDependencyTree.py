from collections import Counter
import json


class SentenceDependencyTree:
    def __init__(self, text, dictionary):
        self.dictionary = dictionary
        self.main_dep = ['nsubj', 'nsubj:pass', 'obj', 'iobj', 'obl', 'obl:agent', 'nmod', 'amod', 'det', 'advmod']  # Зависимости пар слов, за которыми следим
        self.found_rules = []

        self.sentiment_by_dictionary = None
        self.sentiment_by_rules = None
        self.sentence_sentiment = None

        self.generate_tree(text)

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
                            child.text, child.dep_, child.pos_, child.lemma_, self.dictionary.get_word_tag(child.lemma_))
            else:
                i = self.create_leaf(parents_children, child.i, child.head.i,
                                child.text, child.dep_, child.pos_, child.lemma_, self.dictionary.get_word_tag(child.lemma_))
                self.create_tree(child.children, parents_children[i]['children'])

    def generate_tree(self, text):
        self.doc = self.dictionary.nlp(text)

        self.sentiment_by_dictionary = dict()
        self.sentiment_by_dictionary['text'] = self.doc.text

        self.root = None
        for sent in self.doc.sents:
            self.root = sent.root

        self.sentiment_by_dictionary['tokens'] = dict()
        self.sentiment_by_dictionary['tokens']['id'] = self.root.i
        self.sentiment_by_dictionary['tokens']['text'] = self.root.text
        self.sentiment_by_dictionary['tokens']['dependency'] = self.root.dep_
        self.sentiment_by_dictionary['tokens']['pos'] = self.root.pos_
        self.sentiment_by_dictionary['tokens']['lemma'] = self.root.lemma_
        self.sentiment_by_dictionary['tokens']['sentiment'] = self.dictionary.get_word_tag(self.root.lemma_)
        self.sentiment_by_dictionary['tokens']['children'] = []

        self.create_tree(self.root.children, self.sentiment_by_dictionary['tokens']['children'])

        self.sentiment_by_rules = json.loads(json.dumps(self.sentiment_by_dictionary.copy()))

        aboba = self.search_dep([self.sentiment_by_rules['tokens']], dict({'id': -1}))  # Поиск правил
        #print(json.dumps(self.sentiment_by_dictionary, ensure_ascii=False, indent=4))
        #print(json.dumps(self.sentiment_by_rules, ensure_ascii=False, indent=4))

        self.sentence_sentiment = aboba['sentiment']

    def search_dep(self, json_tree: list[dict], parent):
        dep_array = []
        for element in json_tree:
            if element['children']:
                element = self.search_dep(element['children'], element)
            if element['dependency'] in self.main_dep:
                dep_array.append(self.calculate_sentiment_by_rules(parent, element))
                self.found_rules.append(
                    f"{element['text']} {parent['text']} | ПРАВИЛО: {self.get_sentiment_type(element['dependency'])} | DEP: {element['dependency']} | POS: {element['pos']}")
                # print(colored(
                #     f"{element['text']} {parent['text']} | ПРАВИЛО: {self.get_sentiment_type(element['dependency'])} | DEP: {element['dependency']} | POS: {element['pos']}",
                #     'green'))
            else:
                dep_array.append(element['sentiment'])
        parent['sentiment'] = self.calculate_node_sentiment_recoloring(dep_array)
        return parent

    def get_sentiment_type(self, dependency):
        if dependency in ['nsubj', 'nsubj:pass']:
            return 'Подлежащее - сказуемое'
        if dependency in ['obj', 'iobj']:
            return 'Дополнение - дополняемое действие'
        if dependency in ['obl', 'obl:agent', 'advmod']:  # advmod &&&
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