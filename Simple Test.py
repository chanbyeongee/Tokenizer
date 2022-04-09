from hangul_utils import split_syllables
import pandas as pd

words = pd.read_csv("kor_dict.txt",sep=" ",names=["term","freq"])
words.term = words.term.map(split_syllables)
words.to_csv("kor_phrase_dict.txt",sep=" ",header=None,index=None)


