class Cesar:
    def __init__(self, all_set: list):
        self.all_set = all_set
        
    def crypt(self, text: str, key=3) -> str:
        crypt_text = [ 
            self.all_set[
                (key + self.all_set.index(letter)) % len(self.all_set)
            ] 
            if letter != " "
            else " " 
            for letter in text
        ]

        return "".join(map(str, crypt_text))


    def decrypt(self, crypt_text: str, key=3) -> str:
        text = [ 
            self.all_set[
                (self.all_set.index(letter) - key) % len(self.all_set)
            ] 
            if letter != " "
            else " " 
            for letter in crypt_text
        ]

        return "".join(map(str, text))

