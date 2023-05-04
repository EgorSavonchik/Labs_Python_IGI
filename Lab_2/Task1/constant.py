SENTENCE_PATTERN = "[.!\?]+"
NON_DECLARATIVE_SENTENCE_PATTERN = "[!\?]+"

WORD_PATTERN =  "\w*[a-zA-Z]+\w*" #"(?=.*[a-zA-Z])[a-zA-Z0-9]+" pochemy?

NUMBER_PATTERN = "\b\d+\b"

INITIALS = "(?:[A-Z]\. )+[A-Z][a-z]+"

ONE_WORD_ABBREVIATIONS = [ "etc\.", "vs\.", "jr\.", "sr\.", "smb\.", "smth\.", "adj\.", "prep\.", "pp\.", "par\.", "ex\.",
    "pl\.", "edu\.", "appx\.", "sec\.", "gm\.", "cm\.", "yr\.", "Jan\.", "Feb\.", "Mar\.",
    "Apr\.", "Jun\.", "Jul\.", "Aug\.", "Sep\.", "Oct\.", "Nov\.", "Dec\.", "Mon\.", "Tue\.", "Wed\.", "Thu\.", "Fri\.", "Sat\.", "Sun\."]

NOT_END_ONE_WORD_ABBREVIATIONS = ["Mr\.", "Ms\.", "Mrs\.", "Lt\.", "Dr\.", "Rep\."]

TWO_WORDS_ABBREVIATIONS = ["e\.g\.", "i\.e\.", "p\.s\.", "Ph\.d\."]