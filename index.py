def isMatch(inputString, pattern):
    if not pattern:
        return not inputString

    first_matching = bool(inputString) and pattern[0] in {inputString[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (isMatch(inputString, pattern[2:]) or (first_matching and isMatch(inputString[1:], pattern)))
    else:
        return first_matching and isMatch(inputString[1:], pattern[1:])


if __name__ == '__main__':

    str = "abc"
    patternInput = ".b.*"
    print(isMatch(str, patternInput))