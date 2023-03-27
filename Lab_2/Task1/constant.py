SENTENCE_PATTERN = "[.!\?]+"
NON_DECLARATIVE_SENTENCE_PATTERN = "[!\?]+"

WORD_PATTERN = "(?=.*[a-zA-Z])[a-zA-Z0-9]+"

NUMBER_PATTERN = "\b\d+\b"

INITIALS = "[A-Z]\. [A-Z]\. [A-Z][a-z]+"

ONE_WORD_ABBREVIATIONS = [ "etc.", "vs.", "jr.", "sr.", "mr.", "ms.", "mrs.", "smb.", "smth.", "adj.", "prep.", "pp.", "par.", "ex.",
    "pl.", "edu.", "appx.", "sec.", "gm.", "cm.", "yr.", "jan.", "feb.", "mar.",
    "apr.", "jun.", "jul.", "aug.", "sep.", "oct.", "nov.", "dec.", "mon.", "tue.", "wed.", "thu", "fri.", "sat.", "sun."]

TWO_WORDS_ABBREVIATIONS = ["e.g.", "i.e.", "p.s.", "ph.d."]