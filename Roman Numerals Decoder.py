def solution(roman):
    symbol_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    result = 0
    
    if len(roman) == 1:
        return symbol_dict[roman[0]]

    for i in range(len(roman)-1):
        if symbol_dict[roman[i]] >= symbol_dict[roman[i+1]]:
            if result == 0:
                result = symbol_dict[roman[0]]
            result += symbol_dict[roman[i+1]]
        elif symbol_dict[roman[i]] < symbol_dict[roman[i+1]]:
            if result == 0:
                result = symbol_dict[roman[0]]
            result = (result - symbol_dict[roman[i]]) + \
                symbol_dict[roman[i+1]] - symbol_dict[roman[i]]
            
    return result
