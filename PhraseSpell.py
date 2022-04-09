from symspellpy import SymSpell, Verbosity
from hangul_utils import split_syllables, join_jamos

class PhraseSpell :
    def __init__(self,max_edit_distance=5):
        self.sym_spell = SymSpell(max_dictionary_edit_distance=max_edit_distance)
        self.dict_db_path = "kor_phrase_dict.txt"
        self.max_edit_distance=max_edit_distance

    def load(self):
        self.sym_spell.load_dictionary(self.dict_db_path,0,1,encoding="UTF8")

    def correct(self,text):
        text = split_syllables(text)
        suggestions = self.sym_spell.lookup(text,Verbosity.ALL,self.max_edit_distance)

        if not suggestions:
            return join_jamos(text)
        else :
            return join_jamos(suggestions[0].term)

if __name__ == "__main__":
    my_correct_spell = PhraseSpell(max_edit_distance=2)
    my_correct_spell.load()

    while 1 :
        text = input("입력하세요: ")
        if text == "quit":
            break
        else :
            print(my_correct_spell.correct(text))
