def count_words(str: str):
    words = str.split()
    return len(words)


def count_characters(str: str):
    result = {}
    for i in range(0, len(str)):
        char = str[i].lower()

        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result
