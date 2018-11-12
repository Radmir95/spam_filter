import codecs

# need optimization in future
def preprocess_data(data):

    with codecs.open('words_to_exclude', 'r', 'utf-8') as words_to_exclude:
        words = words_to_exclude.read().split(',')

    data_processed = []
    for data_word in data:
        current_word = data_word
        for word_excl in words:
            words_t = current_word.split()
            if words_t.__contains__(word_excl):
                words_t.remove(word_excl)
            current_word = ''
            for w in words_t:
                current_word += " " + w
        data_processed.append(current_word.lstrip(" "))
    return data_processed


preprocess_data(["привет в мир!"])

