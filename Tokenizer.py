from MakeSpace import MakeSpace
from Hanspell import Hanspell
from KoNLPy import KoNLPy
from hangul_utils import split_syllables
import json
import numpy as np

#1. 먼저 띄어쓰기한다
#2. 띄어쓰기된 단어하나하나 교정해보면서
#3. 동시에 토크나이저를 해본다, 점수가 높은것으로 해본다.

class Tokenizer:
    def __init__(self):
        self.spacing=MakeSpace()
        self.spell_checker=Hanspell()
        self.tokenize = KoNLPy()
        self.candidate_list=[]
        self.jamo_dict = self._load_jamo()
        self.dim = 7

    def get_dim(self):
        return self.dim

    def auto_embedded(self, text):

        tagged = self.extract(text)
        embedded = self._embedding(tagged)

        return embedded

    def extract(self,text):
        extracted_text = self._appropriate_checker(text)
        return extracted_text

    def _load_jamo(self):
        with open("jamo_dict.json", 'r') as f:
            data = json.load(f)

        return data

    def _embedding(self, tagged):

        embedded = []

        for (word, tag) in tagged:
            jamo = split_syllables(word)

            if tag.startswith('N'):
                temp = [self.jamo_dict[sep] for sep in jamo]
                embedded.append(temp)
            elif tag.startswith('V'):
                temp = [self.jamo_dict[sep] * -1 for sep in jamo]
                embedded.append(temp)

        result = [np.array(vec) @ (np.reshape(np.arange(1, len(vec)*self.dim+1),(len(vec), self.dim))) for vec in embedded]


        return result

    def _appropriate_checker(self, text):

        raw_text_list = text.split(" ")
        temp_text_list = raw_text_list

        max_score = -99

        for (temp_idx,temp), (raw_idx,raw) in zip(enumerate(temp_text_list),enumerate(raw_text_list)):
            temp_text_list[temp_idx] = temp = self.spell_checker.check(temp)
            if temp == raw :
                continue
            checked_text = " ".join(temp_text_list)
            tagged = self.tokenize.analyze(checked_text)

            if max_score <= self.tokenize.evaluate(tagged) :
                raw_text_list[raw_idx] = temp

        checked_text = " ".join(temp_text_list)
        tagged = self.tokenize.analyze(checked_text)

        return tagged

if __name__ == "__main__":
    text="안뇽하세요? 나는 이병찬이얌."
    token = Tokenizer()

    print(token.auto_embedded(text))



