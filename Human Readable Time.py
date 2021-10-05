def make_readable(seconds):
    minute = seconds // 60
    hour = minute // 60

    if seconds >= 0 and seconds < 60:
        if len(str(seconds)) == 1:
            return f'00:00:0{seconds}'
        else:
            return f'00:00:{seconds}'
    elif seconds >= 60 and seconds < 3600:
        if seconds == 60:
            return '00:01:00'
        if len(str(minute)) == 1:
            if len(str(seconds % 60)) == 1:
                return f'00:0{minute}:0{minute % 60}'
            return f'00:0{minute}:{minute % 60}'
        return f'00:{minute}:{minute % 60}'
    elif seconds >= 3600 and seconds < 360000:
        if len(str(hour)) == 1:
            if len(str(minute % 60)) == 1 and len(str(seconds % 60)) == 1:
                return f'0{hour}:0{minute%60}:0{seconds%60}'
            elif len(str(minute % 60)) == 1:
                return f'0{hour}:0{minute%60}:{seconds%60}'
            elif len(str(seconds % 60)) == 1:
                return f'0{hour}:{minute%60}:0{seconds%60}'

            return f'0{hour}:{minute%60}:{seconds%60}'

        if len(str(minute % 60)) == 1 and len(str(seconds % 60)) == 1:
            return f'{hour}:0{minute%60}:0{seconds%60}'
        elif len(str(minute % 60)) == 1:
            return f'{hour}:0{minute%60}:{seconds%60}'
        elif len(str(seconds % 60)) == 1:
            return f'{hour}:{minute%60}:0{seconds%60}'

        return f'{hour}:{minute%60}:{seconds%60}'
    else :
        return None
