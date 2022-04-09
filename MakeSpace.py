from pykospacing import Spacing

class MakeSpace:
    def __init__(self):
        self.spacing_mod = Spacing()

    def convert(self,text):
        return self.spacing_mod(text)

if __name__ == "__main__":
    test = MakeSpace()
    msg = "나는이따가밥을먹고양치를하고유튜브를보다가12시에잠을잘것이다."
    converted_msg = test.convert(msg)
    print(converted_msg)