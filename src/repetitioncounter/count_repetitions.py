def count_repetitions(tokens):
    occurrences = {}

    current_phrase_start_counter = 0
    while current_phrase_start_counter < len(tokens):
        current_word = tokens[current_phrase_start_counter]
        current_phrase_end_counter = current_phrase_start_counter + 1
        while current_phrase_end_counter < len(tokens):
            current_phrase = tokens[current_phrase_start_counter:current_phrase_end_counter]
            current_phrase_as_string = " ".join(current_phrase)
            if current_phrase_as_string in occurrences:
                current_phrase_end_counter = current_phrase_end_counter + 1
                continue
            current_phrase_size = current_phrase_end_counter - current_phrase_start_counter
            comparison_phrase_start_counter = current_phrase_end_counter
            comparison_phrase_end_counter = current_phrase_end_counter + current_phrase_size

            while comparison_phrase_end_counter < len(tokens) + 1:
                comparison_phrase = tokens[comparison_phrase_start_counter:comparison_phrase_end_counter]
                if comparison_phrase == current_phrase:
                    if current_phrase_as_string in occurrences:
                        occurrences[current_phrase_as_string] = occurrences[current_phrase_as_string] + 1
                    else:
                        occurrences[current_phrase_as_string] = 2

                comparison_phrase_start_counter = comparison_phrase_start_counter +1
                comparison_phrase_end_counter = comparison_phrase_end_counter + 1

            current_phrase_end_counter = current_phrase_end_counter +1

        current_phrase_start_counter = current_phrase_start_counter + 1

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

