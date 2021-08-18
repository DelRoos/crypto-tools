import utils.errors.constant as constant


class Error:
    __values = []
 
    def __init__(self, val: str, message: str):
        self.__values.append(val)
        self.message = message

    def set_val(self, val: str)-> bool:
        if val not in self.values:
            self.__values.append(val)
            return True
        return False
    
    def get_val(self) -> list:
        return self.__values

    def solve(self, text: str, code: str)-> str:
        if code == constant.CHARACT_NOT_EXIST_IN_SET:
           return "".join(map(str, [ text.replace(letter, '') for letter in self.__values ])) 