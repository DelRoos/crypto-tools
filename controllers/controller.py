import json
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
