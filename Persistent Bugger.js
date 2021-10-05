function persistence(num) {
    const numArr = ('' + num).split('');
    let tempArr = ('' + num).split('');

    console.log(tempArr);

    if (numArr.length === 1 || !num) {
        return 0;
    }

    let result = 0;
    let multi = +tempArr[0];

    while (tempArr.length >= 2) {
      
        for (let j = 0; j < tempArr.length - 1; j++) {
            multi *= +tempArr[j + 1];
        }
      
        tempArr = ('' + multi).split('');
        multi = +tempArr[0]
        result++;
    }

    return result
}
