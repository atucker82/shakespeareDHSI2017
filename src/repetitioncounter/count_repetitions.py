def count_repetitions(tokens):
    occurrences = {}

    current_word_counter = 0
    while current_word_counter < len(tokens):
        current_word = tokens[current_word_counter]
        if current_word not in occurrences:
            for next_word in tokens[current_word_counter +1:]:
                if current_word == next_word:
                    if current_word in occurrences:
                        occurrences[current_word] = occurrences[current_word] + 1
                    else:
                        occurrences[current_word] = 2

        current_word_counter = current_word_counter + 1


    return occurrences

def tokenize(line):
    tokens = []
    lowercased_line = line.lower()
    punctuation_to_remove = '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~'
    without_punctuation = ""
    for character in lowercased_line:
        if character not in punctuation_to_remove:
            without_punctuation = without_punctuation + character
    split = without_punctuation.split(" ")
    for token in split:
        if token != '':
            tokens.append(token)

    return tokens

