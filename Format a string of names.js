function list(names){
  if (names.length < 1) {
    return '';
  }
  
  let result = '';
  
  if (names.length === 1) {
    for (const name of names) {
    result += Object.values(name);
    }
  } else {
    for (const name of names) {
      if (name === names[names.length - 1]) {
        result += ' & ' + Object.values(name);
      } else if (name === names[names.length - 2]){
        result += Object.values(name);
      } else {
        result += Object.values(name) + ', ';
      }
    }
  }
  
  
  return result;
}
