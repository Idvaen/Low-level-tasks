function sumTwoSmallestNumbers(numbers) {  
  numbers.sort((a, b) => {
      return a - b;
  });

  let sum = 0;
  for (let i = 0; i < 2; i++) {
      sum += numbers[i];
  }
  
  return sum;
}
