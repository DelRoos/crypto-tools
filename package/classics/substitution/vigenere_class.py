class Vigenere:
    def __init__(self, all_set: list):
        self.all_set = all_set
    
    def crypt(self, text: str, key: str)-> str:
        key = self.__generate_key(text=text, key=key)
        crypt_text = [ 
            self.all_set[
                (self.all_set.index(key[i]) + self.all_set.index(text[i])) % len(self.all_set)
            ] 
            for i in range(len(text))
        ]

        return "".join(map(str, crypt_text))


    def decrypt(self, text: str, key: str)-> str:
        key = self.__generate_key(text=text, key=key)
        crypt_text = [ 
            self.all_set[
                (self.all_set.index(text[i]) - self.all_set.index(key[i])) % len(self.all_set)
            ] 
            for i in range(len(text))
        ]

        return "".join(map(str, crypt_text))

    def __generate_key(self, text: str, key: str):

        length_key = len(key)
        length_text = len(text)

        if length_text == length_key:
            return key
        
        if length_text < length_key:
            key = key[:length_text]
        elif length_text > length_key:
            key = key*(length_text//length_key)+key[:(length_text%length_key)]
        
        return key