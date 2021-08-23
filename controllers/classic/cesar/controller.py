import controllers.controller as global_config
from package.classics.shift.cesar.cesar_class import Cesar


def encode_decode(text: str, keys: list, crypt: bool = True)-> list:
    general = {
        "method": "Cesar", 
        "text": text, 
        "result": []
    }

    cesar = Cesar(all_set=global_config.alphabet)
    general['text'] = global_config.check_and_validate_text(text=general['text'])

    if crypt:
        general['action'] = "Crypt"
        for key in keys:
            general["result"].append({
                "key": key,
                "text": cesar.crypt(text=general["text"], key=key)
            })
    else:
        general['action'] = "Decrypt"
        for key in keys:
            general["result"].append({
                "key": key,
                "text": cesar.decrypt(crypt_text=general["text"], key=key)
            })

    return general