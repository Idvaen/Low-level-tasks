def solution(args):
    result = ''
    tmp_res = list()
    tmp_res.append(args[0])

    for i in range(0, len(args)-1):
        if args[i+1] - args[i] == 1:
            tmp_res.append(args[i+1])
        else:
            if len(tmp_res) > 2:
                if result == '':
                    result = f'{tmp_res[0]}-{tmp_res[-1]},'
                else:
                    result += f'{tmp_res[0]}-{tmp_res[-1]},'
                tmp_res = [args[i+1]]
            elif len(tmp_res) == 2:
                result += f'{tmp_res[0]},{tmp_res[1]},'
                tmp_res = [args[i+1]]
            elif tmp_res:
                result += f'{tmp_res[0]},'
                tmp_res = [args[i+1]]
            tmp_res = [args[i+1]]

        if i == len(args)-2:
            if len(tmp_res) > 2:
                if result == '':
                    result = f'{tmp_res[0]}-{tmp_res[-1]},'
                else:
                    result += f'{tmp_res[0]}-{tmp_res[-1]},'
            elif len(tmp_res) == 2:
                result += f'{tmp_res[0]},{tmp_res[1]},'
            elif tmp_res:
                result += f'{tmp_res[0]},'

    return result.rstrip(',')
