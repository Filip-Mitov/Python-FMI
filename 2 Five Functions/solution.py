def is_pangram(sentence):
    all_symbols = set()
    for symbol in sentence:
        if ord('А') <= ord(symbol) and ord(symbol) <= ord('я'):
            all_symbols.add(symbol.lower())

    return len(all_symbols) == 30

def char_histogram(text):
    histogram_symbols = {}
    for symbol in text:
        if not symbol in histogram_symbols:
            histogram_symbols.setdefault(symbol, 1)
        else:
            histogram_symbols[symbol] += 1

    return histogram_symbols

def sort_by(func, arguments):
    for outter_index in range(len(arguments)):
        for index in range(len(arguments) - 1):
            if func(arguments[index], arguments[index+1]) > 0:
                arguments[index], arguments[index + 1] = arguments[index + 1],\
                    arguments[index]

    return arguments

def group_by_type(dictionary):
    grouped_types = {}
    for key in dictionary:
        if not type(key) in grouped_types:
            grouped_types[type(key)] = {key: dictionary[key]}
        else:
            grouped_types[type(key)].update({key: dictionary[key]})

    return grouped_types

def anagrams(words):
    anagram_words = {}
    for one_word in words:
        key_symbols = [symbol.lower() for symbol in one_word \
            if symbol.isalpha()]

        key_symbols.sort()
        key_symbols = str(key_symbols)

        if not key_symbols in anagram_words:
            anagram_words[key_symbols] = [one_word]
        else:
            anagram_words[key_symbols].append(one_word)

    return list(anagram_words.values())
