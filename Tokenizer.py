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
        self.max_score=-99

    def extract(self,text):
        spaced_text = self.spacing.convert(text)
        extracted_text = self._appropriate_checker(spaced_text)
        return extracted_text

    def _appropriate_checker(self,text):

        self.candidate_list=[]
        self.max_score = -99

        first_time_extract = self.tokenize.analyze(text)
        checked_text = ""

        return checked_text

    def _recrusive_checker(self,candidate):
        """
        TODO: 재귀적으로 돌면서, 각 형태소를 맞춤법 검사를 하거나, 앞뒤로 더해보며 점수가 높은경우에 맞춤법 검사를 함.

        """


if __name__ == "__main__":
    print("Something To do")

