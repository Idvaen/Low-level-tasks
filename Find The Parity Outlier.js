function findOutlier(integers) {
  const arr = integers.map(a => Math.abs(a) % 2);
  
  if (arr.reduce((a, b) => a + b) === 1) {
        return integers[arr.indexOf(1)];
    } 
  if (arr.reduce((a, b) => a + b) !== 1){
        return integers[arr.indexOf(0)];
    }
}
