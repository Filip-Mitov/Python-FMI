def wow_such_much(start, end):
    array = []
    for i in range(start, end):
        if i % 3 == 0 and not i % 5 == 0:
            array.append("such")
        elif not i % 3 == 0 and i % 5 == 0:
            array.append("much")
        elif i % 15 == 0:
            array.append("suchmuch")
        else:
            array.append(str(i))

    return array

def count_doge_words(sentence):
    bugs = {"wow":1, "lol":1, "so":1, "such":1, "much":1, "very":1}
    word_sentence = sentence.split()
    counter = 0

    for i in range (0, len(word_sentence)):
        counter += bugs.get(word_sentence[i].casefold(), 0)

    return counter
