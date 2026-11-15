const input = prompt("Enter an integer:");
const number = Number(input);
const result = document.querySelector("#result");

if (input === null || input.trim() === "" || !Number.isSafeInteger(number)) {
  result.textContent = "Please enter a valid integer.";
} else {
  let prime = number >= 2;
  for (let divisor = 2; prime && divisor <= Math.sqrt(number); divisor++) {
    if (number % divisor === 0) prime = false;
  }
  result.textContent = `${number} is ${prime ? "" : "not "}a prime number.`;
}
