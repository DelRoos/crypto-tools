import string

class SetAlphabet:
    def __init__(self):
        self.set_ascii: list = list(string.ascii_lowercase)

    def give_param_of_set(self, lower = False, upper  = False, digits = False, punctuation = False)-> str:
        str_alpha = ''

        if lower :
            str_alpha += string.ascii_lowercase
        if upper :
            str_alpha += string.ascii_uppercase
        if digits :
            str_alpha += string.digits
        if punctuation :
            str_alpha += string.punctuation
        
        if str_alpha == '':
            str_alpha = string.ascii_lowercase
            
        self.set_ascii = list(str_alpha)
        return self.set_ascii