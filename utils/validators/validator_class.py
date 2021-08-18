import utils.errors.constant as constant
from utils.errors.error_class import Error

class Validator:
    errors: Error = []
    
    def check_letter_in_set(self, charact: str, all_set: list)-> bool:
        if charact in all_set:
            return True
        else:
            if not self.__message_exist_in_errors(constant.CHARACT_NOT_EXIST_IN_SET):
                self.errors.append(
                    Error(
                        val = charact,
                        message = constant.CHARACT_NOT_EXIST_IN_SET
                    )
                )
            else:
                for error in self.errors:
                    if error.message == constant.CHARACT_NOT_EXIST_IN_SET:
                        error.set_val(val = charact)
                        break

            return False

    def __message_exist_in_errors(self, message: str) -> bool:
        for error in self.errors:
            if message == error.message:
                return True
        return False