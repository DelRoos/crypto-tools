import json
from utils.validators.validator_class import Validator
from utils.sets.alphabet import SetAlphabet as Alphabet


with open("/Users/user/Documents/Formation/Secu/tools/crypto_tools/config.json") as configuration :
    configs = json.load(configuration)
# print(configs['auto_correction'])

auto_correction = configs['auto_correction']


config_alphabet = configs['alphabet_params']

alphabet = (Alphabet()).give_param_of_set(
    lower=config_alphabet['alpha_lower'],
    upper=config_alphabet['alpha_upper'],
    digits=config_alphabet['numeric'],
    punctuation=config_alphabet['punctuation'],
)



validated = Validator()

def check_and_validate_text(text: str, all_set: list=alphabet)-> str:
    for letter in text:
        validated.check_letter_in_set(charact=letter, all_set=alphabet)

    if validated.errors :
        if auto_correction:
            for error in validated.errors:
                text = error.solve(text=text, code=error.message)
            return text
        else:
            raise("An error occurred")
    
    return text
