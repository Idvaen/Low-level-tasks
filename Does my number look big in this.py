def narcissistic(value):
    if len(str(value)) == 1:
        return True

    result = 0

    for val in str(value):
        result += int(val)**len(str(value))

    return result == value
