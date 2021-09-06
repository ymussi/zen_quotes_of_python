# zen_quotes

A simple library that returns the Zen of Python quotes.

- Installation

    pip install zen_quotes

- Usage
```
# import lib 
from zen.quote import Quotes
```

```
# That will return you all quotes in English.
Quotes.get_quotes()
```

```
# Altogether there are 19 quotations, but if you need only one quotation, 
# then pass the quotation position number on the list.

Quotes.get_quotes(quote=2) # this will return you the second quote on the list in English.

Quotes.get_quotes(quote=2, lang='pt') # this will return you the second quote on the list in Portuguese.

```

- This lib searches the project data: https://github.com/ymussi/zen_of_python

# TODO

- [] add other languages