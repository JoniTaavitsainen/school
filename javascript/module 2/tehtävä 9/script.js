function even(numbers) {
  const evenNumbers = [];
  for (const number of numbers) {
    if (number % 2 === 0) evenNumbers.push(number);
  }
  return evenNumbers;
}

const numbers = [2, 7, 4];
const evenNumbers = even(numbers);
console.log("Original array:", numbers);
console.log("Even numbers:", evenNumbers);
