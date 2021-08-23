import controllers.controller as global_config
from package.classics.substitution.vigenere_class import  Vigenere


def encode_decode(text: str, keys: list, crypt: bool = True)-> list:
    general = {
        "action" : "",
        "method": "Vigenere", 
        "text": text, 
        "result": []
    }

    vigenere = Vigenere(all_set=global_config.alphabet)
    general['text'] = global_config.check_and_validate_text(text=general['text'])
    keys = [ global_config.check_and_validate_text(text=key) for key in keys]
    

    if crypt:
        general['action'] = "Crypt"
        for key in keys:
            general["result"].append({
                "key": key,
                "text": vigenere.crypt(text=general["text"], key=key)
            })
    else:
        general['action'] = "Decrypt"
        for key in keys:
            general["result"].append({
                "key": key,
                "text": vigenere.decrypt(text=general["text"], key=key)
            })
    
    global_config.print_to_json(results=general)

    return general