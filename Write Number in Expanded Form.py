def expanded_form(num):
    result = ''
    count = len(str(num)) - 1

    for i in str(num):
        if i != '0':
            result += f'{i}'+'0'*count + ' ' + '+' + ' '
        count -= 1
        
    return result[:-3]
