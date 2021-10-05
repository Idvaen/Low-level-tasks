function digPow(n, p){
  const numArr = n.toString().split('');
  let pow = p;
  let sumResult = 0;
  
  for (let i = 0; i < numArr.length; i++) {
    sumResult += ((+numArr[i]) ** pow);
    pow++;
  }
  
  const k = +((sumResult / n).toFixed());
  
  if (sumResult === n * k) {
    return k;
  }
  
  return -1;
}
