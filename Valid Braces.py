def validBraces(string):
    result_dict = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    result = []
    
    for str in string:
        if isClosedBraces(str):
            try:
                if result_dict[str] != result.pop():
                    return False
            except:
                continue
        else:
            result.append(str)
    return len(result) == 0


def isClosedBraces(b):
    try:
        return [')', ']', '}'].index(b) >= 0
    except:
        return False
