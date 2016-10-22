# -*- coding: utf-8 -*-
from nltk.corpus import names, gazetteers

NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
        'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
        'nineteen', 'twenty', 'thirty', 'fourty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety', 'hundred',
        'thousand', 'million', 'billion', 'trillion']

ORDINALS = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
            'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday',
        'friday', 'saturday', 'sunday']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
            'august', 'september', 'october', 'november', 'december',
            'jan', 'feb', 'mar', 'apr', 'jun', 'jul', 'aug', 'sep', 'sept',
            'oct', 'nov', 'dec']

NAMES = set([name.lower() for filename in ('male.txt', 'female.txt') for name
            in names.words(filename)])

USCITIES = set(gazetteers.words('uscities.txt'))

# [XX] contains some non-ascii chars
COUNTRIES = set([country for filename in ('isocountries.txt','countries.txt')
                for country in gazetteers.words(filename)])

# States in North America
NA_STATES = set([state.lower() for filename in
                ('usstates.txt','mexstates.txt','caprovinces.txt') for state in
                gazetteers.words(filename)])

US_STATE_ABBREVIATIONS = set(gazetteers.words('usstateabbrev.txt'))

NATIONALITIES = set(gazetteers.words('nationalities.txt'))

PERSON_PREFIXES = ['mr', 'mrs', 'ms', 'miss', 'dr', 'rev', 'judge',
                    'justice', 'honorable', 'hon', 'rep', 'sen', 'sec',
                    'minister', 'chairman', 'succeeding', 'says', 'president']

PERSON_SUFFIXES = ['sr', 'jr', 'phd', 'md']

ORG_SUFFIXES = ['ltd', 'inc', 'co', 'corp', 'plc', 'llc', 'llp', 'gmbh',
                'corporation', 'associates', 'partners', 'committee',
                'institute', 'commission', 'university', 'college',
                'airlines', 'magazine']

CURRENCY_UNITS = ['dollar', 'cent', 'pound', 'euro']

ENGLISH_PRONOUNS = ['i', 'you', 'he', 'she', 'it', 'we', 'you', 'they']

RE_PUNCT = '[-!"#$%&\'\(\)\*\+,\./:;<=>^\?@\[\]\\\_`{\|}~]'

RE_NUMERIC = '(\d{1,3}(\,\d{3})*|\d+)(\.\d+)?'

RE_NUMBER = '(%s)(\s+(%s))*' % ('|'.join(NUMBERS), '|'.join(NUMBERS))

RE_QUOTE = '[\'"`]'

RE_ROMAN = 'M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)'

RE_INITIAL = '[A-Z]\.'

RE_TLA = '([A-Z0-9][\.\-]?){2,}'

RE_ALPHA = '[A-Za-z]+'

RE_DATE = '\d+\/\d+(\/\d+)?'

RE_CURRENCY = '\$\s*(%s)?' % RE_NUMERIC

RE_PERCENT = '%s\s*' % RE_NUMERIC + '%'

RE_YEAR = '(\d{4}s?|\d{2}s)'

RE_TIME = '\d{1,2}(\:\d{2})?(\s*[aApP]\.?[mM]\.?)?'
