import re
import constant 

def remove_russian_letter(text) :
    for i in range(0, len(text)) :
        if re.search("[а-яА-Я]", text[i]) :
            text = text.replace(text[i], " ")
    
    return text

def number_of_sentences(text : str) :
    text = remove_russian_letter(text)
    
    count = len(re.findall(constant.SENTENCE_PATTERN, text))

    quote_splitting = text.split("\"")
    for i in range(0, len(quote_splitting)) :
        if i % 2 == 0 and i != 0 :
            count += len(re.findall("^ [A-Z]", quote_splitting[i]))

            if i == len(quote_splitting) - 1 and quote_splitting[i] == "":
                count += 1
        elif i % 2 == 1 :
            count -= len(re.findall(constant.SENTENCE_PATTERN, quote_splitting[i])) 

    count -= sum(initials.count(".") for initials in re.findall(constant.INITIALS, text))

    for abbr in constant.ONE_WORD_ABBREVIATIONS :
        count -= len(re.findall(abbr + "(?:,+| [a-z])", text)) #  + " [A-Z]{1,}" posle abb s malenkoy bukvi

    for abbr in constant.NOT_END_ONE_WORD_ABBREVIATIONS :
        count -= len(re.findall(abbr, text))

    for abbr in constant.TWO_WORDS_ABBREVIATIONS :
        count -= len(re.findall(abbr + "(?:,+| [a-z])", text)) * 2
        count -= len(re.findall(abbr + " [A-Z]", text))
        count -= len(re.findall(abbr + "$", text))
    
    return count

def number_of_non_declaration_sentances(text : str) :
    text = remove_russian_letter(text)

    count = len(re.findall(constant.NON_DECLARATIVE_SENTENCE_PATTERN, text))

    quote_splitting = text.split("\"")
    for i in range(0, len(quote_splitting)) :
        if i % 2 == 1 :
            count -= len(re.findall(constant.NON_DECLARATIVE_SENTENCE_PATTERN, quote_splitting[i])) 

    return count

def average_length_of_sentences(text :str) :
    text = remove_russian_letter(text)
    words = re.findall(constant.WORD_PATTERN, text)
    
    return round(sum(len(word) for word in words) / number_of_sentences(text), 2) if number_of_sentences(text) != 0 else 0

def average_length_of_words(text : str) :
    text = remove_russian_letter(text)
    words = re.findall(constant.WORD_PATTERN, text)
 
    return round(sum(len(word) for word in words) / len(words), 2) if len(words) != 0 else 0

def top_k_repeated_ngrams(text : str, k = 10, n = 4) : 
    text = remove_russian_letter(text) #.lower() # register consider

    words = re.findall(constant.WORD_PATTERN, text)

    seq = [words[i:] for i in range(n)]
 
    ngrams = [" ".join(ngram) for ngram in list(zip(*seq))]

    dict = {}

    for ngram in ngrams :
        if ngram not in dict :
            dict[ngram] = 1
        else :
            dict[ngram] += 1

    return sorted(dict.items(), key = lambda x: x[1], reverse = True)[0:k] 