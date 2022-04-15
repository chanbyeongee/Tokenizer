from MakeSpace import MakeSpace
from Hanspell import Hanspell
from KoNLPy import KoNLPy

#1. 먼저 띄어쓰기한다
#2. 띄어쓰기된 단어하나하나 교정해보면서
#3. 동시에 토크나이저를 해본다, 점수가 높은것으로 해본다.

class Tokenizer:
    def __init__(self):
        self.spacing=MakeSpace()
        self.spell_checker=Hanspell()
        self.tokenize = KoNLPy()
        self.candidate_list=[]


    def extract(self,text):
        spaced_text = self.spacing.convert(text)
        extracted_text = self._appropriate_checker(spaced_text)
        return extracted_text

    def _appropriate_checker(self,text):

        raw_text_list = text.split(" ")
        temp_text_list = raw_text_list

        max_score = -99

        for (temp_idx,temp), (raw_idx,raw
                              ) in zip(enumerate(temp_text_list),enumerate(raw_text_list)):
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
    text="안뇽? 나는 권도완이얌, 그리고 탐정일찌도."

