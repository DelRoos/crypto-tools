import controllers.controller as global_config
from utils.validators.validator_class import Validator
from package.classics.shift.cesar.cesar_class import Cesar

def encode_decode(text: str, keys: list, crypt: bool = True)-> list:
    general = {
        "method": "Cesar", 
        "text": text, 
        "result": []
    }

    validated = Validator()
    cesar = Cesar(all_set=global_config.alphabet)

    for letter in text:
        validated.check_letter_in_set(charact=letter, all_set=global_config.alphabet)

    if validated.errors :
        if global_config.auto_correction:
            for error in validated.errors:
                general["text"] = error.solve(text=general["text"], code=error.message)
        else:
            raise("An error occurred")

    if crypt:
        for key in keys:
            general["result"].append({
                "key": key,
                "text": cesar.crypt(text=general["text"], key=key)
            })
    else:
        for key in keys:
            general["result"].append({
                "key": key,
                "text": cesar.decrypt(crypt_text=general["text"], key=key)
            })

    return general