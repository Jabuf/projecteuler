def is_palindrome(string):
    palindrome = False
    string_length = len(string)

    if string_length % 2 == 0:
        length_for_comparaison = int(string_length / 2)
    else:
        length_for_comparaison = int((string_length - 1) / 2)

    if string[length_for_comparaison:] == inverse_string(string[:-length_for_comparaison]):
        palindrome = True

    return palindrome


def inverse_string(string):
    inversed_string = ""

    for i in range(len(string), 0, -1):
        inversed_string += string[i - 1]

    return inversed_string
