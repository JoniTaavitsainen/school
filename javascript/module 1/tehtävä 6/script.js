const result = document.querySelector("#result");

if (!confirm("Should I calculate the square root?")) {
  result.textContent = "The square root is not calculated.";
} else {
  const input = prompt("Enter a number:");
  const number = Number(input);
  if (input === null || input.trim() === "" || !Number.isFinite(number)) {
    result.textContent = "Please enter a valid number.";
  } else if (number < 0) {
    result.textContent = "The square root of a negative number is not defined";
  } else {
    result.textContent = `The square root of ${number} is ${Math.sqrt(number)}.`;
  }
}
