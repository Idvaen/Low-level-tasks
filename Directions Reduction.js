function dirReduc(arr) {
    if (!arr) {
        return [];
    }
  
    let i = 0;

    while (i < arr.length) {
        arr = arr.join(' ').replace('NORTH SOUTH', ' ').replace('SOUTH NORTH', ' ').replace('WEST EAST', ' ').replace('EAST WEST', ' ').trim().replace('  ', '').split(' ');
        i++;
    }
  
    if (arr[0] === '') {
        return [];
    }

    return arr;
}
