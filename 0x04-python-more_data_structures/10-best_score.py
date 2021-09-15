#!/usr/bin/python3
def best_score(a_dictionary):

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret, bigt = list(a_dictionary.keys())[0], a_dictionary[ret]
    for key, value in a_dictionary.items():
        if value > bigt:
            ret, bigt = key, value

    return (ret)

