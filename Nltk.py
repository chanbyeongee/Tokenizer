from nltk.tokenize import word_tokenize
import nltk
from googletrans import Translator

translator = Translator()

text = "지금 애플 공홈에서 에어팟 프로 50% 할인중이야 ㅋㅋ"

result = translator.translate(text, dest='en')

new_text= word_tokenize(result.text)
print(nltk.pos_tag(new_text))

