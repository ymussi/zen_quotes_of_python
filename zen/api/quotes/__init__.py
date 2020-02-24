from zen.config import Config

class Quotes():
    def __init__(self):
        self.langs = Config.get('quotes', 'langs').split(',')
        print(self.langs)

    def get_quotes(self, lang = None):
        if lang is None:
            quotes = Config.get('quotes', 'zen_en')
            resp = quotes.split('/')
        elif lang in self.langs:
            quotes = Config.get('quotes', f'zen_{lang}')
            resp = quotes.split('/')
        else:
            resp = f'Unidentified language requested. Available languages are: {self.langs}.'
        
        return resp

