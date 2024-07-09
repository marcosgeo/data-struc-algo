
## creating

my_dict1 = dict()

my_dict2 = {}

eng_esp = dict(one='uno', two='dos', three='tres')
print(eng_esp)

eng_esp2 = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng_esp2)

eng_esp3 = dict([('one', 'uno'), ('two', 'dos'), ('three', 'tres')])
print(eng_esp3)


def count_word_frequency(words) -> dict:
    """
    Count the frequency of words in a given list of words
    :param words:
    :return dict:
    """
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    This function takes two dictionaries as parameters and merge
    them summing the values of common keys.
    :param dict1:
    :param dict2:
    :return:
    """
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value

    return result


def max_value_key(the_dict: dict) -> int:
    """
    This function takes a dictionary as parameter and returns the key
    with the highest value
    :param the_dict:
    :return:
    """
    max_value = max(the_dict.values())
    for key, value in the_dict.items():
        if value == max_value:
            return key
    # clever solution
    # return max(the_dict, key=the_dict.get)


def reverse_dict(the_dict) -> dict:
    """
    This function takes a dictionary as parameter and returns a new dictionary
    in which the key-value pairs are reversed
    :param the_dict:
    :return:
    """
    return {v: k for k, v in the_dict.items()}


def filter_dict(the_dict: dict, function: callable) -> dict:
    """
    This function takes a dictionary as a parameter and returns a dictionary
    with elements based on a condition.
    :param the_dict:
    :param function:
    :return dict:
    """
    result = {}
    for k, v in the_dict.items():
        if function(k, v):
            result[k] = v

    return result
    # using comprehension
    # return {k: v for k, v in the_dict.items() if function(k, v)}


def check_same_frequency(list1, list2) -> bool:
    """
    This function takes two lists as parameters and check if they have
    the same frequency on elements.
    :param list1:
    :param list2:
    :return:
    """
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter

    return count_elements(list1) == count_elements(list2)
