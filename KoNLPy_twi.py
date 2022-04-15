from ckonlpy.tag import Twitter

weights = [
    ('max_length_of_noun', 0.5),
    ('length_of_phrase', 0.1),
    ('exist_noun', 0.2),
    ('single_word', -0.1),
    ('exist_verb', -5)
]

def my_evaluate_function(candidate):

    weights = [
        ('max_length_of_noun', 0.5),
        ('length_of_phrase', 0.1),
        ('exist_noun', 0.2),
        ('single_word', -0.1),
        ('exist_verb', -5)
    ]

    num_nouns = len([word for word, pos, begin, e in candidate if pos == 'Noun'])
    num_words = len(candidate)
    has_no_nouns = (num_nouns == 0)
    len_sum_of_nouns = 0 if has_no_nouns else sum(
        (len(word) for word, pos, _, _ in candidate if pos == 'Noun'))

    num_verbs = len([word for word, pos, begin, e in candidate if pos == "Verb"])
    exist_verb = (num_verbs == 0)

    scores = (num_nouns, num_words, has_no_nouns, len_sum_of_nouns,exist_verb)
    score = sum((score * weight for score, (_, weight) in zip(scores, weights)))
    return score

class KoNLPy:
    def __init__(self,score_sheet=None):
        self.twitter = Twitter()
        self.weights = self._set_weights(score_sheet)

    def evaluate(self, candidate):
        num_nouns = len([word for word, pos in candidate if pos == 'Noun'])
        num_words = len(candidate)

        scores = (
            self._max_length_of_noun(candidate),
            len(text),
            num_nouns > 0,
            num_words == 1,
        )
        score = sum((score * weight for score, (_, weight) in zip(scores, self.weights)))
        return score

    def my_evaluate_function(self,candidate):

        weights = [
            ('max_length_of_noun', 0.5),
            ('length_of_phrase', 0.1),
            ('exist_noun', 0.2),
            ('single_word', -0.1),
            ('exist_verb', -5)
        ]

        num_nouns = len([word for word, pos in candidate if pos == 'Noun'])
        num_words = len(candidate)
        has_no_nouns = (num_nouns == 0)
        len_sum_of_nouns = 0 if has_no_nouns else sum(
            (len(word) for word, pos in candidate if pos == 'Noun'))

        num_verbs = len([word for word, pos in candidate if pos == "Verb"])
        exist_verb = (num_verbs == 0)

        scores = (num_nouns, num_words, has_no_nouns, len_sum_of_nouns, exist_verb)
        score = sum((score * weight for score, (_, weight) in zip(scores, weights)))
        return score

    def analyze(self,text):
        return self.twitter.pos(text)

    def get_morphs(self,text):
        return self.twitter.morphs(text)

    def _set_weights(self, score_sheet):

        if score_sheet == None:
            weights = [
                ('max_length_of_noun', 0.5),
                ('length_of_phrase', 0.1),
                ('exist_noun', 0.2),
                ('single_word', -0.1)
            ]
        else:
            weights = score_sheet

        return weights

    def set_customized_func(self,weights,func):
        self.twitter.set_evaluator(weights,func)

    def _max_length_of_noun(self, wordpos_list):
        satisfied = [len(wordpos[0]) for wordpos in wordpos_list if wordpos[1] == 'Noun']
        return max(satisfied) if satisfied else 0

if __name__ == "__main__":
    text = "내가그린기린그림."
    test = KoNLPy()

    test.set_customized_func(weights,my_evaluate_function)

    raw_answer = test.analyze(text)
    print(raw_answer)
    print(test.my_evaluate_function(raw_answer))
    print(test.get_morphs(text))

