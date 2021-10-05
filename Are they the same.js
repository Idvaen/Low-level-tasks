function comp(array1, array2){

  if (array1 === '' || array2 === '') {
    return false;
  }
  
   if (array1 === null || array2 === null) {
    return false;
  }
  
  if (array1.length < 1 || array2.length < 1) {
    return true;
  }
  
  return array2.map(Math.sqrt).reduce((a, b) => a + b) === array1.reduce((a, b) => a + b);
}
