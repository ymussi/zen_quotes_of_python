from zen.config import Config

class Quotes():

    LANGS_ = Config.get('quotes', 'langs').split(',')

    @classmethod
    def get_quotes(cls, number=None, lang=None):
        if number is not None and int(number) > 19:
            resp = 'Citation referring to the number informed not found. The Zen of Python has a total of 19 quotes.'
        elif lang is None:
            quotes = Config.get('quotes', 'zen_en')
            resp = {"quotes": [el.strip() for el in quotes.split('/')] if number is None else quotes.split('/')[int(number)-1].strip()}
        elif lang in cls.LANGS_:
            quotes = Config.get('quotes', f'zen_{lang}')
            resp = {"quotes": [el.strip() for el in quotes.split('/')] if number is None else quotes.split('/')[int(number)-1].strip()}
        else:
            resp = f'Unidentified language requested. Available languages are: {cls.LANGS_}.'
        
        return resp
