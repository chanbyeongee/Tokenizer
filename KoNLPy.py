from konlpy.tag import Mecab

class KoNLPy:
    def __init__(self,score_sheet=None):
        self.mecab = Mecab()
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

    def analyze(self,text):
        return self.mecab.pos(text)

    def get_morphs(self,text):
        return self.mecab.morphs(text)

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
        self.mecab.set_evaluator(weights,func)

    def _max_length_of_noun(self, wordpos_list):
        satisfied = [len(wordpos[0]) for wordpos in wordpos_list if wordpos[1] == 'Noun']
        return max(satisfied) if satisfied else 0

if __name__ == "__main__":
    text = "내가 그린 기린 그림."
    test = KoNLPy()
    raw_answer = test.analyze(text)
    print(raw_answer)
    print(test.get_morphs(text))

