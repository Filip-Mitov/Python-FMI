import re


def matcher(regex, string):
    match = re.search(regex, string)

    if match is None:
        return False

    start, end = match.span()
    return string[:start] + '(' + string[start:end] + ')' + string[end:]

