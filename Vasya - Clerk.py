def tickets(people): 
    sum = 0
    
    if people[len(people) - 1] != 100:
        sum += 25
    

    for person in people:
        if person == 25:
            sum += 25
        elif person == 50:
            sum -= 25
        elif person == 100:
            sum -= 75
            
        if sum >= 0:
            continue
        else:
            return 'NO'
    
    return "YES"
